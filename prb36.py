class stack:
    def __init__(self):
        self.stack=[]
    def Isvalid(self,str):
        for char in str:     
            if self.stack[-1]==char:
                self.stack.pop()
            else:
                self.stack.append(char)

            if len(self.stack)==0:
                    self.stack.append(char) 

        if len(self.stack)==0:
            return 1
        else:
            return 0        

                  
s1=stack()
ans=s1.Isvalid("({]")
print(ans)

 