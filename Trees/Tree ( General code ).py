class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add(self,data,parentdata = None):
        node = TreeNode(data)

        if not self.root:
            self.root = node
            return

        ParentNode = self.findNode(parentdata,self.root)

        if not ParentNode:
            print("ParentNode not found")
            return

        ParentNode.children.append(node)


    def findNode(self,data, node):
        if node.data == data:
            return node

        for child in node.children:
            nodefound = self.findNode(data,child)
            if nodefound : return nodefound

        return None

    def display(self,depth=0, node = None):
        if not node:
            node = self.root
        print(" "*depth,node.data)

        for child in node.children:
            self.display(depth+1,child)

    def remove(self, data):
        if not self.root:
            print("Tree is empty")
            return

        if self.root.data == data:
            self.root = None
            return

        ParentNode = self.findParentNode(data,self.root)

        if ParentNode:
            for child in ParentNode.children:
                if child.data == data:
                    ParentNode.children.remove(child)
                    return
        print("Node not found")

    def findParentNode(self,data,node):
        for child in node.children:
            if child.data == data:
                return node
            nodefound = self.findParentNode(data,child)
            if nodefound: # If nodefound is not None
              return nodefound  

        return None


tree = Tree()
tree.add(1)
tree.add(2,1)
tree.add(3,1)
tree.add('a',1)
tree.add(4,2)
tree.add(5,2)
tree.add(6,3)
tree.add(7,3)
tree.display()
tree.remove('a')
tree.display()
