class MyHashMap:

    def __init__(self):
        self.l=[]
        self.l2=[]

    def put(self, key: int, value: int) -> None:
        if key not in self.l:
            self.l.append(key)
            self.l2.append(value)
        else:
            for i in range(len(self.l)):
                if self.l[i]==key:
                    self.l2[i]=value
        

    def get(self, key: int) -> int:
        for i in range(len(self.l)):
            if self.l[i]==key:
                return self.l2[i]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.l:
            for i in range(len(self.l)):
                if self.l[i]==key:
                    self.l.remove(self.l[i])
                    del self.l2[i]
                    break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)