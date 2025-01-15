class TreeNode:
    def __init__(self, value):
        self.value = value
        self.child = []

    def insert(self, child):
        self.child.append(child)

    def print_tree(self):
        print(self.value)
        if self.child:
            for c in self.child:
                c.print_tree()

def build_tree():
    lap = TreeNode('people')
    people1 = TreeNode('Deepak')
    people1.insert(TreeNode('appu'))
    people2 = TreeNode('Dhanush')
    people2.insert(TreeNode('dhani'))
    lap.insert(people1)
    lap.insert(people2)
    return lap


if __name__ == '__main__':
    res = build_tree()
    res.print_tree()