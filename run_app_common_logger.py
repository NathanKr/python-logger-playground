from log_utils.utils import configure_root_logger
from common_logger.utils1 import add 
from common_logger.utils2 import sub


# get_module_logger(
#     module_name=None, # root
#     log_level = logging.DEBUG, # default of level for root is WARNING
#     formatter = 'logger name : %(name)s , %(levelname)s , func : %(funcName)s , %(message)s , module : %(module)s ,line :  %(lineno)d , %(asctime)s' 
# )

configure_root_logger()

print(f'write log to file root.log')
print(add(1,2.3))
print(sub(4,5))