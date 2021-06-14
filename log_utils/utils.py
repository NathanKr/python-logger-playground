def foo(num1,num2):
    smart_print(pair_sep='\n',n1=num1,n2=num2)
    return num1+num2


def smart_print(pair_sep,**kwargs):
    for key,value in kwargs.items():
        print (f'{key} {value}',end=pair_sep)



foo(1,2)