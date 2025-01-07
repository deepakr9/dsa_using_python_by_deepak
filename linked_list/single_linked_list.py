class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, index, data):
        new_node = Node(data)
        coun = self.count()
        if index < 0 or index > coun:
            print('index out of bound')
            return

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        count = 0
        temp = self.head
        while temp and count < index-1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node
        
    def delete(self, key):
        if self.head is None:
            return 0
        temp = self.head
    #if head contains the data
        if self.head.data == key:
            self.head = self.head.next
            return
    # searching through the list
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
    # key not in the list
        if not temp:
            print('not found')
            return
    # deleting the node
        prev.next = temp.next

    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print('None')

    def count(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    def make_cycle(self):
        i = 2
        current = self.head
        while i > 0:
            current = current.next
            i -= 1
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = current

    def detect_cycles(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def nth_from_end(self, n):
        fast, slow = self.head, self.head
        for _ in range(n):
            if not fast:
                return False
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.data
    
    def list_insertion(self, l):
        for item in l:
            self.insert(item)

    # merging two linked list in sorted order 
    def merge(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data > l2.data:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        tail.next = l1 or l2

        return dummy.next

    # Middle of the Linked List
    def middle(self):
        if self.head is None:
            return
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow.data

    # Removing Duplicates
    def remove_duplicates(self):
        seen = set()
        seen.add(self.head.data)
        current = self.head
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next  

    # rotate linked list imp
    def rotate(self, val):
        if not self.head or not self.head.next or val == 0:
            return
        count = self.count()
        n = val % count
        cur = self.head
        if n == 0:
            return 
        for _ in range(count-n-1):
            cur = cur.next
        
        new_head = cur.next
        temp = new_head
        cur.next = None
        while temp.next:
            temp = temp.next
        temp.next = self.head
        self.head = new_head

    # K-Reverse Linked List
    def k_reverse(self, n):
        
        if self.head is None or n == 0:
            return 
        cur = self.head

        prev_tail = None
        new_head = None

        while cur:

            group_head = cur
            prev = None
            count = 0
            while cur and count < n:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
                count += 1
            
            if not new_head:
                new_head = prev
            
            if prev_tail:
                prev_tail.next = prev 
                 
            prev_tail = group_head
        self.head = new_head











l1 = Linkedlist()
l2 = Linkedlist()
l1.list_insertion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
l1.display()
l1.k_reverse(3)

l1.display()
