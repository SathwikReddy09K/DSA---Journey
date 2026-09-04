class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,head):
        curr=head
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def divide(self,head):
        ohead=ehead=None
        curr=head

        while curr != None:
            next_node=curr.next
            curr.next=None
            
            if curr.data % 2 == 0 :

                if ehead == None :
                    ehead=curr
                    etail=ehead

                etail.next=curr
                etail=etail.next
            else:
                if ohead == None :
                    ohead=curr
                    otail=ohead

                otail.next=curr
                otail=otail.next
                    
            curr=next_node
        otail.next=ehead
        etail.next= None
    
        return ohead

      
head=Node(16)
head.next=Node(15)
head.next.next=Node(8)
head.next.next.next=Node(7)
head.next.next.next.next=Node(2)
head.next.next.next.next.next=Node(1)
head.next.next.next.next.next.next=Node(6)

print("single linked list:")
head.traveral(head)
ans=head.divide(head)
print("Odd--even single linked list:")
head.traveral(ans)

