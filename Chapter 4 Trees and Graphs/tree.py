class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def addChild(self, child):
        child.parent = self;
        self.children.append(child)
        
    def print_tree(self):
        print(self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = TreeNode("Eletronics")
    laptop = TreeNode("Laptop")
    mobile = TreeNode("Mobile")
    root.addChild(laptop)
    root.addChild(mobile)
    laptop.addChild(TreeNode("Mac"))
    mobile.addChild(TreeNode("IPhone"))
    return root
    
    
if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
    

