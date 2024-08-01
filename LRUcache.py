class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def _move_to_front(self, key: int):
        if key in self.order:
            self.order.remove(key)
        self.order.insert(0, key)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._move_to_front(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self._move_to_front(key)
        else:
            if len(self.cache) == self.capacity:
                lru_key = self.order.pop()
                del self.cache[lru_key]
            self.cache[key] = value
            self.order.insert(0, key)
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))  # Output: 1

cache.put(3, 3)
print(cache.get(2))  # Output: -1

cache.put(4, 4)
print(cache.get(1))  # Output: -1

print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4
