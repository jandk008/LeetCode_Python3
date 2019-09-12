class DesignHashSet:
    def __init__(self):
        self.table = bytearray(10 ** 6)

    def add(self, key: int):
        self.table[key] = 1

    def remove(self, key: int):
        self.table[key] = 0

    def contains(self, key):
        return self.table[key] == 1
