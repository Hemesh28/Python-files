n= int(input("Enter a number:"))
count=0
for i in range(2,n//2+1):
    if n%i==0:
        count+=1
if count==0:
    print("Prime")
else :
    print("Not Prime")
