class HashTable:
    def __init__(self):
        self.bucket = 20
        self.hashmap = [[] for i in range(self.bucket)]

    def __str__(self):
        return str(self.__dict__)

    def hash(self,key):
        return len(key) % self.bucket

    def put(self,key,value):
        hash_value = self.hash(key)
        ref = self.hashmap[hash_value]
        for i in range(len(ref)):
            if ref[i][0] == key:
                ref[i][1] = value
                return None
        ref.append([key,value])
        return None

    def get(self,key):
        hash_value = self.hash(key)
        ref = self.hashmap[hash_value]
        for i in range(len(ref)):
            if ref[i][0] == key:
                return ref[i][1]

        return -1

    def remove(self,key):
        hash_value = self.hash(key)
        ref = self.hashmap[hash_value]
        for i in range(len(ref)):
            if ref[i][0] == key:
                ref.pop(i)
                return None
        return None

h=HashTable()
h.put('grapes',1000)
h.put('apples',10)
h.put('ora',300)
h.put('banan',200)
print(h.get('grapes'))
print(h)
h.remove('apples')
print(h)
