import queuelinkedlist as queue

class BSTNode():
    def __init__(self,data):
        self.data = data
        self.leftChild=None
        self.rightChild=None

      
def insert(rootV,value):
        if rootV.data == None:
            rootV.data = value
            #print("main")
        elif value<=rootV.data:
            if rootV.leftChild is None:
                rootV.leftChild = BSTNode(value) #interesting
                #print("left")
                #print(rootV.leftChild)
            else:
                insert(rootV.leftChild,value)
        else:
            if rootV.rightChild == None:
                rootV.rightChild = BSTNode(value)
                #print("right")
            else:
                insert(rootV.rightChild,value)
        return "Inserted successfully"
   
def preTrav(root):
    if not root:
        return
    else:
        print(root.data)
        preTrav(root.leftChild)
        preTrav(root.rightChild)
        
def inTrav(oot):
    if not oot:
        return
    else:
        inTrav(oot.leftChild)
        print(oot.data)
        inTrav(oot.rightChild)
        
def postTrav(root):
    if not root:
        return
    else:
        postTrav(root.leftChild)
        postTrav(root.rightChild)
        print(root.data)
        
        
def levelTrav(root):
    if not root:
        return
    else:
        cusQ=queue.Queue()
        cusQ.enqueue(root)
        while not (cusQ.isEmpty()):
            roo=cusQ.dequeue()
            print(roo.data)
            if roo.leftChild is not None:
                cusQ.enqueue(roo.leftChild)
            if roo.rightChild is not None:
                cusQ.enqueue(roo.rightChild)
                

                
            
BST = BSTNode(None)
print(insert(BST,70))
print(insert(BST,60))
print(insert(BST,77))
print(insert(BST,87))
print(insert(BST,7))
print(insert(BST,43))
print(insert(BST,67))
print(insert(BST,234))

print(BST.data)
print(BST.leftChild.data)

print("\nPre:")
preTrav(BST)

print("\nIn:")
inTrav(BST)

print("\nPost:")
postTrav(BST)

print("\nLevel:")
levelTrav(BST)


