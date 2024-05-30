size=int(input("How many elements are in list: "))
list=[]
print("Enter the list")
for i in range(size):
    num=int(input(f"Enter number {i+1} : "))
    list.append(num)
def sum(list,i,size):
    if i==size:
        return 0
    return list[i]+sum(list,i+1,size)
print("Sum is ",sum(list,0,size))