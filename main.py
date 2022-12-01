import os
from time import sleep

import colorama
from colorama import Fore
from tqdm import trange

import audioplayer
import logger
import recorder

if __name__ == '__main__':
    colorama.init()
    logger.logo(f"""
         ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
         ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
         ██║███████║██████╔╝██║   ██║██║███████╗
    ██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
    ╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
     ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
     """)
    logger.info(f"Jarvis made by: {Fore.BLUE}sdev")
    logger.info(f"Telegram: {Fore.BLUE}@olex2andr\n")
    logger.info("Jarvis Voice listener can work only with Russian Language at this moment.\n")

    for i in trange(10, desc=Fore.WHITE + '[' + Fore.LIGHTWHITE_EX + '!' + Fore.WHITE + '] Starting Voice Listener' + Fore.WHITE, bar_format='{desc} {percentage}%', leave=False):
        sleep(.1)

    logger.accent("Voice Listener started successfully. Type 'help' to see Jarvis commands.")

    while True:
        recorded = recorder.record_volume().lower()
        if recorded == 'открой google':
            audioplayer.play('Открываю')
            os.startfile('D:/Chrome/Application/chrome.exe')
        else:
            symbols = {
                'х': '*',
                'x ': '* ', # python issue
                ' x': ' *', # python issue
                ',': '.'
            }

            for symbol, replaced in symbols.items():
                recorded = recorded.replace(symbol, replaced)

            try:
                math = round(eval(recorded), 4)
                logger.info(f"Результат ({recorded}): {math}")
                audioplayer.play(math)
            except:
                pass