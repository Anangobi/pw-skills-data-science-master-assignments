n=int(input("Enter the number of line"))
k=1
m=n-1
for i in range(0,n):
    for j in range(0,m):
        print("",end=" ")
    m=m-1
    for k in range(0,k):
        print("*",end=" ")
    k=k+2
    print("")
