n=int(input("Enter which number to print: "))
def f(n):
    if(n==0):
        return 1
    return f(n-1)*n
print(f(n))