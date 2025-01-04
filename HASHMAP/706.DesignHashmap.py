class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        found = False
        for i in range(0,len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap[i][1] = value
                found = True
        if not found:
            self.hashmap.append([key,value])

    def get(self, key: int) -> int:
        for i in range(0,len(self.hashmap)):
            if self.hashmap[i][0] == key:   
                return self.hashmap[i][1]
        return -1   

    def remove(self, key: int) -> None:
        for i in range(0,len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap.remove([self.hashmap[i][0],self.hashmap[i][1]])
                break
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
