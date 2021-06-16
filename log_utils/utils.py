from pprint import pformat
import logging
import os

def configure_root_logger():
    """
        i prefer to use this a not logging.basicConfig because this is more flexiable
        e.g. in term of controlling encoding of the log file
    """
    module_name=None # root
    log_level = logging.DEBUG # default of level for root is WARNING
    formatter = 'logger name : %(name)s , %(levelname)s , func : %(funcName)s , %(message)s , module : %(module)s ,line :  %(lineno)d , %(asctime)s' 

     # no need to use the return , it is accessed by logging
    get_logger_with_file_handler(module_name,log_level,formatter)



def get_logger_with_file_handler(module_name : str, log_level : int,formatter : str)->logging.Logger:
    """
        get logger with file handler
        the log file is the same as the module name with extension .log

    Args:
        module_name (str): pass here__name__
        log_level (int): pass here e.g. logger.DEBUG
        formatter (str): pass here e.g. 'logger name : %(name)s , %(levelname)s,
                                        func : %(funcName)s , %(message)s , module : %(module)s ,
                                        line :  %(lineno)d , %(asctime)s'  

    Returns:
        logging.Logger: [description]
    """
    logger = logging.getLogger(module_name) # use with module_name
    logger.setLevel(log_level) # e.g logging.DEBUG

    if module_name == None:
        file_name = 'root'
    else:
        file_name = module_name

    
    log_name = os.path.join('logs',f'{file_name}.log')
    file_handler = logging.FileHandler(log_name)

    oFormatter = logging.Formatter(formatter)
    file_handler.setFormatter(oFormatter)
    logger.addHandler(file_handler)

    return logger


SEP = '\n'
def args_to_string(**kwargs)->str:
        args_as_string=SEP
        index=0
        for key,value in kwargs.items():
            formated_value = pformat(value)
            args_as_string += f'arg{index} {key} : {formated_value}{SEP}'
            index += 1

        return args_as_string     

