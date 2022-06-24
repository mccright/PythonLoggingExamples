import http
import logging
import requests

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

# Test HTTP GET
resp = requests.get(url)
 
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
