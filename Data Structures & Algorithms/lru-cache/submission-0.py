class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.cap = capacity
        self.map = {}  # key -> Node

        # Dummy (sentinel) head/tail to avoid edge-case checks
        self.head = Node(0, 0)  # MRU side
        self.tail = Node(0, 0)  # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- Doubly linked list helpers ---
    def _remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add_to_front(self, node: Node) -> None:
        # insert right after head
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def _pop_lru(self) -> Node:
        # real LRU is node right before tail
        lru = self.tail.prev
        self._remove(lru)
        return lru

    # --- API ---
    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node:
            node.val = value
            self._move_to_front(node)
            return

        new_node = Node(key, value)
        self.map[key] = new_node
        self._add_to_front(new_node)

        if len(self.map) > self.cap:
            lru = self._pop_lru()
            del self.map[lru.key]