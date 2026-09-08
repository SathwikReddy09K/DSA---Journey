class string:
    def ispalindrome(self,str):
        n=len(str)
        for i in range(int(n/2)):
            if str[i]!=str[n-i-1]:
                return 0
        return 1

s=string()
str=input("Enter string:")
ans=s.ispalindrome(str)

if ans:
    print(f"{str} is a Palindrome")
else:
    print(f"{str} is not palindrome")      