class Solution():
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Inner Trie class definition
        class Trie:
            def __init__(self):
                self.children = {}
                self.is_end_of_word = False

        # Function to insert words into the Trie
        def insert(root, key):
            cur = root
            for char in key:
                if char not in cur.children:
                    cur.children[char] = Trie()
                cur = cur.children[char]
            cur.is_end_of_word = True

        # Function to search for the longest common prefix in the Trie
        def searchPrefix(root):
            prefix = []
            cur = root
            while cur and len(cur.children) == 1 and not cur.is_end_of_word:
                char = list(cur.children.keys())[0]
                prefix.append(char)
                cur = cur.children[char]
            return ''.join(prefix)

        # Initialize the Trie and insert all strings
        root = Trie()
        for word in strs:
            insert(root, word)

        # Return the longest common prefix found
        return searchPrefix(root)

