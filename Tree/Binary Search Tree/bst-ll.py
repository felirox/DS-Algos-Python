class BSTNode():
    def __init__(self,data):
        self.data = data
        self.leftChild=None
        self.rightChild=None

      
def insert(root,value):
        if root.data == None:
            root.data = value
        elif value<=root.data:
            if root.leftChild is None:
                root.leftChild ==BSTNode(value) #interesting
            else:
                insert(root.leftChild,value)
        else:
            if value>root.data:
                if root.rightChild == None:
                    root.rightChild == BSTNode(value)
                else:
                    insert(root.rightChild,value)
        return "Inserted successfully"
   

BST = BSTNode(None)


