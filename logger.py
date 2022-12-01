from colorama import Fore, Style
import datetime

def info(text):
    print(Fore.WHITE + '[' + Fore.LIGHTWHITE_EX + '+' + Fore.WHITE + '] ' + text)

def input(text):
    print(Fore.WHITE + '[' + Fore.LIGHTWHITE_EX + '?' + Fore.WHITE + '] ' + text)

def accent(text):
    print(Fore.WHITE + '[' + Fore.LIGHTWHITE_EX + '!' + Fore.WHITE + '] ' + text)

def error(text):
    print(Fore.WHITE + '[' + Fore.RED + 'E' + Fore.WHITE + '] ' + text)

def text(text):
    time = datetime.datetime.now()
    print(Fore.BLUE + str(time.hour) + ':' + str(time.minute) + ':' + str(time.second) + str(time.microsecond) + ' ' + Fore.WHITE + text + Style.RESET_ALL)

def logo(text):
    symbols = ['╗', '║', '╝', '╔', '═', '╚']
    string = ''
    for i in text:
        if i in symbols:
            string = string + Fore.BLUE + i + Style.RESET_ALL
        else:
            string = string + Fore.LIGHTWHITE_EX + i + Style.RESET_ALL

    print(string)