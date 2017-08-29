'''
File: watchdog.py
Description: Provides logging for the bolt server
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 28/08/2017
'''
import datetime

class Watchdog(object):
    """Watchdog mechanism for Bolt

    Provides logging functionality for the Bolt CI to log the various execution
    steps
    """

    #Log level
    LOG_ERROR = 1
    LOG_WARNING = 2
    LOG_INFO = 3
    LOG_DEBUG = 4

    def __init__(self, log_file, logging_level=3):
        """Watchdog constructor

        Initializes the watchdog with the provided parameters

        Args:
            log_file(str): The path to the log file
        Kwargs:
            logging_level(int): The desired level of logging that is required(Default: INFO)
        """

        self.log_file = log_file
        self.logging_level = logging_level

        self._open_log_file(self.log_file)

        self.log_format = "{}:{}[{}]:{}\n" #TIME:PROJECT[LEVEL]:MESSAGE

    def error(self, message):
        """Log error level messages into the file

        Args:
            message(str): The error message to be logged
        """

        if self.logging_level < self.LOG_ERROR:
            return 0
        self._log('ERROR', message)

    def warn(self, message):
        """Log warning level messages into the file

        Args:
            message(str): The warning message to be logged
        """

        if self.logging_level < self.LOG_WARNING:
            return 0
        self._log('WARN', message)

    def info(self, message):
        """Log info level messages into the file

        Args:
            message(str): The info message to be logged
        """

        if self.logging_level < self.LOG_INFO:
            return 0
        self._log('INFO', message)

    def debug(self, message):
        """Log debug level messages into the file

        Args:
            message(str): The debug message to be logged
        """

        if self.logging_level < self.LOG_DEBUG:
            return 0
        self._log('DEBUG', message)

    def close(self):
        """Close the logging mechanism
        """

        self.logger.close()

    def _log(self, message_level, message):
        """Write the log message to the file

        Args:
            message_level(str): The level of the message to log
            message(str): The content of the message
        """

        log_message = self.log_format.format(str(datetime.datetime.now()), __file__, message_level, message)
        self.logger.write(log_message)

    def _open_log_file(self, log_file):
        """Open the provided log file for writing

        Args:
            log_file(str): The path to the log file to be opened

        Raises:
            IOError
        """

        try:
            self.logger = open(self.log_file, 'a+')
        except Exception:
            print "Unable to open the log file. Logger Init Failed"
            raise IOError("Unable to open log file. Logger failed")
