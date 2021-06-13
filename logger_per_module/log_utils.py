import logging


def get_module_logger(module_name : str, log_level : int,formatter : str)->logging.Logger:
    logger = logging.getLogger(module_name) # use with module_name
    logger.setLevel(log_level) # e.g logging.DEBUG

    log_name = f'{module_name}.log'
    file_handler = logging.FileHandler(log_name)

    oFormatter = logging.Formatter(formatter)
    file_handler.setFormatter(oFormatter)
    logger.addHandler(file_handler)

    return logger
