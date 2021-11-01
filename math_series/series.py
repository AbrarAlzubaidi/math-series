
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas (n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def series2(n):
    if n==0:
        return 7
    else:
        return 1+series2(n-1)


def sum_series(n, option1=None, option2=None):
    if option1 == None and option2 == None:
        return fibonacci(n)
    elif option1 == 2 or option2 == 1:
        return lucas(n)
    else:
        return series2(n)

        

sum_series(5,4,2)