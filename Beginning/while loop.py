sum=0
while 1:
    a=(input("Enter yes to continue giving numbers or enter no to break and print sum: "))
    if a=="no":
        print("Sum is :",sum)
        break
    elif a=="yes" :
        b=int(input("Enter number to add: "))
        sum+=b