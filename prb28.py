'''palindrome two after deleting one character'''
class string:
    def ispalindrome(self,str):
        n=len(str)
        count=0
        for i in range(int(n/2)):
            if str[i]!=str[n-i-1]:
                count+=1

        if count>1:
            return 0
        else:       
            return 1

s=string()
str=input("Enter string:")
ans=s.ispalindrome(str)

if ans:
    print(f"{str} is a Palindrome")
else:
    print(f"{str} is not palindrome")      