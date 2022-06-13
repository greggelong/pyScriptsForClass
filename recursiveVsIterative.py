def fact(num):
    if num == 1:
        return 1
    else:
        num = num * fact(num-1)
        
    return num



def factIter(num):
    result = 1
    for i in range(1,num+1):
        result = result * i
        
    return result
        
        
        
def fib(num):
    if num <=2:
        return 1
    else:
        return fib(num-1)+fib(num-2)


def fibIter(n):
    if n <=2:
        return 1
    else:
        f1 =1
        f2 =1
        result = 0
        for i in range(3, n+1):
            result = f1 + f2
            f1= f2 # swap variables
            f2 = result 
    return result
        




for n in range(1,101):
    print(n, ":",fibIter(n))

