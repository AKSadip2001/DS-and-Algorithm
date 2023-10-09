class Node:
    def __init__(self, int):
        self.val = int
        self.next = None

class LinkList:
    def __init__(self):
        self.root=None
    
    def addNode(self, int):
        newNode = Node(int)
        if self.root==None:
            self.root=newNode
        else:
            temp = self.root
            while(temp.next!=None):
                temp = temp.next
            temp.next=newNode

    def deleteNode(self, int):
        if self.root==None:
            print("No element in list")
            return
        elif self.root.val==int:
            temp = self.root
            self.root = self.root.next
            print("node removed")
            del temp
            return
        else:
            temp = self.root
            while temp.next!=None:
                if temp.next.val==int:
                    temp.next=temp.next.next
                    print("node removed")
                    return
                temp = temp.next
            print("Node not found")
                

    def printList(self):
        if(self.root==None):
            print("List is empty")
        else:
            temp=self.root
            while(temp!=None):
                print(temp.val, end=" ")
                temp = temp.next
            print()

list = LinkList()

list.addNode(5)
list.addNode(15)
list.addNode(25)
list.addNode(35)

list.printList()

list.deleteNode(45)

list.printList()