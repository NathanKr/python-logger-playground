import logging


def get_module_logger(module_name : str, log_level : int,formatter : str)->logging.Logger:
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

    log_name = f'{module_name}.log'
    file_handler = logging.FileHandler(log_name)

    oFormatter = logging.Formatter(formatter)
    file_handler.setFormatter(oFormatter)
    logger.addHandler(file_handler)

    return logger
