import logging
from utils1 import add 
from utils2 import sub

LOG_FILE_NAME = 'root.log'

logging.basicConfig(
    level=logging.DEBUG,  # default is warning
    filename=LOG_FILE_NAME,   # default is console
    format='logger name : %(name)s , %(levelname)s , func : %(funcName)s , %(message)s , module : %(module)s ,line :  %(lineno)d , %(asctime)s'  
                    )  # log record format


print(add(1,2.3))
print(sub(4,5))