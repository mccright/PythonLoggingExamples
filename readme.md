## My Python Logging Reminders  
[![](https://tokei.rs/b1/github/mccright/PythonLoggingExamples)](https://github.com/mccright/PythonLoggingExamples)  

These examples are just reminders/demonstrations to help me get started on any given python script.  

> For a more detailed description of Python logging refer to [the official manual](https://docs.python.org/3.10/library/logging.html#module-logging).  There is a useful diagram outlining the flow of log event information in loggers and handlers at: [https://docs.python.org/3.10/howto/logging.html#logging-flow](https://docs.python.org/3.10/howto/logging.html#logging-flow).  And don't ignore the logging cookbook if you have the urge to do your own thing [https://docs.python.org/3/howto/logging-cookbook.html](https://docs.python.org/3/howto/logging-cookbook.html)  
* Or a quick overview: "Logging in Python: A Developer’s Guide." By Bala Priya C., 2022-07-19 [https://blog.sentry.io/2022/07/19/logging-in-python-a-developers-guide](https://blog.sentry.io/2022/07/19/logging-in-python-a-developers-guide)  

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
* [requestsDebugging](https://github.com/mccright/PythonLoggingExamples/blob/main/requestsDebugging/devClient.py): A useful approach to *requests* debug logging especially valuable when attempting to deal with a poorly documented or otherwise opaque API.  This is well explained by Ben Hoey at [bhoey.com](https://bhoey.com/blog/better-debug-logging-for-the-python-requests-library/).  

* The next...  

### Install  

None.  These are not modules, just little code reminders.  
That said,  `tryloguru/LogTestLoGuru.py` requires `pip3 install loguru --user`.  

### What Should You Log?   
See some ideas at: [https://github.com/mccright/rand-notes/blob/master/Application-Logging.md](https://github.com/mccright/rand-notes/blob/master/Application-Logging.md)  

### Explore later

* Try 'minilog' a minimalistic logging wrapper for Python.  
[https://github.com/jacebrowning/minilog](https://github.com/jacebrowning/minilog)  
* Try 'Python Quick Logging | QLogging', colored Python logging based on Python the logging package.  
[https://github.com/sinkingtitanic/qlogging](https://github.com/sinkingtitanic/qlogging)  
* This utility approach: [https://github.com/karldoenitz/PythonUtils/tree/master/logger](https://github.com/karldoenitz/PythonUtils/tree/master/logger)  
* Minimal approach: [https://github.com/cherkavi/python-utilities/blob/master/logging/log-example.py](https://github.com/cherkavi/python-utilities/blob/master/logging/log-example.py)  
* If all you want is quick, easy console logging, look at [https://github.com/apparebit/konsole](https://github.com/apparebit/konsole)  

### Additional References  
* "Python logging: do's and don'ts" [https://www.palkeo.com/en/blog/python-logging.html](https://www.palkeo.com/en/blog/python-logging.html)  
* "Logging in Python like a PRO" [https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/](https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/)  
* "The Ins and Outs of Logging in Python, Part 1" [https://monadical.com/posts/ins-and-outs-of-logging-in-python-part-one.html#](https://monadical.com/posts/ins-and-outs-of-logging-in-python-part-one.html#)  
* "How to Pickle and Unpickle Objects in Python." [https://stackabuse.com/how-to-pickle-and-unpickle-objects-in-python/](https://stackabuse.com/how-to-pickle-and-unpickle-objects-in-python/)  
