import logging
from utils1 import add 
from utils2 import sub

LOG_FILE_NAME = 'log.txt'

logging.basicConfig(
    level=logging.DEBUG,  # default is warning
    filename=LOG_FILE_NAME,   # default is console
    format='%(levelname)s , func : %(funcName)s , %(message)s , module : %(module)s ,line :  %(lineno)d , %(asctime)s'  
                    )  # log record format

print(f'write log to file : {LOG_FILE_NAME}')
print(add(1,2.3))
print(sub(4,5))