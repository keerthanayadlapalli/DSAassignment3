class SeparateChainingHashMap:
    def __init__(self, cap):
        self.capacity = cap
        self.size = 0
        self.table = [[] for _ in range(cap)]

    def hash(self, key):
        return key % self.capacity

    def insert(self, key, value):
        idx = self.hash(key)
        for kv in self.table[idx]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[idx].append([key, value])
        self.size += 1

    def find(self, key):
        idx = self.hash(key)
        for kv in self.table[idx]:
            if kv[0] == key:
                return True
        return False

    def remove(self, key):
        idx = self.hash(key)
        self.table[idx] = [kv for kv in self.table[idx] if kv[0] != key]
        self.size -= 1


hash_map = SeparateChainingHashMap(10)


hash_map.insert(1, 100)
hash_map.insert(2, 200)
hash_map.insert(11, 1100)  # Collision with key 1

print(hash_map.find(1))  # True
print(hash_map.find(2))  # True
print(hash_map.find(3))  # False

hash_map.remove(1)
print(hash_map.find(1))  # False
