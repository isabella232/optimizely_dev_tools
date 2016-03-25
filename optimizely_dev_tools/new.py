import inspect
import os
import pkg_resources
import re
import shutil
import sys

from collections import OrderedDict
from colorama import Fore, Back, Style, init

from optimizely_dev_tools import packagefiles

def check_package_name(package_name):
  """Check that package name matches convention

  Args:
    package_name: The package name to validate

  Returns:
    A boolean determining whether the package name is valid or not
  """
  m = re.match('[a-z0-9_]{3,30}', package_name)
  return (m != None and m.group(0) == package_name)

def copy_logo(package_name):
  """Copies logo from assets folder to the new package folder

  Args:
    package_name: The name of the package and root folder to copy the logo to
  """
  buffer_size = 16000
  fsrc = pkg_resources.resource_stream('optimizely_dev_tools', 'assets/logo.png')
  with open(package_name + '/assets/logo.png', 'w') as fdest:
      shutil.copyfileobj(fsrc, fdest, buffer_size)  

def print_create_message(package_name, file_to_make):
  """Prints success message for the creation of a file

  Args:
    package_name: The name of the package to print
    file_to_make: The file that was created
  """
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + package_name + file_to_make)

def create_package(package_name, default_config):
  """Create the necessary integration package files

  Args:
    package_name: The name of the package/folder in which necessary files will be generated
    default_config: Whether to auto-fill yaml fields, or to just provide instructions on how to fill the fields
  """
  os.makedirs(package_name)
  print_create_message(package_name, '/')

  os.makedirs(package_name + '/assets')
  print_create_message(package_name, '/assets')

  copy_logo(package_name)
  print_create_message(package_name, '/assets/logo.png')

  packagefiles.create_init_file(package_name)
  print_create_message(package_name, '/__init__.py')

  packagefiles.create_config_file(package_name, default_config)
  print_create_message(package_name, '/config.yaml')

  packagefiles.create_example_response_file(package_name, default_config)
  print_create_message(package_name, '/example.json')

  packagefiles.create_integration_file(package_name, default_config)
  print_create_message(package_name, '/integration.yaml')

  packagefiles.create_functions_js_file(package_name, default_config)
  print_create_message(package_name, '/functions.js')

  packagefiles.create_functions_py_file(package_name, default_config)
  print_create_message(package_name, '/functions.py')

  packagefiles.create_functions_py_test_file(package_name, default_config)
  print_create_message(package_name, '/functions_test.py')

  packagefiles.create_functions_js_test_file(package_name, default_config)
  print_create_message(package_name, '/functions_test.unittests.js')

def main(args):
  init(autoreset=True)
  package_name = args.package_name
  # currently only Audiences supported
  config_type = args.config_type
  default_config = args.default_config

  if not check_package_name(package_name):
    print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] Packagename must match [a-z0-9_]{4,30}')
  elif not os.path.exists(package_name):
    create_package(package_name, default_config)
  else:
    print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] Folder already exists')
