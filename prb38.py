def sumofdigits(nums):
    for i in range(len(nums)):
        first_digit=nums[i]//10
        second_digit=nums[i]%10
        sum=first_digit + second_digit
        if sum == i :
            return i
    return -1


nums=[1,10,12,23]
ans=sumofdigits(nums)
print("smallest index with digit sum equal to index:",ans)


