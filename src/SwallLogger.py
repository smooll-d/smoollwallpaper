import logging

from colorama import init, Fore, Style, deinit

class SwallLogger:
    def __init__(self, name: str):
        init()

        self.name = name
        self.logger = logging.getLogger(self.name)
        
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            self.logger.propagate = False

            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                fmt="(%(asctime)s) | [%(levelname)s] - %(name)s: %(message)s",
                datefmt="%H:%M:%S"
            )

            ch.setFormatter(formatter)

            self.logger.addHandler(ch)

        deinit()

    def debug(self, message: str):
        self.logger.debug(Fore.LIGHTBLUE_EX + message + Style.RESET_ALL)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(Fore.YELLOW + message + Style.RESET_ALL)

    def error(self, message: str):
        self.logger.error(Fore.RED + message + Style.RESET_ALL)

    def critical(self, message: str):
        self.logger.critical(Fore.MAGENTA + message + Style.RESET_ALL)