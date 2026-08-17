'''pivot inex means,where sum of left array = sum of right array'''

def pivotindex(arr,n,sum):
    right=sum
    left=0
    for i in range(1,n):
        left+=arr[i-1]
        right-=arr[i]
        if right==left:
            return i
    else:
        return -1
def sum_of_array(arr,n):
    sum=0
    for i in range(1,n):
        sum+=arr[i]
    return sum
        
                    
arr=list(map(int,input("Enter array values:").split())) 
n=len(arr)
print("original array:\n",arr)
sum=sum_of_array(arr,n)
ans=pivotindex(arr,n,sum) 
print("pivot index of array:",ans)