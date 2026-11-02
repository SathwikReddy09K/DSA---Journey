def majorityelement(arr):
    n=len(arr)
    count=0
    for i in range(n):
        if count==0:
            val=arr[i]
            count=1
        elif val==arr[i]:
            count+=1
        else:
            count-=1

    count=0
    for num in arr:
        if num==val:
            count+=1

    if count > n//2:
        return val
    else:
        return -1

arr=list(map(int,input("Enter array:").split()))
ans=majorityelement(arr)
print(f"Majority elements in {arr} is",ans)
            



 
   
