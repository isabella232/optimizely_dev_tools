import pkg_resources
import os

from distutils.dir_util import copy_tree
from shutil import copy, copyfile

resource_package = __name__

def create_init_file(package_name):
  file_name = '__init__.py'
  f = open(package_name + '/' + file_name, 'w')
  f.write('# This file indicates this is a Python package. No modifications needed.')

def create_config_file(package_name, default_config):
  file_name = 'config.yaml'
  file_content = ''
  if default_config:
    resource_path = os.path.join('template_files', 'config_yaml_default_template')
    file_content = pkg_resources.resource_string(resource_package, resource_path)
    file_content = file_content.format(package_name=package_name)
  else:
    resource_path = os.path.join('template_files', 'config_yaml_unconfigured_template')
    file_content = pkg_resources.resource_string(resource_package, resource_path)
  with open(os.path.join(package_name, file_name), 'w') as f:
    f.write(file_content)

def create_integration_file(package_name, default_config):
  file_name = 'integration.yaml'
  file_content = ''
  if default_config:
    resource_path = os.path.join('template_files', 'integration_yaml_default_template')
    file_content = pkg_resources.resource_string(resource_package, resource_path)
    file_content = file_content.format(package_name=package_name)
  else:
    resource_path = os.path.join('template_files', 'integration_yaml_unconfigured_template')
    file_content = pkg_resources.resource_string(resource_package, resource_path)
    file_content = file_content.format(package_name=package_name)
  with open(os.path.join(package_name, file_name), 'w') as f:
    f.write(file_content)

def create_example_response_file(package_name, default_config):
  file_name = 'example.json'
  file_content = '// Provide an example response from your streaming server (if you use dynamic audiences in your integration)'
  if default_config:
    resource_path = os.path.join('template_files', 'example.json')
    file_path = pkg_resources.resource_filename(resource_package, resource_path)
    copy(file_path, package_name)
  else:
    f = open(os.path.join(package_name, file_name), 'w')
    f.write(file_content)

def create_functions_js_file(package_name, default_config):
  file_name = 'functions.js'
  file_path = package_name + '/' + file_name
  if default_config:
    resource_path = os.path.join('template_files', 'functions_default.js')
    template_path = pkg_resources.resource_filename(resource_package, resource_path)
    copyfile(template_path, file_path)
  else:
    resource_path = os.path.join('template_files', 'functions_unconfigured.js')
    template_path = pkg_resources.resource_filename(resource_package, resource_path)
    copyfile(template_path, file_path)

def create_functions_js_test_file(package_name, default_config):
  file_name = 'functions_test.unittests.js'
  file_path = package_name + '/' + file_name

  resource_path = os.path.join('template_files', 'functions_test_default.unittests.js')
  template_path = pkg_resources.resource_filename(resource_package, resource_path)
  copyfile(template_path, file_path)

def create_functions_py_file(package_name, default_config):
  file_name = 'functions.py'
  file_path = os.path.join(package_name, file_name)
  if default_config:
    resource_path = os.path.join('template_files', 'functions_default.py')
    template_path = pkg_resources.resource_filename(resource_package, resource_path)
    copyfile(template_path, file_path)
  else:
    resource_path = os.path.join('template_files', 'functions_unconfigured.py')
    template_path = pkg_resources.resource_filename(resource_package, resource_path)
    copyfile(template_path, file_path)

def create_functions_py_test_file(package_name, default_config):
  file_name = 'functions_test.py'
  file_path = package_name + '/' + file_name

  resource_path = os.path.join('template_files', 'functions_test_default.py')
  template_path = pkg_resources.resource_filename(resource_package, resource_path)
  copyfile(template_path, file_path)

def create_package_json():
  file_name = 'package.json'
  package_json_path = pkg_resources.resource_filename(resource_package, file_name)
  copyfile(package_json_path, './'+file_name)

def create_test_helpers():
  folder_name = 'testing'
  testing_folder_path = pkg_resources.resource_filename(resource_package, folder_name)
  copy_tree(testing_folder_path, './'+folder_name)

def create_grunt_file():
  file_name = 'Gruntfile.js'
  grunt_file_path = pkg_resources.resource_filename(resource_package, file_name)
  copyfile(grunt_file_path, './'+file_name)

def create_nvmrc():
  file_name = '.nvmrc'
  nvmrc_path = pkg_resources.resource_filename(resource_package, file_name)
  copyfile(nvmrc_path, './'+file_name)

def create_scripts_dir():
  folder_name = 'scripts'
  scripts_folder_path = pkg_resources.resource_filename(resource_package, folder_name)
  copy_tree(scripts_folder_path, './'+folder_name)
  os.chmod('./scripts/create_under_test_js_files.sh', 0755)
