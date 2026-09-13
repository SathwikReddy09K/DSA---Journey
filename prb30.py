
def length_of_last_word(str):
    length=0
    j=len(str)-1
    while j>=0 :
        if str[j]==" ":
            return length
        j-=1
        length+=1
    return length   


str=input("Enter string:")
print(str)
ans=length_of_last_word(str)
print(f"length of last word in {str}:", ans)
