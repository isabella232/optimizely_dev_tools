import os.path
import yaml
from colorama import Fore, Back, Style, init
import re
import sys
from pprint import pprint
import localserver



def check_packagename(packagename):
  m = re.match('[a-z0-9_]{3,30}', packagename)
  valid = (m != None and m.group(0) == packagename)
  if valid:
    print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] Package exists')
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
    dataMap = {}
    try:
      f = open(filename)
      dataMap = yaml.safe_load(f)
      f.close()
    except yaml.scanner.ScannerError as e:
      print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] Invalid yaml format in ' + filename)  
      print e
      sys.exit(0)

    print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] ' + filename + ' is in a valid yaml format')

    # pprint(dataMap[packagename])
    return dataMap[packagename]
  else:
    print('[' + Fore.RED + 'ERROR' + Style.RESET_ALL + '] ' + filename + ' does not exist.')  
    sys.exit(0)

def start_package(packagename, integration):
  localserver.main(packagename, integration)


def main(args):
  init(autoreset=True)
  packagename = args.packagename
  
  check_packagename(packagename)
  check_package_root(packagename)
  integration = check_integration_yaml(packagename)

  start_package(packagename, integration)


  