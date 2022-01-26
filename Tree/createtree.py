
class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
        
    def __str__(self,level=0):
        ret = "  "*level +str(self.data) +"\n"
        for child in self.children:
            ret+= child.__str__(level+1)
        return ret
        
    def addChild(self,TreeNode):
        self.children.append(TreeNode)
  
tree = TreeNode('Drinks',[])

#print(tree)

cold = TreeNode('Cold Drinks',[])
hot = TreeNode('Hot Drinks',[])
tree.addChild(cold)
tree.addChild(hot)

# ~*~

tea = TreeNode('Tea',[])
coffee = TreeNode('Coffee',[])
cola = TreeNode('Cola',[])
fanta = TreeNode('Fanta',[])
cold.addChild(fanta)
cold.addChild(cola)
hot.addChild(coffee)
hot.addChild(tea)

print(tree)