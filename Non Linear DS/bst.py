class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def addNode(root, val):
    if root==None:
        return Node(val)
    elif val>root.data:
        root.right = addNode(root.right, val)
    elif val<root.data:
        root.left = addNode(root.left, val)

    return root

def findMin(temp):
    while temp.left!=None:
        temp = temp.left
    return temp.data

def findMax(temp):
    while temp.right!=None:
        temp = temp.right
    return temp.data

def deleteNode(root, val):
    if root==None:
        return

    if val<root.data:
        root.left = deleteNode(root.left, val)
    elif val>root.data:
        root.right = deleteNode(root.right, val)
    else:
        if root.left==None and root.right==None:
            return None
        elif root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            minVal = findMin(root.right)
            root.data = minVal
            root.right = deleteNode(root.right, minVal)
    
    return root

# Inorder Traversal
def printTree(root):
    if root==None:
        return
    else:
        printTree(root.left)
        print(root.data, end=" ")
        printTree(root.right)

def preorderTraversal(root):
    if root==None:
        return
    else:
        print(root.data, end=" ")
        printTree(root.left)
        printTree(root.right)

def postorderTraversal(root):
    if root==None:
        return
    else:
        printTree(root.left)
        printTree(root.right)
        print(root.data, end=" ")
            

root = None
root = addNode(root, 6)
root = addNode(root, 5)
root = addNode(root, 9)
root = addNode(root, 11)
root = addNode(root, 4)
root = addNode(root, 8)

printTree(root)
print("")

root = deleteNode(root, 11)

printTree(root)
print("")

preorderTraversal(root)
print("")

postorderTraversal(root)
print("")