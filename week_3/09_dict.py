def put(self, key, value):
    index = hash(key) % len(self.items)
    self.items[index] = value

def get(self, key):
    index = hash(key) % len(self.items)
    return self.items[index]