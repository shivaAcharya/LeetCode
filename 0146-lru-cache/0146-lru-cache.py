class Node:
    
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev    
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node
        self.head = Node(-1, -1) #LRU
        self.tail = Node(-1, -1) #MRU
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)
        
        if len(self.cache) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.cache[node_to_delete.key]
        
    
    def add(self, node):
        # 1 <=> 2 <=> Tail [Add 3]
        prev_end = self.tail.prev #2
        prev_end.next = node # 2 -> 3
        node.prev = prev_end # 2 <=> 3
        node.next = self.tail # 3 -> Tail
        self.tail.prev = node # 3 <=> Tail
    
    
    def remove(self, node):
        # 1 <=> 2 <=> 3 <=> 4 [Remove 2]
        node.prev.next = node.next
        node.next.prev = node.prev

    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)