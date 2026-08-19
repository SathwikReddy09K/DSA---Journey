class linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,current):
        while current!=None:
            print(current.data,"-<",end=" ")
            current=current.next
        print("NULL")


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
current=head
print("original single linkedlist:")
node1.traveral(current)

node2.next=node1
node3.next=node2
node4.next=node3
node5.next=node4
node1.next=None

head=node5
current=head
print("Reversing  single linkedlist:")
node5.traveral(current)
