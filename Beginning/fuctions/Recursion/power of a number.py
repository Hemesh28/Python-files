x=int(input("Enter the number: "))
y=int(input("Enter the exponent: "))
def f(x,y):
    if(y==0):
        return 1
    return f(x,y-1)*x
print(f"{x} raised to the power of {y} is: ", f(x,y))