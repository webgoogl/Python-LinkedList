# Linked List Concept

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Function to Traverse LinkedList

def linkedlist(n):
    head=n    
    while head != None:
        print(head.data,end=" ->")
        head=head.next
    print("None")
    print("\n")
    
# Function to Add Node at Begning

def Insert_At_Begning(n,new):
    head=n
    NewNode=node(new)
    NewNode.next=head
    head=NewNode
    linkedlist(head)
    print("\n")

# Function to Add Node at End

def Insertion_At_End(n,new):
    NewNode=node(new)
    head=n

    while n.next!=None:
        n=n.next
    n.next=NewNode
    linkedlist(head)
    print("\n")

# Function to Add Node at Any Positions

def Insertion_At_Any(n,new):
    NewNode=node(new)
    head=n

    while n!=None and n.data!=10:
        n=n.next
    NewNode.next=n.next
    n.next=NewNode
    
    linkedlist(head)
    print("\n")

        
""" ######################################################################### """

n1=node(10)
n2=node(20)

n1.next=n2

linkedlist(n1)

new=int(input("Insert Data for NewNode -> "))
#Insert_At_Begning(n1,new)
#Insertion_At_End(n1,new)
Insertion_At_Any(n1,new)



