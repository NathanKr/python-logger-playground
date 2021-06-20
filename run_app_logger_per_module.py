from log_utils.utils import configure_root_logger
from logger_per_module.utils1 import add 
from logger_per_module.utils2 import sub

configure_root_logger()

print(add(1,2.3))
print(sub(4,5))