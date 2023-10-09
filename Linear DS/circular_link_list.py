class Node:
    def __init__(self, int, rootNode):
        self.val = int
        self.next = rootNode

class CircularLinkList:
    def __init__(self):
        self.root = None

    def addNode(self, int):
        newNode = Node(int, self.root)
        if self.root==None:
            self.root=newNode
            self.root.next=self.root
            return
        else:
            temp=self.root
            while temp.next!=self.root:
                temp=temp.next
            temp.next=newNode
    
    def deleteNode(self, val):
        if self.root.val==val:
            if self.root.next==self.root:
                self.root=None
            else:
                temp = self.root
                while temp.next != self.root:
                    temp=temp.next
                self.root=self.root.next
                temp.next=self.root
            return
        else:
            temp = self.root
            while temp.next != self.root:
                if temp.next.val==val:
                    temp.next = temp.next.next
                    return
                temp=temp.next


    
    def printList(self):
        temp=self.root

        while True:
            print(temp.val, end=" ")
            if temp.next==self.root:
                print(self.root.val, end=" ")
                break
            temp=temp.next
        print("")


list = CircularLinkList()

list.addNode(10)
list.addNode(20)
list.addNode(30)
list.addNode(40)

list.printList()

list.deleteNode(40)

list.printList()


