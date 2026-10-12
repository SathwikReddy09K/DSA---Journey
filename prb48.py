class solution:
    def searchRange(self,nums,target):
        first=0
        last=len(nums)-1
        pos=[]

        while first < last:     
            if nums[first] == target:
                pos.append([first,first+1])
                break
            if nums[last] == target:
                pos.append([last-1,last]) 
                break
            first+=1
            last-=1 
        if pos==[]:
            pos.append([-1,-1])
        return pos

s1=solution()
nums=list(map(int,input("Enter elements:").split()))
target=int(input("Enter target element:"))
ans=s1.searchRange(nums,target)  
print("First and last position of element in sorted array:",ans) 
     
                 
                 
                 