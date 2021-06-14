from pprint import pformat

def foo(num1,num2):
    print(args_to_string(n1=num1,n2=num2))
    return num1+num2

SEP = '\n'

def args_to_string(**kwargs)->str:
        args_as_string=SEP
        index=0
        for key,value in kwargs.items():
            formated_value = pformat(value)
            args_as_string += f'arg{index} {key} : {formated_value}{SEP}'
            index += 1

        return args_as_string     


foo(1,2)