import logging
import inspect

class LogGen:
    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)
        file = logging.FileHandler("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Logs\\logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s: %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger

# DEBUG
# INFO
# WARN
# ERROR
# CRICTICAL
