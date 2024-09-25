# implement hash function 

def get_hash(key):
    h= 0
    for char in key:
        h+=ord(char)
    return h % 100

#create class

class HashTable():
    def __init__(self):
        self.Max =100
        self.arr = [None for i in range(self.Max)]


    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.Max 