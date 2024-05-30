#Down Up Solution -> O(N)
def fibonacci(a,b,i,n):
    
    c=a+b
    a=b
    b=c
    if i==n:
      print(c)
      return 0
    fibonacci(a,b,i+1,n)
    
n=int(input("Enter which number to print: "))
print(f"The {n}th number in fibonacci series is: ")
a=0
b=1
fibonacci(a,b,2,n)


#Top Down Solution -> O(2^N)
# n=int(input("Enter which number to print: "))
# def f(n):
#   if(n==0):
#     return 0
#   if n==1:
#     return 1
#   return f(n-1)+f(n-2)
# print(f(n))