def prefix_sum(arr):

    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        arr[i]=sum

    return arr


arr=list(map(int,input("Enter array:").split()))
ans=prefix_sum(arr) 
print(f"Prefix sum of {arr} is",ans)