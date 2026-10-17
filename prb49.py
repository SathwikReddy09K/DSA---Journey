class solution:
    def maxalternatingsum(self,nums):
        i=0
        sum=0
        for val in nums:
            sq_val=val*val
            if i % 2==0:
                sum+=sq_val
            else:
                sum-=sq_val
            i+=1
        return sum

s1=solution()
nums=[1,2,3]
ans=s1.maxalternatingsum(nums)  
print(ans)   
