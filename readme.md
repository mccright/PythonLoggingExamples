## My Python Logging Reminders  
[![](https://tokei.rs/b1/github.com/mccright/Log4NetDemo/?category=code)](https://github.com/mccright/Log4NetDemo)  

These examples are just reminders/demonstrations to help me get started on python scripts.  

### Approaches  

* The standard python logging module: `trylogging/LogTestLogging.py`  
    *Usage:*  
    `from LogTestLogging import init_logging`  
    `logger = init_logging()`  
    `logger.info('info testing message')`  
* The loguru module -- because it was so easy to configure: `tryloguru/LogTestLoGuru.py`  
    *Usage:*  
    `from LogTestLoGuru import init_logging`  
    `logger = init_logging()`  
    `logger.info('info testing message')`  
* The next...  

### Install  

None.  These are not modules, just little code reminders.  
That said,  `tryloguru/LogTestLoGuru.py` requires `pip3 install loguru --user`.  

### What Should You Log?   
See some ideas at: [https://github.com/mccright/rand-notes/blob/master/Application-Logging.md](https://github.com/mccright/rand-notes/blob/master/Application-Logging.md)  

### Explore later

Try 'minilog' a minimalistic logging wrapper for Python.  
[https://github.com/jacebrowning/minilog](https://github.com/jacebrowning/minilog)  

Try 'Python Quick Logging | QLogging', colored Python logging based on Python the logging package.  
[https://github.com/sinkingtitanic/qlogging](https://github.com/sinkingtitanic/qlogging)  

* This utility approach: [https://github.com/karldoenitz/PythonUtils/tree/master/logger](https://github.com/karldoenitz/PythonUtils/tree/master/logger)  
* Minimal approach: [https://github.com/cherkavi/python-utilities/blob/master/logging/log-example.py](https://github.com/cherkavi/python-utilities/blob/master/logging/log-example.py)  

### Additional References  

"Logging in Python like a PRO" [https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/](https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/)  

