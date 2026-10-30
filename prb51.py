class solution:
    def removeduplicates(self,arr):
        i=0
        for j in range(len(arr)):
            if arr[i]!=arr[j]:
                arr[i+1]=arr[j]
                i+=1
        return arr[:i+1]        
        

s1=solution()
arr=list(map(int,input("Enter sorted array values only:").split()))  
print(arr)
ans=s1.removeduplicates(arr)  
print(" After removing duplicates from sorted array is",ans)

            