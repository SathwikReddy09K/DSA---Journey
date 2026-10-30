def consecutive_count(nums):
    n=len(nums)
    left=right=0
    max_count=1

    while right < n :
        
        if nums[right]==nums[right-1]+1:
            count=right-left+1
            max_count= max(max_count,count)
        else:
    
            left=right

    

        right+=1  

    return max_count


nums=list(map(int,input("Enter values:").split()))
sorted_nums=sorted(nums)
ans=consecutive_count(sorted_nums)
print("Longest consecutive numbers:",ans)