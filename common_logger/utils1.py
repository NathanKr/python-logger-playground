import logging


def add(num1 : float,num2 : float)->float:
    logging.warning(f'args : {num1} , {num2}')
    return num1+num2