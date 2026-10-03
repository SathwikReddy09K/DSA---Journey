class solution:
    def Min_length(self,arr,target):
        min_len=0
        right=0
        left=0
        while right < len(arr) and left < right:
            if sum >=target:
                min_len=(min_len,right-left)
                sum-=arr[left]
                left+=1

            else:
                sum+=arr[right]
                right+=1
                
        return min_len
s1=solution()
arr=[1,3,5,2,2,4]
target=8
ans=s1.Min_length(arr,target)
print(ans)