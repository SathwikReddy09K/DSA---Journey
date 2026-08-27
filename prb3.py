'''maximun of sum of sub array of size k'''
   
def max_sumof_subarray(arr,n,k):
  sum=0
  for i in range (k):
     sum+=arr[i]
  high=sum                            #sum of 1st sub array size of k
  for j in range(n-k):
     prev=high
     sum-=arr[j] 
     sum+=arr[j+k] 
     if sum >prev:
          high=sum 
  return high        
k=int(input("Enter the size of sub array:"))
arr=[2,1,5,1,3,2]
n=len(arr)
ans=max_sumof_subarray(arr,n,k)        
print(f"Maximum sum of sub array of size {k} is:",ans)
