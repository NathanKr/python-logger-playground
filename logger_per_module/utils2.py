from config import UTILS2_LOGLEVEL
from log_utils import get_module_logger


formatter = 'logger name : %(name)s ,%(levelname)s , func : %(funcName)s , %(message)s , module : %(module)s ,line :  %(lineno)d , %(asctime)s'
logger = get_module_logger(__name__,UTILS2_LOGLEVEL,formatter)


def sub(num1 : float,num2 : float)->float:
    logger.debug(f'args : {num1} , {num2}')
    return num1-num2