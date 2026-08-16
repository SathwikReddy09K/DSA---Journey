class solution:
    def reversingarray(self,arr,n):   # reversing array
        for i in range(int(n/2)):
            arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        return arr
    def leftrotation(self,arr,n):
        for i in range(int(n/2)):
                arr[i],arr[n-i-2]=arr[n-i-2],arr[i]
        return arr

if __name__=="__main__":
     s1=solution()
     arr=[1,2,3,4,5]
     n=len(arr)
     print("Orginal array:\n",arr)
     rev=s1.reversingarray(arr,n)
     print("After reversing array:\n",rev)
     ans=s1.leftrotation(rev,n)
     print("After left rotation of array by one place:\n",ans)
        