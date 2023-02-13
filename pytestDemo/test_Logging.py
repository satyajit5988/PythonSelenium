import logging


def test_loggingDemo():
    # Creating a logging object
    logger = logging.getLogger(__name__)

    # Passing info about file location
    filehandler = logging.FileHandler('logfile.log')

    # Setting format for logging
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

    # Linking formatting info to filehandler object
    filehandler.setFormatter(formatter)

    # passing filehandler object to addHandler
    logger.addHandler(filehandler)  # Filehandler Object

    # Setting log level
    logger.setLevel(logging.ERROR)

    # Order of logging is as below, SetLevel accordingly to see the subsequent logs
    logger.debug("Debug")
    logger.info("Info")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical")

