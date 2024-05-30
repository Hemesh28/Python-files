list=[]
l=int(input("Enter number of elements: "))
print("Enter the list")
for i in range(l):
    num=int(input(f"Enter number {i+1} : "))
    list.append(num)

def sum(list,Sum):
    for i in list:
        Sum+=i
    return Sum
print("Sum is : ",sum(list,0))
