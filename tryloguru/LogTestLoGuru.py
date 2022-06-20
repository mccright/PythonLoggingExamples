#!/usr/bin/env python3
import errno
from loguru import logger
import sys
import datetime
import os

# This is just a short experiment and reminder for later.
# It is not meant to be a ready-to-use component.
# See https://github.com/Delgan/loguru/ for many more use cases.
# Also loguru recipes: 
# https://loguru.readthedocs.io/en/stable/resources/recipes.html
# and https://www.programcreek.com/python/example/118602/loguru.logger.configure
# Config Formatting guidance:
# https://github.com/Delgan/loguru/blob/fe2f34d3e6c23afcd98aedaede880ea27d0f3298/loguru/_logger.py

# Log file options
# , rotation="500 MB"
#   Examples: "100 MB", "0.5 GB"
# , rotation="00:00"
# , rotation="1 week"
#   Examples: "1 month 2 weeks", "4 days", "10h", "monthly", "18:00", "sunday", "w0", "friday at 12:00"
# , retention="10 days"
#   Example max age usage: "1 week", "3 days", "2 months"
# , compression="zip"
#   Use: "gz", "bz2", "xz", "lzma", "tar", "tar.gz", "tar.bz2", "tar.xz", or "zip".
#


def init_logging():
    # UTC so global logs sync.
    dt = datetime.datetime.utcnow()
    scriptName = os.path.basename(__file__)
    print(scriptName)
    # If needed, put the log file in a log directory using: 
    # logdir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/log/' 
    myLog = str(scriptName) + "-{time}.log"
    config = {
        "handlers": [
            {"sink": sys.stdout, "format": "{time:!UTC} - {message}", \
                "colorize": True},
            {"sink": str(myLog), "format": \
                "{time:YYYY-MM-dd HH:mm:ss:SSS Z!UTC} \
                {level} {file}:{line} - {message}", "serialize": False},
        ],
        "extra": {"user": "someone"}
    }

    logger.level('TRACE', color='<dim>')
    logger.level('DEBUG', color='<dim><cyan>')
    logger.level('INFO', color='')
    logger.level('SUCCESS', color='<dim><green>')
    logger.level('WARNING', color='<yellow>')
    logger.level('ERROR', color='<bold><red>')
    logger.level('CRITICAL', color='<bold><red><WHITE>')

    try:
        logger.configure(**config)
    except IOError as e:
        print("IOError: " + e.reason.decode("utf8", 'ignore'))
        exitCode = errno.ENOENT
        exit(exitCode)
    except Exception as e:
        print("Exception Cause: " + e.__cause__)
        print("Exception Message: " + e.__str__())
        exitCode = errno.ENOENT
        exit(exitCode)


if __name__ == '__main__':
    init_logging()
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

    logger.info("Ended")

    logger.debug('debug testing message')
    logger.info('info testing message')
    logger.success('success testing message')
    logger.warning('warning testing message')
    logger.error('error testing message')
    logger.critical('critical testing message')
