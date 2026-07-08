class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail 
        self.tail.prev = self.head

        self.fmap = {}
        self.capacity = capacity

    def printLL(self):
        temp = []

        demo = self.head 

        while demo:
            temp.append((demo.key, demo.val))
            demo = demo.next 

        print(temp)

    def _delete_node(self, node):
        prev_node = node.prev 
        prev_node.next = node.next 
        node.next.prev = prev_node

    def _insert_at_start(self, node):
        temp = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        temp.prev = node 
        node.next = temp

    def _move_node_to_front(self, node):
        # delete node from its position
        self._delete_node(node)

        # insert node after head 
        self._insert_at_start(node)
        

    def get(self, key: int) -> int:
        if not key in self.fmap: return -1

        # move recently used to front
        node_to_move = self.fmap[key]
        if node_to_move.prev.val == -1: # node already in front 
            return self.fmap[key].val

        self._move_node_to_front(node_to_move)
        return self.fmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.fmap: self._delete_node(self.fmap[key])
        new = Node(key, value)
        self.fmap[key] = new 

        # insert into DLL
        self._insert_at_start(new)

        # if capacity increases 
        if len(self.fmap) > self.capacity:
            node_to_delete = self.tail.prev 
            del self.fmap[node_to_delete.key]

            node_to_delete.prev.next = self.tail 
            self.tail.prev = node_to_delete.prev


        
