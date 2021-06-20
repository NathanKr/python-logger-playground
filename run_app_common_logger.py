from log_utils.utils import configure_root_logger
from common_logger.utils1 import add 
from common_logger.utils2 import sub

configure_root_logger()

print(f'write log to file root.log')
print(add(1,2.3))
print(sub(4,5))