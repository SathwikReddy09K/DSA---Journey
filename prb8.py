def product_array(arr,n):
    prod=1
    for i in range(n):
        prod*=arr[i]
    return prod
def final_array(arr,n,prod):
    for i in range(n):
        arr[i]=int(prod/arr[i])
    return arr

arr=list(map(int,input("Enter array input values:").split()))
print("origin array:",arr)
n=len(arr)
prod=product_array(arr,n)
print("product of array expect itself:",final_array(arr,n,prod))
      
