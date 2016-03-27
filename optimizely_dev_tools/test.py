import subprocess

from colorama import Fore, Style, init

def main(args):
  init(autoreset=True)
  package_name = args.package_name

  print(Fore.BLUE + 'Running Python tests...' + Style.RESET_ALL)

  subprocess.call(['python', '-m', 'unittest', 'discover', '-p', '*_test.py'])

  print(Fore.BLUE + 'Running JavaScript tests...' + Style.RESET_ALL)

  subprocess.call(['sh', '../scripts/run_tests.sh'])
