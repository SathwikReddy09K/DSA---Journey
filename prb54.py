# METHOD 1(using sum)
def missingnumber_m1(arr,n):
    N=n+1
    sum=0
    org_sum=N*(N+1)/2

    for i in range(n):
        sum+=arr[i]

    Missing_value=int(org_sum-sum)
    return Missing_value


# METHOD 2(using XOR operand)
def missingnumber_m2(arr,n):            #XOR : case1:(1^1=0),case2:(1^0=1)
    N=n+1    
    XOR1=XOR2=0
   
    for i in range (1,N+1):
        XOR1=XOR1^i
    

    for i in range(n):
        XOR2=XOR2^arr[i]
    

    missing_value=XOR1^XOR2
    return missing_value

      
      

arr=[1,5,2,4]
n=len(arr)

case=input("Enter your's choice(method1 or method2):")

if case=="method1":
  ans=missingnumber_m1(arr,n)
  print(f"Mising element in  {arr} is",ans)

elif case=="method2":
   ans=missingnumber_m2(arr,n)
   print(f"Mising element in  {arr} is",ans)

else:
   print("You enter wrong case")
   
   

   
   

    
