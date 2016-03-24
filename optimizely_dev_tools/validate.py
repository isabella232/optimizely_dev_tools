import importlib
import localserver
import os
import re
import subprocess
import sys
import yaml

from colorama import Fore, Back, Style, init
from os import path
from pprint import pprint
from pykwalify.core import Core
from pylint import epylint as lint

def print_successful_validation_message(message):
  """Prints success message for validation of the contents of a file

  Args:
    file_name: The file that was successfully validated
  """
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Validated ' + message)

def print_fail_validation_message(exception):
  """Prints fail message for validation of the contents of a file

  Args:
    file_name: The file that yields unsuccessful validation results
    exception: The exception thrown by the file's respective validation function
  """
  print('[' + Fore.RED + 'FAIL' + Style.RESET_ALL + '] ' + str(exception))

def validate_package_name(package_name):
  """Check that package name matches convention

  Args:
    package_name: The package name to validate

  Raises:
    Exception if package name is invalid
  """
  m = re.match('[a-z0-9_]{3,30}', package_name)
  valid = (m != None and m.group(0) == package_name)
  if not valid:
    raise Exception('package name is not valid')

def validate_package_root_exists(package_name):
  """Check that a root folder with the package name exists

  Args:
    package_name: The name of the package's root folder that we are verifying exists

  Raises:
    Exception if folder with package name doesn't exist
  """
  if not path.exists(package_name):
    raise Exception('folder for specified package name doesn\'t exist')

def validate_necessary_files_exist(package_name):
  """Checks that files necessary to the integration/app exist in respective directory

  Args:
    package_name: The name of the package's root folder

  Raises:
    Exception if a required file doesn't exist
  """
  init_py_path = package_name+'/__init__.py'
  if not path.isfile(init_py_path):
    raise Exception('__init__.py doesn\'t exist')
  integration_yaml_path = package_name+'/integration.yaml'
  if not path.isfile(integration_yaml_path):
    raise Exception('integration.yaml doesn\'t exist')
  integration_yaml_map = {}
  f = open(integration_yaml_path)
  data_map = yaml.safe_load(f)
  f.close()
  yaml_root_key = data_map.keys()[0]
  integration_categories = data_map[yaml_root_key]['categories']
  if 'Productivity' in integration_categories or 'Audiences' in integration_categories:
    config_yaml_path = package_name+'/config.yaml'
    if not path.isfile(config_yaml_path):
      raise Exception('config.yaml doesn\'t exist')
  if 'Audiences' in integration_categories:
    # Audience integrations must have functions.js, functions.py, example.js, functions_test.py, config.yaml, and functions_test.js
    functions_js_path = package_name+'/functions.js'
    functions_js_test_path = package_name+'/functions_test.unittests.js'
    functions_py_path = package_name+'/functions.py'
    functions_py_test_path = package_name+'/functions_test.py'
    config_yaml_path = package_name+'/config.yaml'
    if not path.isfile(functions_js_path):
      raise Exception('functions.js doesn\'t exist')
    if not path.isfile(functions_js_test_path):
      raise Exception('functions_test.unittests.js doesn\'t exist')
    if not path.isfile(functions_py_path):
      raise Exception('functions.py doesn\'t exist')
    if not path.isfile(functions_py_test_path):
      raise Exception('functions_test.py doesn\'t exist')

def validate_integration_yaml(package_name):
  """Check that an integration's integration.yaml file has a valid schema

  Raises:
    Exception if the integration.yaml file has an improper schema
  """
  schema_validator = Core(source_file=package_name+'/integration.yaml', schema_files=['optimizely_dev_tools/integration_schema.yaml'])
  schema_validator.validate(raise_exception=True)

def validate_config_yaml(package_name):
  """Check that an integration's config.yaml file has a valid schema

  Raises:
    Exception if the config.yaml file has an improper schema
  """
  schema_validator = Core(source_file=package_name+'/config.yaml', schema_files=['optimizely_dev_tools/config_schema.yaml'])
  schema_validator.validate(raise_exception=True)

def get_pylint_errors(pylint_output):
  """The Pylint py_run function yields a list of warnings and errors. This function filters out warnings and only yields errors

  Returns:
    List of errors
  """
  error_list = []
  for message in pylint_output:
    if 'error' in message:
      error_list.append(message)
  return error_list

def validate_functions_py(package_name):
  """Check that an integration's functions.py file is syntactically correct and that it contains necessary functions
  
  Raises:
    Exception if functions.py is an invalid Python program
  """
  pylint_stdout, pylint_stderr = lint.py_run(package_name+'/functions.py', True)
  errors = get_pylint_errors(pylint_stdout.readlines())
  if errors:
    raise Exception("Syntax errors in functions.py: " + str(errors))
  functions = importlib.import_module(package_name+'.functions')
  if not hasattr(functions, 'get_dynamic_audience_conditions'):
    raise Exception("functions.py does not contain get_dynamic_audience_conditions function")

def validate_functions_js(package_name):
  """Check that an integration's functions.js file is syntactically correct

  Raises:
    Exception if functions.js is an invalid JS program
  """
  try:
    subprocess.check_call(['node','validate_functions.js', package_name+'/functions.js'])
  except Exception as e:
    raise Exception("functions.js validation error")

def start_package(packagename, integration):
  localserver.main(packagename, integration)

def main(args):
  init(autoreset=True)
  package_name = args.package_name

  try:
    validate_package_name(package_name)
    print_successful_validation_message('correctness of format of package name')
  except Exception as e:
    print_fail_validation_message(e)

  # existence checks
  try:
    validate_package_root_exists(package_name)
    print_successful_validation_message('that package root folder exists')
  except Exception as e:
    print_fail_validation_message(e)
  try:
    validate_necessary_files_exist(package_name)
    print_successful_validation_message('that necessary files exist')
  except Exception as e:
    print_fail_validation_message(e)

  # code structure checks
  try:
    validate_integration_yaml(package_name)
    print_successful_validation_message('integration.yaml correctness')
  except Exception as e:
    print_fail_validation_message(e)
  try:
    validate_config_yaml(package_name)
    print_successful_validation_message('config.yaml correctness')
  except Exception as e:
    print_fail_validation_message(e)
  try:
    validate_functions_py(package_name)
    print_successful_validation_message('functions.py correctness')
  except Exception as e:
    print_fail_validation_message(e)
  try:
    validate_functions_js(package_name)
    print_successful_validation_message('functions.js correctness')
  except Exception as e:
    print_fail_validation_message(e)

  # local app setup
  #start_package(package_name, integration)
