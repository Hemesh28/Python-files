r=int(input("Enter the rows: "))
c=int(input("Enter the cols: "))
arr1=[[0 for _ in range(c)] for _ in range(r)]
arr2=[[0 for _ in range(c)] for _ in range(r)]
arr3=[[0 for _ in range(c)] for _ in range(r)]
print("Enter the array 1: ")
for i in range(r):
    for j in range(c):
        arr1[i][j]=int(input())
print("Enter the array 2: ")
for i in range(r):
    for j in range(c):
        arr2[i][j]=int(input())
print("The sum of of matrices is : ")
for i in range(r):
    for j in range(c):
        arr3[i][j]=arr1[i][j]+arr2[i][j]
        print(arr3[i][j],end=" ")
    print()