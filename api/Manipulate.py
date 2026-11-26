if __name__ == "__main__":
    import Terminal as t
else:
    from . import Terminal as t

class Flexlist():
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        id0 = key[0]
        if len(key) == 1:
            return self.data[id0]
        else:
            id1 = key[1]
            return self.data[id0][id1]
        
    def __eq__(self, other):
        if isinstance(other, Flexlist):
            return self.data == other.data
        else:
            return self.data == other

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)-1

    def __setitem__(self, key, value):
        key0 = key[0]
        key1 = key[1]
        self.data[key0][key1] = value

    def __delitem__(self, key):
        if key == "links":
            t.error(f"tried to delete metadata 'links' in Flexlist")
        else:
            del self.data[key]

    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        pass