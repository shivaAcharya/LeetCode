class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]


    def add(self, node: ListNode) -> None:
        # 1 <=> 2 <=> Tail [Add 3]
        previous_end = self.tail.prev #2
        previous_end.next = node #2 -> 3
        node.prev = previous_end #2 <=> 3
        node.next = self.tail    #3 -> Tail
        self.tail.prev = node    #3 <=> Tail

    def remove(self, node: ListNode) -> None:
        # 1 <=> 2 <=> 3 <=> 4 [Remove 2]
        node.prev.next = node.next # 1 -> 3 <=> 4
        node.next.prev = node.prev # 1 <=> 3 <=> 4


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)