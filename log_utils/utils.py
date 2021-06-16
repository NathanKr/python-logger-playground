from pprint import pformat
from typing import List
import pandas as pd

def sum2(num1,num2):
    print(args_to_string(n1=num1,n2=num2))
    return num1+num2

def sum_list(list : List[int]):
    print(args_to_string(list = list))
    return sum(list)

def foo(df : pd.DataFrame):
    print(args_to_string(df = df))

SEP = '\n'
def args_to_string(**kwargs)->str:
        args_as_string=SEP
        index=0
        for key,value in kwargs.items():
            formated_value = pformat(value)
            args_as_string += f'arg{index} {key} : {formated_value}{SEP}'
            index += 1

        return args_as_string     

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                  columns=['col1', 'col2', 'col3' , 'col4'])


sum2(1,2)
sum_list([1,2,3])
foo(df)