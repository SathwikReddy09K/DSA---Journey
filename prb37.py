def ReverseDegree(str):
    str=str.upper()
    index=1
    sum=0
    for s in str:
        value=(ord("Z")-ord(s)) + 1
        print(f"index in reversing {s} is",value)
        sum += (value * index)
        index+=1
    return sum


str=input("Enter string:")
ans=ReverseDegree(str)
print(f"sum of index in reversing alphabet of {str}", ans)    