class string:
    def longest_palindrom(self,str):
        n=len(str)
        for i in range(int(n/2)):
            if str[i]!=str[n-i-1]:
                str=str[i+1:n-i-1]
        return str

s=string()
str=input("Enter string:")
ans=s.longest_palindrom(str)
print(ans)