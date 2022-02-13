from colorama import Fore, Style
from time import sleep
import time

class Logger:

    def __init__(self):
        pass

    def alert(self, message, err = 'none'):
        alert = 'err:7648'
        if err == 'none':
            alert = time.strftime('[%X %x] ') + message
        if err == 'err':
            alert = Fore.RED + time.strftime('[%X %x] ') + message + Style.RESET_ALL
        if err == 'suc':
            alert = Fore.GREEN + time.strftime('[%X %x] ') + message + Style.RESET_ALL
        if err == 'war':
            alert = Fore.YELLOW + time.strftime('[%X %x] ') + message + Style.RESET_ALL
        print(alert)