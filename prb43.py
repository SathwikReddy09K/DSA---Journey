class solution:
    def Min_length(self,arr,target):
        min_len=len(arr)
        right=0
        left=0
        sum=0
        while right < len(arr) :
            if sum >target:
                min_len=min(min_len,right-left)
                sum-=arr[left]
                left+=1

            else:
                sum+=arr[right]
                right+=1
                
        return min_len
s1=solution()
arr=list(map(int,input("Enter array:").split()))
target=int(input("Enter target value:"))
ans=s1.Min_length(arr,target)
print(ans)