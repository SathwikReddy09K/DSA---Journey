class stack:
    def __init__(self):
        self.stack=[]
    def Isvalid(self,str):
        for char in str: 
            if len(self.stack)==0:
                self.stack.append(char)  
 
            else:     
                if ((self.stack[-1]=='('and char==')')or (self.stack[-1]=='{' and char=='}')or (self.stack[-1]=='[' and char==']')):

                    self.stack.pop()
                else:
                    self.stack.append(char)

        if len(self.stack)==0:
            return True
        else:
            return False       

                  
s1=stack()
str=input("Enter string within {,},[,],(,):")
ans=s1.Isvalid(str)
print(f"Checking  vaild parentheses of {str}:",ans)
 