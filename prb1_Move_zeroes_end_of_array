class solution:                              
    def movezeroes_to_end(self,arr,n):           
        i=0
        j=n-1
        while(i<j):
            if arr[i]==0:
              if arr[j]!=0:
                arr[i],arr[j]=arr[j],arr[i]     #swap(arr[i],arr[j])
                i+=1
                j-=1
              else:
               j-=1
            else:
              i+=1
        return arr                               

s1=solution()      
arr=list(map(int,input("Enter array:").split()))    #input array
print("Original array:\n",arr)
n=len(arr)         #length of array
ans=s1.movezeroes_to_end(arr,n)                     
print("After moving zeroes to end of array:\n",ans)
