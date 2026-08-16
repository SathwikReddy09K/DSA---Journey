# Rotate a array by k places (left or right)

def reversing(arr,n,mid):   # reversing array
    for i in range(mid):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    return arr 
      
def Rightrotation(arr,n,k):   
        for i in range(int(k/2)):
            arr[i],arr[k-i-1]=arr[k-i-1],arr[i]
        m=n-k
        for i in range(int(m/2)):
            arr[k+i],arr[n-i-1]=arr[n-i-1],arr[k+i]
        return arr 
def leffrotation(arr,n,k):
    m=n-k
    for i in range(int(m/2)):
        arr[i],arr[m-1-i]=arr[m-1-i],arr[i]
    p=n-m    
    for i in range(int(p/2)):
        arr[m+i],arr[n-i-1]=arr[n-i-1],arr[m+i]
    return  arr   
          
arr=[1,2,3,4,5,6,7]
print(" Original array:\n",arr,)

n=len(arr)
mid=int(n/2)

reversing(arr,n,mid)
print("\n Reversing original array:\n",arr)

k=int(input("\n No.of rotations array:\n"))
rotation=input("\n Rotation of array left (or) right:\n").lower()

if rotation=="right":  
     Rightrotation(arr,n,k)
     print(f"\n After {k} rotations of array in right side:\n {arr}")
elif rotation=="left":
     leffrotation(arr,n,k)
     print(f"\n After {k} rotations of array in left side:\n{arr}")
else:
    print("\n Invalid input,enter only left or right\n")