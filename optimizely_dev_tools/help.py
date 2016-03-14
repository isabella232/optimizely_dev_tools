import webbrowser
from colorama import Fore, Back, Style, init

def main(args):
  website = 'http://developers.optimizely.com'
  print('Opening ' + Fore.CYAN + website + Style.RESET_ALL + ' in your favorite webbrowser.')
  webbrowser.open_new(website)
  
