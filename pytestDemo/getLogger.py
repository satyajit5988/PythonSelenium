import inspect
import logging


class BaseClass:

    def getLogger(self):

        TCName = inspect.stack()[1][3]

        # Creating a logging object
        logger = logging.getLogger(TCName)

        # Passing info about file location
        filehandler = logging.FileHandler('logfile.log')

        # Setting format for logging
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

        # Linking formatting info to filehandler object
        filehandler.setFormatter(formatter)

        # passing filehandler object to addHandler
        logger.addHandler(filehandler)  # Filehandler Object

        # Setting log level
        logger.setLevel(logging.DEBUG)
        return logger

