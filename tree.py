class Tree():
    def __init__(root,val, children = []):
        self.root = root
        self.val = val
        #each child is in the list
        self.children = children
        #Sum of all of nodes's values
        self.sum = 0

    def getVal(self):
        return self.val

    def getSum(self):
        return self.sum

    def getChildren(self):
        return self.children

    def deepSearch(self):
        pass
