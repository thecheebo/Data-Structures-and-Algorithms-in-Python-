INITIAL_CAPACITY = 20

class HashTable:

    def __init__(self):
        self.max_length = INITIAL_CAPACITY
        self.max_load_factor = 0.75
        self.length = 0
        self.table = [None] * self.max_length

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        self.length += 1
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.length -= 1
                break
            index = self._increment_key(index)
        tuple = (key, value)
        self.table[index] = tuple
        if self.length / float(self.max_length) >= self.max_load_factor:
            self._resize()

    def __getitem__(self, key):
        index = self._find_item(key)
        return self.table[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self.table[index] = None

    def _hash(self, key):
        # TODO more robust
        return hash(key) % self.max_length

    def _increment_key(self, key):
        return (key + 1) % self.max_length

    def _find_item(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            raise KeyError
        if self.table[index][0] != key:
            original_key = index
            while self.table[index][0] != key:
                index = self._increment_key(index)
                if self.table[index] is None:
                    raise KeyError
                if index == original_key:
                    raise KeyError
        return index

    def _resize(self):
        self.max_length *= 2
        self.length = 0
        old_table = self.table
        self.table = [None] * self.max_length
        for tuple in old_table:
            if tuple is not None:
                self[tuple[0]] = tuple[1]

a = HashTable()
a.__setitem__("card","bard")
a.__setitem__("card", "car")
a.__setitem__("fable", "table")
a.__setitem__("basil", "cat")
a.__setitem__("card1", "car")
a.__setitem__("fable1", "table")
a.__setitem__("basil1", "cat")
a.__setitem__("card2", "car")
a.__setitem__("fable2", "table")
a.__setitem__("basil2", "cat")
a.__setitem__("card3", "car")
a.__setitem__("fable3", "table")
a.__setitem__("card5","bard")
a.__setitem__("card6", "car")
a.__setitem__("fable5", "table")
a.__setitem__("basil4", "cat")
a.__setitem__("card17", "car")
a.__setitem__("fable8", "table")
a.__setitem__("basil9", "cat")
a.__setitem__("card0", "car")
a.__setitem__("fable245", "table")
a.__setitem__("basil45", "cat")
a.__setitem__("card43", "car")
a.__setitem__("fable35", "table")
