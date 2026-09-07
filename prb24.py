def Roman_to_int(str):
    k=len(str)
    sum=0
    for i in range(0,k):
        val=str[i]
        if val=="I":
            sum+=1
        elif val=="V":
                sum+=5
        elif val=="X":
            sum+=10        
        elif val=="L":
            sum+=50
        elif val=="C":
            sum+=100
        elif val=="D":
            sum+=500    
        elif val=="M":
            sum+=500
        else:
            sum+=0
    return sum        

str=input("Enter roman letters:")
str=str.upper()

ans=Roman_to_int(str)
print("coverting roman to integer:")
print(ans)

