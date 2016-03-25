from shutil import copy, copyfile

def create_init_file(package_name):
  file_name = '__init__.py'
  f = open(package_name + '/' + file_name, 'w')
  f.write('# This file indicates this is a Python package. No modifications needed.')

def create_config_file(package_name, default_config):
  filename = 'config.yaml'
  file_content = ''
  if default_config:
    with open('template_files/config_yaml_default_template', 'r') as f:
      file_content = f.read()
      file_content = file_content.format(package_name=package_name)
  else:
    with open('template_files/config_yaml_unconfigured_template', 'r') as f:
      file_content = f.read()
  with open(package_name + '/' + filename, 'w') as f:
    f.write(file_content)

def create_integration_file(package_name, default_config):
  file_name = 'integration.yaml'
  file_content = ''
  if default_config:
    with open('template_files/integration_yaml_default_template', 'r') as f:
      file_content = f.read()
      file_content = file_content.format(package_name=package_name)
  else:
    with open('template_files/integration_yaml_unconfigured_template', 'r') as f:
      file_content = f.read()
      file_content = file_content.format(package_name=package_name)
  with open(package_name + '/' + file_name, 'w') as f:
    f.write(file_content)

def create_example_response_file(package_name, default_config):
  file_name = 'example.json'
  file_content = '// Provide an example response from your streaming server (if you use dynamic audiences in your integration)'
  if default_config:
    copy('template_files/'+file_name, package_name)
  else:
    f = open(package_name + '/' + file_name, 'w')
    f.write(file_content)

def create_functions_js_file(package_name, default_config):
  file_name = 'functions.js'
  file_path = package_name + '/' + file_name
  if default_config:
    copyfile('template_files/functions_default.js', file_path)
  else:
    copyfile('template_files/functions_unconfigured.js', file_path)

def create_functions_js_test_file(package_name, default_config):
  # TODO: implement
  file_name = '/functions_test.unittests.js'
  file_path = package_name + '/' + file_name
  f = open(file_path, 'w')
  f.close()

def create_functions_py_file(package_name, default_config):
  file_name = 'functions.py'
  file_path = package_name + '/' + file_name
  if default_config:
    copyfile('template_files/functions_default.py', file_path)
  else:
    copyfile('template_files/functions_unconfigured.py', file_path)

def create_functions_py_test_file(package_name, defaut_config):
  # TODO: implement
  file_name = 'functions_test.py'
  file_path = package_name + '/' + file_name
  f = open(file_path, 'w')
  f.close()
