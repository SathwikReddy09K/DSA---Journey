def maxsubarraysum(arr):
    n=len(arr)
    max_sum=sum=0
    for i in range(n):
        sum+=arr[i]
        
        if  sum < 0:
            sum=0
        else:
            max_sum=max(sum,max_sum)

    return max_sum        

arr=[-2,-3,4,-1,-2,1,5,-3]
ans=maxsubarraysum(arr)
print(f"Maximum subarray sum in {arr} is ",ans)