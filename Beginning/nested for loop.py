a=int(input("Enter the x coordinate of last point "))
b=int(input("Enter the y coordinate of last point "))
for j in range(0,b+1):
    for i in range(0,a+1):
        print(f"({i},{j})",end=" ")
    print(" ")