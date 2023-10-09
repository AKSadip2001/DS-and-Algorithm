class Node:
    def __init__(self, int):
        self.val = int
        self.prev = None
        self.next = None

class DoublyLinkList:
    def __init__(self):
        self.root = None

    def addNode(self, int):
        newNode = Node(int)
        if self.root==None:
            self.root = newNode
        else:
            temp = self.root
            while temp.next!=None:
                temp=temp.next
            newNode.prev = temp
            temp.next = newNode
    
    def deleteNode(self, int):
        if self.root.val==int:
            if self.root.next==None:
                self.root=None
            else:
                self.root = self.root.next
                self.root.prev = None

            return
        
        temp = self.root
        while temp!=None:
            if temp.val==int:
                if temp.next==None:
                    temp.prev.next = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return
            temp=temp.next
    
    def printList(self):
        if(self.root==None):
            print("List is empty")
        else:
            temp=self.root
            while(temp!=None):
                print(temp.val, end=" ")
                temp = temp.next
            print()


list = DoublyLinkList()

list.addNode(5)
list.addNode(15)
list.addNode(25)
list.addNode(35)

list.printList()

list.deleteNode(45)

list.printList()