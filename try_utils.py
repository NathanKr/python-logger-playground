from log_utils.utils import args_to_string
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

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                  columns=['col1', 'col2', 'col3' , 'col4'])


sum2(1,2)
sum_list([1,2,3])
foo(df)