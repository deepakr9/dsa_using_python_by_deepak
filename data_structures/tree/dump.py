def preorder_insert(self, data):
    def help():
        nonlocal idx
        if idx >= len(data) or data[idx] == -1:
            idx += 1
            return None
            
        cur = Node(data[idx])
        
        idx += 1
        cur.left = help()
        cur.right = help()

        return cur
    idx = 0
    self.root =  help()
    return self.root.right.data