from .config import UTILS1_LOGLEVEL
import logging
from log_utils.utils import get_logger_with_file_handler

formatter = 'logger name : %(name)s ,%(levelname)s , func : %(funcName)s , %(message)s , module : %(module)s ,line :  %(lineno)d , %(asctime)s'
logger = get_logger_with_file_handler(__name__,UTILS1_LOGLEVEL,formatter)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)


def add(num1 : float,num2 : float)->float:
    logger.warning(f'args : {num1} , {num2}')
    return num1+num2