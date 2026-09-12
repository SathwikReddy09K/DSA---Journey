'''longest palindrom substring'''

class string:
    def longest_palindrom(self,str):
        n=len(str)
        str1=str
        for i in range(int(n/2)):
            if str[i]!=str[n-i-1]:
                str1=str[i+1:n-i-1]
        if len(str1)==0:
            str1=None        
        return str1

s=string()
str=input("Enter string:")
ans=s.longest_palindrom(str)
print("longest palindrom substring is:",ans)