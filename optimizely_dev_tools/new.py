import os
from colorama import Fore, Back, Style, init
import re
from optimizely_dev_tools import packagefiles
import pkg_resources
import shutil

def check_packagename(packagename):
  m = re.match('[a-z0-9_]{3,30}', packagename)
  return (m != None and m.group(0) == packagename)

def copy_logo(packagename):
  buffer_size = 16000
  fsrc = pkg_resources.resource_stream('optimizely_dev_tools', 'assets/logo.png')
  with open(packagename + '/assets/logo.png', 'w') as fdest:
      shutil.copyfileobj(fsrc, fdest, buffer_size)  


def create_package(packagename, example):
  os.makedirs(packagename)
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/')

  os.makedirs(packagename + '/assets')
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/assets/')

  copy_logo(packagename)
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/assets/logo.png')

  packagefiles.create_init_file(packagename, example)
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/__init__.py')

  packagefiles.create_config_file(packagename, example)
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/config.yaml')  

  packagefiles.create_example_response_file(packagename, example)
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/example.json')

  packagefiles.create_integration_file(packagename, example)
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/integration.json')

  packagefiles.create_functions_js_file(packagename, example)
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/functions.js')

  packagefiles.create_functions_py_file(packagename, example)
  print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Created ' + packagename + '/functions.py')

def main(args):
  init(autoreset=True)
  packagename = args.packagename
  example = args.example
  
  if not check_packagename(packagename):
    print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] Packagename must match [a-z0-9_]{4,30}')
  elif not os.path.exists(packagename):
    create_package(packagename, example)
  else:
    print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] Folder already exists')




