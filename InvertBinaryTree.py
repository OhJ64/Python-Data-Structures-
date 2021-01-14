
#Leet code python solution to invert a binary tree

def invertTree(self, root):
    while root is not None:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
