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

### Explore later

Try 'Python Quick Logging | QLogging', colored Python logging based on Python the logging package.  
[https://github.com/sinkingtitanic/qlogging](https://github.com/sinkingtitanic/qlogging)  
