def moveszeroes_toend(arr,n):
    j=-1
    for i in range(n):
        if arr[i]==0:
            j=i
            break

    if j==-1:
        return arr
    else:
        for i in range(j+1,n):
            if arr[i]!=0:
                arr[j],arr[i]=arr[i],arr[j]
                j+=1
    return arr

arr=[1,0,2,3,2,0,9,0,4,5,1,0]
n=len(arr)

ans=moveszeroes_toend(arr,n)
print("Moving zeroes to end of array:",ans)
