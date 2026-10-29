# Rotate a array by k places (left or right)
def Rightrotation(arr,n,k):

    # reversing first k elements
    for i in range (int((n-k)/2)):
        arr[i],arr[k-i]=arr[k-i],arr[i]

    # reversing remaining elements
    for i in range(k):
        arr[n-k+i],arr[n-i-1]=arr[n-i-1],arr[n-k+i]
    
    # reversing array 
    for i in range(int(len(arr)/2)):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
      
    return arr  

def leffrotation(arr,n,k):
    # reversing first n-k elements
    for i in range (int(k/2)):
        arr[i],arr[k-i-1]=arr[k-i-1],arr[i]

    # reversing  remaining elements
    for i in range(int((n-k)/2)):
        arr[k+i],arr[n-i-1]=arr[n-i-1],arr[k+i]

    # reversing array
    for i in range(int(len(arr)/2)):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
      
    return arr
      
arr=[1,2,3,4,5,6,7]
print(" Original array:\n",arr,)
n=len(arr)

k=int(input("\n No.of rotations array:\n"))

#It useful,when no.of rotations are more than n"
k=k % n

rotation=input("\n Rotation of array left (or) right:\n").lower()

if rotation=="right":  
     Rightrotation(arr,n,k)
     print(f"\n After {k} rotations of array in right side:\n {arr}")
elif rotation=="left":
     leffrotation(arr,n,k)
     print(f"\n After {k} rotations of array in left side:\n{arr}")
else:
    print("\n Invalid input,enter only left or right\n")
