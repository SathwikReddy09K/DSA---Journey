def count_substring(str):
    count=0
    dict={}
    for i in range (len(str)):
        for j in range (i,len(str)+1):
            if str[i:j]  not in dict and str[i:j] !="":
                count+=1
                dict[str[i:j]]=count            
    return count

str=input("Enter string:")
ans=count_substring(str)
print(f"No.of distinct substrings in {str} is:",ans)