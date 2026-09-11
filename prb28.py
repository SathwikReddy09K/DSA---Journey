'''palindrome II after deleting one character'''
class string:
    def ispalindrome(self,str):
        n=len(str)
        count=0
        for i in range(int(n/2)):
            if str[i]!=str[n-i-1]:
                if len(str)<=3:
                    return 0
                count=+1
                if count>1:
                    return 0
               
        return 1

s=string()
str=input("Enter string:")
ans=s.ispalindrome(str)

if ans:
    print(f"{str} is a Palindrome after deleting one character")
else:
    print(f"{str} is not palindrome after deleting one character")      