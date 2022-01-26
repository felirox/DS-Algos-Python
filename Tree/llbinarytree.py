import queuelinkedlist as queue


class TreeNode:
    def __init__(self, data):
        self.leftChild = None
        self.data = data
        self.rightChild = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot Drinks")
rightChild = TreeNode("Cold Drinks")
Tea = TreeNode("Tea")
Coffee = TreeNode("Coffee")
Cola = TreeNode("Cola")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftChild.leftChild = Tea
leftChild.rightChild = Coffee
rightChild.leftChild = Cola


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# print("\nPre:")
# preOrderTraversal(newBT)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

    # print(rootNode.data)
# print("\nIn:")
# inOrderTraversal(newBT)


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)


# print("\nPost:")
# postOrder(newBT)


def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        cusQ = queue.Queue()
        cusQ.enqueue(rootNode)
        while not(cusQ.isEmpty()):
            root = cusQ.dequeue()
            print(root.data)
            if (root.leftChild is not None):
                cusQ.enqueue(root.leftChild)
            if(root.rightChild is not None):
                cusQ.enqueue(root.rightChild)


# print("*****************")

# levelOrder(newBT)


def searchBT(rootNode, nodeVal):
    if not rootNode:
        return
    else:
        cusQ = queue.Queue()
        cusQ.enqueue(rootNode)
        while not(cusQ.isEmpty()):
            root = cusQ.dequeue()
            if str(root.data) == nodeVal:
                return "Value found"
            if(root.leftChild is not None):
                cusQ.enqueue(root.leftChild)
            if(root.rightChild is not None):
                cusQ.enqueue(root.rightChild)

        return "Not Found"


# print("~~~~~~~~~~~~~~~~~~~")
# print(searchBT(newBT, "Cosffee"))


def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        cusQ = queue.Queue()
        cusQ.enqueue(rootNode)
        while not (cusQ.isEmpty()):
            root = cusQ.dequeue()
            if root.leftChild is not None:
                cusQ.enqueue(root.leftChild)
            else:
                root.leftChild = newNode
                return "New Node successfully inserted at LC"
            if root.rightChild is not None:
                cusQ.enqueue(root.rightChild)
            else:
                root.rightChild = newNode
                return "New Node successfully inserted at RC"


# newNode = TreeNode("Diet Cola")
# insertNode(newBT, newNode)

# print("*****************")

# preOrderTraversal(newBT)


def deepNode(rootNode):
    if not rootNode:
        return
    else:
        cusQ = queue.Queue()
        cusQ.enqueue(rootNode)
        while not cusQ.isEmpty():
            root = cusQ.dequeue()
            if root.leftChild is not None:
                cusQ.enqueue(root.leftChild)

            if root.rightChild is not None:
                cusQ.enqueue(root.rightChild)
        deepNode = root

    return deepNode  # Memory Location


# print("sdas")
# preOrderTraversal(newBT)
# print("Deepests")
deepestNode = deepNode(newBT)


def delDeepNode(rootNode, deepNode):
    if not rootNode:
        return
    else:
        cusQ = queue.Queue()
        cusQ.enqueue(rootNode)
        while not cusQ.isEmpty():
            root = cusQ.dequeue()
            if root == deepNode:
                # print("baap")
                root = None
                return
            if root.rightChild:
                if root.rightChild is deepNode:
                    # print("baap")
                    root.rightChild = None
                    return
                else:
                    cusQ.enqueue(root.rightChild)
            if root.leftChild:
                if root.leftChild is deepNode:
                    # print("baap")
                    root.leftChild = None
                    return
                else:
                    cusQ.enqueue(root.leftChild)

# preOrderTraversal(newBT)
# print(deepestNode)
# delDeepNode(newBT,deepestNode)
# print("*****************")

# preOrderTraversal(newBT)


def deleteNode(rootNode, node):
    if not rootNode:
        return "BT does not exist"
    else:
        cusQ = queue.Queue()
        cusQ.enqueue(rootNode)
        while not(cusQ.isEmpty()):
            root = cusQ.dequeue()
            if root.data == node:
                dNode = deepNode(rootNode)
                root.data = dNode.data
                delDeepNode(rootNode, dNode)
                return "Node Successfully Deleted"
            if root.leftChild is not None:
                cusQ.enqueue(root.leftChild)
            if root.rightChild is not None:
                cusQ.enqueue(root.rightChild)
        return "Failed to delete"


levelOrder(newBT)
print(deleteNode(newBT, "Drinks"))
levelOrder(newBT)


def deletewholeBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "This was probably the easiest. Typical life shit"


deletewholeBT(newBT)
print("Dellll out")
levelOrder(newBT)
