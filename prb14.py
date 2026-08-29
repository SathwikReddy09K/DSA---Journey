'''Middle nodes of  single linked list'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def delete_fornt_node(self,head):
        fornt=head
        head=head.next
        fornt.next=None
        return head
    def delete_last_node(self,new_head):
        curr=new_head
        while curr.next != None:
            prev=curr
            curr=curr.next
        prev.next=None
        return new_head

        

node1=Node(10)            
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=None

head=node1

print("Oringial single linkedlist:")
head.traveral(head)
print()

new_head=head.delete_fornt_node(head)
ans=head.delete_last_node(new_head)

print("Middle nodes of single linked list :")
head.traveral(ans)


