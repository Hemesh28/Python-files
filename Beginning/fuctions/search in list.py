l=int(input("How many elements are in list: "))
list=[]
print("Enter the list")
for i in range(l):
    num=int(input(f"Enter number {i+1} : "))
    list.append(num)
key=int(input("Enter the element to search: "))
def search(key,list):
    for i in list:
        if i==key:
            return True
    return False
if search(key,list) == True:
    print("Element is found ")
else :
    print("Element is not found ")
        