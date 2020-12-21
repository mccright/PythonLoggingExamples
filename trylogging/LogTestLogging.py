import logging
from os import path
import datetime
from time import gmtime
# Need this to configure the handlers
from logging.config import dictConfig

def init_logging():
    logFilePath = path.basename(__file__) + '.log'
    logger = logging.getLogger(logFilePath)
    formatter = logging.Formatter(
        '%(asctime)s %(name)s:%(lineno)d [%(thread)d] %(levelname)s: %(message)s')
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logging.Formatter.converter = gmtime

    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=logFilePath, when='midnight', backupCount=30)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logging.Formatter.converter = gmtime

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


if __name__ == '__main__':
    logger = init_logging()
    # Begin some logging tests
    # First log an Exception
    logger.info("Started");
    try:
        x = 612
        y = 0
        z = x / y
    except Exception as ex:
        logger.error("Divide operation failed.")
        logger.debug(
            "Encountered {0} when trying to perform calculation.".format(ex))

    logger.info("Ended");

    # Now just emit some custom messages.
    # logger.setLevel(logging.DEBUG)
    logger.debug('debug testing message')
    logger.info('info testing message')
    logger.warning('warning testing message')
    logger.error('error testing message')
    logger.critical('critical testing message')
