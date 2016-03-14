import os.path
import yaml
from colorama import Fore, Back, Style, init
import re

def check_packagename(packagename):
  m = re.match('[a-z0-9_]{3,30}', packagename)
  valid = (m != None and m.group(0) == packagename)
  if valid:
    print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Package exists')
    return ['packagename']
  else:
    print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] Packagename must match [a-z0-9_]{4,30}') 
    sys.exit(0)

def check_package_root(packagename):
  if os.path.exists(packagename):
    print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Package directory exists')
  else:
    print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] Package directory doesn\'t exist')  
    sys.exit(0)

def check_integration_yaml(packagename):
  filename = packagename + '/integration.yaml'
  if os.path.isfile(packagename + '/integration.yaml'):
    print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] ' + filename + ' exists')
    f = open(filename)
    dataMap = yaml.safe_load(f)
    f.close()
    print dataMap
  else:
    print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] ' + filename + ' does not exist.')  
    sys.exit(0)


def main(args):
  init(autoreset=True)
  packagename = args.packagename
  
  check_packagename(packagename)
  check_package_root(packagename)
  check_integration_yaml(packagename)


  