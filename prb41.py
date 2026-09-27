def count_substring(str,n):
    count=0
    dict={}
    for i in range (n):
        for j in range (i+1,n+1):
            if str[i:j]  not in dict:
                count+=1
                dict[str[i:j]]=count            
    return count

str=input("Enter string:")
n=len(str)
ans=count_substring(str,n)
print(f"No.of distinct substrings in {str} is:",ans)