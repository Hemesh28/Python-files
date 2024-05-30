arr=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        arr[i][j]*=2
        print(arr[i][j],end=" ")
    print()
for i in arr:
    print(i)