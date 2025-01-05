## My Python Logging Reminders  
[![](https://tokei.rs/b1/github/mccright/PythonLoggingExamples)](https://github.com/mccright/PythonLoggingExamples)  
logpai/logparser

These examples are just reminders/demonstrations to help me get started on any given python script.  

> For a more detailed description of Python logging refer to [the official manual](https://docs.python.org/3.10/library/logging.html#module-logging).  There is a useful diagram outlining the flow of log event information in loggers and handlers at: [https://docs.python.org/3.10/howto/logging.html#logging-flow](https://docs.python.org/3.10/howto/logging.html#logging-flow).  And don't ignore the logging cookbook if you have the urge to do your own thing [https://docs.python.org/3/howto/logging-cookbook.html](https://docs.python.org/3/howto/logging-cookbook.html)  
* Or a quick overview: "Logging in Python: A Developer’s Guide." By Bala Priya C., 2022-07-19 [https://blog.sentry.io/2022/07/19/logging-in-python-a-developers-guide](https://blog.sentry.io/2022/07/19/logging-in-python-a-developers-guide)  
* Or for troubleshooting see: [https://github.com/brandon-rhodes/logging_tree](https://github.com/brandon-rhodes/logging_tree)  
* or a short video lesson at: "[Python Logging: How to Write Logs Like a Pro!](https://www.youtube.com/watch?v=pxuXaaT1u3k)" with its supporting code at: [https://github.com/ArjanCodes/2023-logging](https://github.com/ArjanCodes/2023-logging)  

### Approaches  
* The old *print* way:  
```Python
def log(loglevel, component, message):
    print(f"{datetime.now(timezone('UCT'))} \
[{loglevel}] {component}: {message}", file=sys.stderr)
```
Then log something with:  
```Python
log("INFO", __file__, f"Using important_var: {important_var}")
```

* The standard python logging module: [`trylogging/LogTestLogging.py`](https://github.com/mccright/PythonLoggingExamples/tree/main/trylogging)  
    *Usage:*  
    `from LogTestLogging import init_logging`  
    `logger = init_logging()`  
    `logger.info('info testing message')`  
* The loguru module -- because it was so easy to configure: [`tryloguru/LogTestLoGuru.py`](https://github.com/mccright/PythonLoggingExamples/tree/main/tryloguru)  
    *Usage:*  
    `from LogTestLoGuru import init_logging`  
    `logger = init_logging()`  
    `logger.info('info testing message')`  
  * See "[A Complete Guide to Logging in Python with Loguru](https://betterstack.com/community/guides/logging/loguru/)" for an excellent overview and a detailed example describing how to integrate it into a typical web application.  
  * or see "[An Intro to Logging with Loguru](https://www.pythonpapers.com/p/an-intro-to-logging-with-loguru)" by Mike Driscoll for a useful quick summary with code examples.  
* [requestsDebugging](https://github.com/mccright/PythonLoggingExamples/blob/main/requestsDebugging/devClient.py): A useful approach to *requests* debug logging especially valuable when attempting to deal with a poorly documented or otherwise opaque API.  This is well explained by Ben Hoey at [bhoey.com](https://bhoey.com/blog/better-debug-logging-for-the-python-requests-library/).  

* The next...  

### Install  

None.  These are not modules, just little code reminders.  
That said,  `tryloguru/LogTestLoGuru.py` requires `pip3 install loguru --user`.  

### What Should You Log?   
See some ideas at: [https://github.com/mccright/rand-notes/blob/master/Application-Logging.md](https://github.com/mccright/rand-notes/blob/master/Application-Logging.md)  

### Explore later  
* Explore ```SysLogHandler```: https://docs.python.org/3/library/logging.handlers.html#sysloghandler - The SysLogHandler class, located in the logging.handlers module, supports sending logging messages to a remote or local Unix syslog.  
* Try logparser from  [LOGPAI/Log Analytics Powered by AI](https://github.com/logpai):  [https://github.com/logpai/logparser](https://github.com/logpai/logparser)  
>Logparser provides a machine learning toolkit and benchmarks for automated log parsing, which is a crucial step for structured log analytics. By applying logparser, users can automatically extract event templates from unstructured logs and convert raw log messages into a sequence of structured events. The process of log parsing is also known as message template extraction, log key extraction, or log message clustering in the literature.  
* Try 'minilog' a minimalistic logging wrapper for Python.  
[https://github.com/jacebrowning/minilog](https://github.com/jacebrowning/minilog)  
* Try 'Python Quick Logging | QLogging', colored Python logging based on Python the logging package.  
[https://github.com/sinkingtitanic/qlogging](https://github.com/sinkingtitanic/qlogging)  
* This utility approach: [https://github.com/karldoenitz/PythonUtils/tree/master/logger](https://github.com/karldoenitz/PythonUtils/tree/master/logger)  
* Minimal approach: [https://github.com/cherkavi/python-utilities/blob/master/logging/log-example.py](https://github.com/cherkavi/python-utilities/blob/master/logging/log-example.py)  
* If all you want is quick, easy console logging, look at [https://github.com/apparebit/konsole](https://github.com/apparebit/konsole)  
* "**structlog** makes logging in Python faster, less painful, and more powerful by adding structure to your log entries. It has been successfully used in production at every scale since 2013" [https://github.com/hynek/structlog](https://github.com/hynek/structlog)  

### Additional References  
* *From SolarWinds® [Loggly](https://www.loggly.com)®* Python Logging resources: [Python Logging Libraries and Frameworks](https://www.loggly.com/ultimate-guide/python-logging-libraries-frameworks/) and [Python Logging Basics](https://www.loggly.com/ultimate-guide/python-logging-basics/)  
* "Assisted Log Enabler for AWS" - Find resources that are not logging, and turn them on. Assisted Log Enabler for AWS is for customers who do not have logging turned on for various services, and lack knowledge of best practices and/or how to turn them on. [https://github.com/awslabs/assisted-log-enabler-for-aws](https://github.com/awslabs/assisted-log-enabler-for-aws)  
* "Python logging: do's and don'ts" [https://www.palkeo.com/en/blog/python-logging.html](https://www.palkeo.com/en/blog/python-logging.html)  
* "Logging in Python like a PRO" [https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/](https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/)  
* "The Ins and Outs of Logging in Python, Part 1" [https://monadical.com/posts/ins-and-outs-of-logging-in-python-part-one.html#](https://monadical.com/posts/ins-and-outs-of-logging-in-python-part-one.html#)  
* "Logging practices I follow" [https://www.16elt.com/2023/01/06/logging-practices-I-follow/](https://www.16elt.com/2023/01/06/logging-practices-I-follow/)  
* "How to Pickle and Unpickle Objects in Python." [https://stackabuse.com/how-to-pickle-and-unpickle-objects-in-python/](https://stackabuse.com/how-to-pickle-and-unpickle-objects-in-python/)  
* another example: https://github.com/timreibe/vaccipy/blob/master/tools/clog.py  
* Example github search for "log.py" files:  ```path:/(^|\/)log\.py$/  language:Python```  
* Create another example -- using a configuration file like the example at [https://github.com/PublicDataLab/DataPortalExplorer/blob/master/logging.ini](https://github.com/PublicDataLab/DataPortalExplorer/blob/master/logging.ini)  
* "Python Logging - The Log Levels." By Mike Driscoll. Jun 12, 2024 [https://www.pythonpapers.com/p/python-logging-the-log-levels](https://www.pythonpapers.com/p/python-logging-the-log-levels)  
* Using and abusing Python's logging module for more readable logs — Colin Chan (PyBay 2024) [https://www.youtube.com/watch?v=vrMHbep8-Lk](https://www.youtube.com/watch?v=vrMHbep8-Lk&list=PL85KuAjbN_gvx5b_BgLVcKfccnlZAVPMk&index=5)