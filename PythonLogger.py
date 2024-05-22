# This is a simple Python script.
# Press Shift+F10 to execute it
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime
from pathlib import Path
import os

__autor__ = "Srdjan Dragojevic"
__github__ = ""
__email__ = ""

DEBUG = "DEBUG"
INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"
AllLogLevels: list[str] = [DEBUG, INFO, WARNING, ERROR]


class Logger:

    def __init__(self, log_file_name: str = None,
                 log_file_path: Path = None,
                 log_levels: list[str] = None,
                 log_text_line: str = "...") -> None:
        """
        Initialize the attributes of the newly created Logger object

        :param log_file_name: Name that you want log file to have. Default is log.txt
        :param log_file_path: Path where to store the log file. Default is the path where PythonLogger is
        :param log_levels: What levels you want for logger to write in log file. Default are all levels
        "DEBUG", "INFO", "WARNING", "ERROR"
        :param log_text_line: Text that you want to be logged. Default is ...
        """

        if log_file_name is None:
            self.file_name: str = "log.txt"
        else:
            self.file_name: str = log_file_name
        print(f"Log file name: {self.file_name}")

        if log_file_path is None:
            self.file_path = Path.cwd()
        else:
            self.file_path: Path = log_file_path
        print(f"Log file path: {self.file_path}")

        if log_levels is None:
            self.levels: list[str] = AllLogLevels
        else:
            for idx, lvl in enumerate(log_levels):
                if lvl not in AllLogLevels:
                    log_levels.pop(idx)
            self.levels: list[str] = log_levels

        current_time = datetime.now()
        d_m_y = current_time.strftime("%d-%B-%Y")
        h_m_s_ms = current_time.strftime("%H:%M:%S.%f")
        text_line: str = f'{d_m_y}|{h_m_s_ms}|{INFO}|{log_text_line}'
        print(text_line)

        self.all_text_lines: str = f"{text_line}"

        abs_path = os.path.join(self.file_path, self.file_name)
        # delete old log if there was one
        if os.path.exists(abs_path):
            os.remove(abs_path)

        # create new log file
        with open(abs_path, "w") as file:
            file.write(self.all_text_lines)

    def log_line(self, log_level: str = INFO, log_text_line: str = "...") -> None:
        """

        :param log_level: Can be: "DEBUG", "INFO", "WARNING", "ERROR"
        :param log_text_line: Default is ...
        :return:
        """

        current_time = datetime.now()
        d_m_y = current_time.strftime("%d-%B-%Y")
        h_m_s_ms = current_time.strftime("%H:%M:%S.%f")
        text_line: str = f'{d_m_y}|{h_m_s_ms}|{log_level}|{log_text_line}'
        print(text_line)

        # log only those text lines that are in the list of log levels
        if log_level in self.levels:
            self.all_text_lines: str = f"{self.all_text_lines}{text_line}"

    def set_levels(self, log_levels: list[str] = None) -> None:
        """
        Set the levels that you want to be logged

        :param log_levels: List of levels to be logged
        :return:
        """

        # check if log_levels list is empty
        if log_levels is None:
            self.levels: list[str] = AllLogLevels
        elif len(log_levels) == 0:
            pass  # do nothing
        else:
            # check if not existing log level is added
            for idx, lvl in enumerate(log_levels):
                if lvl not in AllLogLevels:
                    log_levels.pop(idx)

            if len(log_levels) == 0:
                self.levels: list[str] = AllLogLevels
            else:
                self.levels: list[str] = log_levels


def main():
    print("Logger module started")
    logger = Logger()
    j = 0
    for i in range(1000000):
        if i % 100000 == 0:
            logger.log_line(f"this is {j}. line")
            j += 1


# this check ensures that this code will run only if this module is run directly
# module is a single file that contains python code (import module)
# package is a collection of modules in a directory; every package contains __init__.py file (import module2)
# library is a collection of packages
if __name__ == '__main__':
    main()
