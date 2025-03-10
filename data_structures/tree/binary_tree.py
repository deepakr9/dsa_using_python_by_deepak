# What is a Binary Tree?
# A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left and right child.
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):

        if not self.root:
            self.root = Node(data)
            return
        
        queue = [self.root]

        while queue:
            cur = queue.pop(0)
            if not cur.left:
                cur.left = Node(data)
                return
            else:
                queue.append(cur.left)
            
            if not cur.right:
                cur.right = Node(data)
                return
            else:
                queue.append(cur.right)
        
    def preorder_traversal(self, node):

        if node is None:
            return []
        return ([node.data]+self.preorder_traversal(node.left)+self.preorder_traversal(node.right))

    def inorder_traversal(self, node):

        if node is None:
            return []
        return (self.inorder_traversal(node.left)+[node.data]+self.inorder_traversal(node.right))
    
    def postorder_traversal(self, node):

        if node is None:
            return []
        return (self.postorder_traversal(node.left)+self.postorder_traversal(node.right)+[node.data])
    
    def level_traversal(self, node):
        if node is None:
            return []
        queue = [node]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.data)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result


    def size(self, node):
        if node is None:
            return 0
        return 1+self.size(node.left)+self.size(node.right)
    

    def height(self, node):
        if node is None:
            return 0
        
        return 1+max(self.height(node.left), self.height(node.right))

    def search(self, key):
        if self.root is None:
            return 
            
        queue = deque([self.root])

        while queue:

            cur = queue.popleft()

            if cur.data == key:
                return True

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)
        return False    

        
        
    def delete(self, key):

        if self.root is None:
            return 
        
        if self.root.data == key and not self.root.left and not self.root.right:
            self.root = None
            return 
        
        queue = deque([self.root])
        node_deleted = None
        deep_node = None
        while queue:
            current = queue.popleft()
            if current.data == key:
               node_deleted = current
            if current.left:
               queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        if node_deleted:

            deep_node = current
            node_deleted.data = deep_node.data
            self.__delete(deep_node)

    def __delete(self, node):
        queue = deque([self.root])

        while queue:
            cur = queue.popleft()

            if cur is node:
                cur = None
                return
            
            if cur.left:
                if cur.left is node:
                    cur.left = None
                    return
                            
                queue.append(cur.left)
            
            if cur.right:
                if cur.right is node:
                    cur.right = None
                    return
                            
                queue.append(cur.right)
            
    def btreeGameWinningMove(self, root, n, x) -> bool:
        # Find the subtree sizes using DFS
        def count_nodes(node):
            if not node:
                return 0
            left_size = count_nodes(node.left)
            right_size = count_nodes(node.right)
            if node.data == x:
                self.left_size = left_size
                self.right_size = right_size
            return 1 + left_size + right_size
        
        # Compute subtree sizes
        self.left_size = 0
        self.right_size = 0
        res = count_nodes(root)
        
        # Parent subtree size
        parent_size = n - (self.left_size + self.right_size + 1)
        
        # Check if the second player can control more than half the nodes
        max_control = max(self.left_size, self.right_size, parent_size)
        return max_control > n // 2


t1 = Tree()
t2 = Tree()
t1.insert(1)
t1.insert(2)
t1.insert(3)
t1.insert(4)
t1.insert(5)
t1.insert(6)
t1.insert(7)
t1.insert(8)
t1.insert(9)
t1.insert(10)
t1.insert(11)
print(t1.preorder_traversal(t1.root))
print(t1.btreeGameWinningMove(t1.root, 11, 2))