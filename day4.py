class solution:

    def reversing_array(self,arr):     # reversing array
        for i in range(int(n/2)):
            arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        return arr 
    
    def left_rotation(self,arr,n):
        for i in range(int(n/2)):
            arr[i],arr[n-i-2]=arr[n-i-2],arr[i]
        return arr 

s1=solution()
arr=[1,2,3,4,5]
n=len(arr)
print("original array:\n",arr)
rev=s1.reversing_array(arr)
print("After reversing array:\n",rev)
ans=s1.left_rotation(rev,n)
print("After left rotation array by one position:\n ",ans)
