def Maxprofit(arr,n):
    min_val=arr[0]
    max_profit=0
    for i in range(1,n):
        if arr[i] < min_val :
            min_val=arr[i]
            index=i
    for i in range(index+1,n):
        price=arr[i]
        profit=price - min_val
        if profit > max_profit:
            max_profit=profit
    return max_profit

arr=[7,10,1,3,6,9,2]
print("original array :\n",arr)
n=len(arr)
ans=Maxprofit(arr,n)
print("Maximum profit in buy and sell is ",ans)   
