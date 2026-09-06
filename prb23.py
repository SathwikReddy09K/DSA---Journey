
def pairandsum(arr):
    sum=0
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            sum+=arr[i] & arr[j]
    return sum        

arr=[10,20,30,40]
print("Original array:")
print(arr)

print("After doing bitwise(AND) operation:")
print(pairandsum(arr))         
    
