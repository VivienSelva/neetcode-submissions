class MyHashMap:
    def __init__(self):
        self.tab = []

    def put(self, key: int, value: int) -> None:
        for t in self.tab:
            if t[0] == key:
                t[1] = value
                return

        self.tab.append([key, value])

    def get(self, key: int) -> int:
        for t in self.tab:
            if t[0] == key:
                return t[1]

        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.tab)):
            if self.tab[i][0] == key:
                self.tab.pop(i)
                return
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)