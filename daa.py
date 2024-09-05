##arr=[45,43,45,54,64,34]
##for i in range(0,len(arr)-1):
##    for j in range(0,len(arr)-i-1):
##        if(arr[j]>arr[j+1]):
##            temp=arr[j]
##            arr[j]=arr[j+1]
##            arr[j+1]=temp
##for i in arr:
##    print(i)


##arr=[43,463,43,53,56]
##
##for i in range(0,len(arr)-1):
##    minindex=i
##    for j in range(i+1,len(arr)):
##        if(arr[j]<arr[minindex]):
##            minindex=j
##
##    temp=arr[minindex]
##    arr[minindex]=arr[i]
##    arr[i]=temp
##
##for i in arr:
##    print(i)

a="i am india"
b="india"

n=len(a)
m=len(b)
for i in range(n-m+1):
    j=0
    while(j<m and a[i+j]==b[j]):
        j=j+1

    if(j==m):
        print(i)
        
    






















