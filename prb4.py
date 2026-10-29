class solution:
     def leftrotationby_1(self,arr,n):
        temp=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]

        arr[n-1]=temp

        return arr    
    
if __name__=="__main__":
     s1=solution()
     arr=[1,2,3,4,5]
     n=len(arr)
     print("Orginal array:\n",arr)
     ans=s1.leftrotationby_1(arr,n)
     print("After left rotation of array by one place:\n",ans)
        
