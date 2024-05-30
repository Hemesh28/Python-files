# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# r=500
# while r>0:
#     gcd=b
#     r=a%b
#     a=b
#     b=r
#     print(gcd)
# print("GCD is ", gcd)

dividend=int(input("Enter the first number: "))
divisor=int(input("Enter the second number: "))
r=dividend%divisor
while r!=0:
    
    
    dividend=divisor
    divisor=r
    r=dividend%divisor
print("GCD is ", divisor)
print(0.1+0.2)