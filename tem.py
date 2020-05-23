class node:
    def __init__(self, data):
        self.data = data                                     #node constructor
        self.left = self.right = None
    def __str__(self):
        return(str(self.data))                          #for overriding print method

class tree(node):
    def __init__(self):                                  #root initialization
        self.root = None
    
    def add(self, data):
        if not self.root:
            self.root = node(data)                  #addition of data into tree (on root)
        else:
            self._add(self.root, data)

    def _add(self, start, data):
                                                        # recursive e=method to find the position to add node
        if data != start.data:
            if data < start.data:
                if not start.left:
                    start.left = node(data)
                else:
                    self._add(start.left, data)
            else:
                if not start.right:
                    start.right = node(data)
                else:
                    self._add(start.right, data)
        else:
            print(data,"/*- already in tree")
    def __str__(self):
        return str(self._print(self.root, ""))                #overriding print method
    
    def _print(self, start, out):
        if start:
            out += str(start.data) + "-"
            out = self._print(start.left, out)
            out = self._print(start.right, out)                   #preorder traversal of binary tree recursive method
        return out
    
Tree_1 = tree()
l1 = list(map(int,input().split()))
for i in l1:
    Tree_1.add(i)
print(str(Tree_1)[:-1])