'''Max adjacent diff sum with 1 replacement'''

def modify_array(arr):
    for i in range(1,len(arr)):
        diff=abs(arr[i-1] - arr[i])      
        if diff == 1:
            arr[i]=1
    return arr        

def sum_of_diff(arr):
    sum=0
    for i in range(1,len(arr)):
        sum+=abs(arr[i-1]-arr[i])     
    return sum    
            

arr=[3,2,1,4,5]
print("Original array:")
print(arr)

arr=modify_array(arr)

print("Array after modified:")
print(arr)

print("sum of diff array:",sum_of_diff(arr))



