import http
import logging
import socket
import warnings
import requests
from requests.packages.urllib3.exceptions import ConnectionError
from requests.packages.urllib3.exceptions import TimeoutError
from requests.packages.urllib3.exceptions import SSLError as _SSLError
from requests.packages.urllib3.exceptions import HTTPError as _HTTPError
from requests.exceptions import ConnectionError, Timeout, SSLError


# This is well explained by Ben Hoey at:
# https://bhoey.com/blog/better-debug-logging-for-the-python-requests-library/
# This is his excellent approach to requests debug logging.  Thank you Ben.
# It is especially valuable when attempting to deal with a 
# poorly documented or otherwise opaque API.
# I have it here just as a reminder to me... 
 
# Set up logging to a file
logging.basicConfig(filename="devClient.log", level=logging.DEBUG)
# Using __name__ as the name of the logger makes sure that the 
# logger hierarchy reflects the python module hierarchy
logger = logging.getLogger(__name__)
 
# Turn on global debugging for the HTTPConnection class
http.client.HTTPConnection.debuglevel = 1


# Redirect print to the debug logger
def debugLog(*args):
    logger.debug(" ".join(args))


http.client.print = debugLog
 
# Assumes you have something listening for tests
url = "http://localhost:8080/test"
 
logger.info("START HTTP GET Test")

try:

    # Test HTTP GET
    resp = requests.get(url, timeout=5)

    if resp.status_code == 408:
        logger.exception(f"Request Timeout: {str(resp.status_code)}")   #  [RFC7231, Section 6.5.7]
except OSError as msg:
    logger.exception(f"OSError: Something bad happened.  Hostname correct?  Network OK? {msg}")

except socket.error as sockerr:
    logger.exception(f"Something bad happened.  Hostname correct?  Network OK? {sockerr}")

except ConnectionError as e:
    logger.exception(f"{e}")

except MaxRetryError as e:
    logger.exception(f"{e}")

except ConnectionError as e:
    logger.exception(f"{e}")

except (_SSLError, _HTTPError) as e:
    if isinstance(e, _SSLError):
        logger.exception(f"{e}")
    elif isinstance(e, TimeoutError):
        logger.exception(f"{e}")
    else:
        logger.exception(f"Request timed out. Not _SSLError or TimeoutError: {e}")
        
except Exception as e:
    logger.exception(f"The request failed: {e}")

logger.info("START HTTP POST Test")
# Test HTTP POST
# ToDo: Wrap the usage below in a try/except
"""
# something like this:
try:
    request_code()
except Exception:
    logger.exception("The request failed.")
"""
resp = requests.post(url, data='POST Testing data')
