class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # LRU
        self.right = Node(0, 0)  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    # Insert a node at the MRU position (right before self.right)
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = node
        node.prev = prv
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove the LRU node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
































# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap=capacity
#         self.cache={}
#         self.left , self.right = Node(0,0) , Node(0,0)
#         self.left.next=self.right
#         self.right.prev=self.left

#     def remove(self,node):
#         prv,nxt=node.prev,node.next
#         prv.next=nxt
#         nxt.prev=prev
    
#     def insert(self,node):
#         prv,nxt=self.right.prev , self.right
#         prv.next=node
#         node.prev , node.next=prv , nxt
#         nxt.prev=node


#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key]=Node(key,value)
#         self.insert(self.cache[key])
#         if len(self.cache)>self.cap:
#             lru=self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]
