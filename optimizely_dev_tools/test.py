import os
import pkg_resources
import subprocess

from colorama import Fore, Style, init

def main(args):
  init(autoreset=True)
  package_name = args.package_name

  print(Fore.BLUE + 'Running Python tests...' + Style.RESET_ALL)

  subprocess.call(['python', '-m', 'unittest', 'discover', '-p', '*_test.py'])

  print(Fore.BLUE + 'Running JavaScript tests...' + Style.RESET_ALL)

  package_dir = os.path.join(os.getcwd(), package_name)

  resource_package = __name__
  resource_path = os.path.join('scripts', 'run_tests.sh')
  run_tests_path = pkg_resources.resource_filename(resource_package, resource_path)
  dir_path = os.path.dirname(run_tests_path)

  os.chdir(package_dir)
  subprocess.call(['sh', run_tests_path, package_dir])
