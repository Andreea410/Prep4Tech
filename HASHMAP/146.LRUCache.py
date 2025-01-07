class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.order = []  
        self.set_operations = set()

    def get(self, key: int) -> int:
        if key in self.map:
            if key in self.set_operations:
                self.order.remove(key)  
                self.set_operations.remove(key) 
            self.order.append(key)
            self.set_operations.add(key)
            return self.map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
           
            self.map[key] = value
            self.order.remove(key)
            self.set_operations.remove(key)
            self.order.append(key)
            self.set_operations.add(key)
        elif len(self.map) == self.capacity:
            key_to_remove = self.order.pop(0)  
            self.set_operations.remove(key_to_remove)
            del self.map[key_to_remove]
        
            self.map[key] = value
            self.order.append(key)
            self.set_operations.add(key)
        else:

            self.map[key] = value
            self.order.append(key)
            self.set_operations.add(key)

# Example usage:
# obj = LRUCache(capacity=2)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))  # Returns 1
# obj.put(3, 3)      # Removes key 2
# print(obj.get(2))  # Returns -1 (not found)
# obj.put(4, 4)      # Removes key 1
# print(obj.get(1))  # Returns -1 (not found)
# print(obj.get(3))  # Returns 3
# print(obj.get(4))  # Returns 4
