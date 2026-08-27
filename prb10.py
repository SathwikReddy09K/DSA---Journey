class linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def reversing(self,curr):
        prev=None
        while curr!=None:
           next_node=curr.next
           curr.next=prev
           prev=curr
           curr=next_node
        return prev
        


node1=linkedlist(10)
node2=linkedlist(20)
node3=linkedlist(30)
node4=linkedlist(40)
node5=linkedlist(50)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None

head=node1
print("original single linkedlist:")
head.traveral(head)

rev=head.reversing(head)

print("After reversing single linkedlist:")
head.traveral(rev)

