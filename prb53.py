def unionoftwoarray(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    union=[]
    for i in range(n1):
        if arr1[i]  not in union:
            union.append(arr1[i])

    for i in range(n2):
        if arr2[i]  not in union:
            union.append(arr2[i])

    return union
# Two input arrays should be in sorted array
arr1=list(map(int,input("Enter values array 1: ").split()))
arr2=list(map(int,input("Enter values array 2: ").split()))

ans=unionoftwoarray(arr1,arr2)
print("union elements from two  sorted arrays is",ans)