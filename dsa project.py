class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)  #dumby head node

    def __len__(self):
        count = 0
        a = self.head
        while a.next is not None:
            count +=1
            a = a.next
        return count

    def move_to_end(self, key):
        a = self.head
        while a.next is not None and a.next.key != key:
            a = a.next

        if a.next is not None:
            # Remove the node from its current position
            node_to_move = a.next
            a.next = a.next.next

            # Move the node to the end
            a = self.head
            while a.next is not None:
                a = a.next
            a.next = node_to_move
            node_to_move.next = None

    def get(self, key):
        a = self.head
        while a.next is not None and a.next.key != key:
            a = a.next
        if a.next is not None:
            val = a.next.value
            self.move_to_end(key)
            return val
        return -1
        

    def put(self, key, value):
        a = self.head
        while a.next is not None and a.next.key != key:
            a = a.next
        if a.next is not None:
            # Update the value and move the node to the end
            a.next.value = value
            self.move_to_end(key)
            return
        
        if len(self) >= self.capacity:
            # Remove the least recently used node (head's next)
            self.head.next = self.head.next.next

        # Add a new node to the end
        new_node = Node(key, value)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = new_node

    def traverse(self):
        current = self.head.next
        while current.next is not None:
            print(f"({current.key}, {current.value})", end = ", ")
            current = current.next
        print(f"({current.key}, {current.value})")


lru = LRUCache(6)
lru.put(1, 1)
lru.put(2,2)
lru.put(3,3)
lru.get(3)
lru.put(1,5)
# print(lru.get(1))
lru.traverse()
# lru.put(2, 2)
# lru.traverse()
# print(lru.get(1))
# lru.traverse()
# lru.put(3, 3)
# lru.traverse()
# print(lru.get(2))
# lru.put(4, 4)
# lru.traverse()
# print(lru.get(1))
# print(lru.get(3))
# lru.traverse()
# print(lru.get(4))