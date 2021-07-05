

class Correctness:
    def __init__(self, ds, insert, remove):
        self.itemsToInsert = 3000
        self.ds = ds(self.itemsToInsert)
        self.insertDs = getattr(self.ds, insert)
        self.removeDs = getattr(self.ds, remove)



        self.insert()
        self.remove()
        if not self.ds.is_empty():
            print("ERROR: Data structure is not empty")

    def insert(self):
        for i in range(self.itemsToInsert):
            self.insertDs(i)

    def remove(self):
        for i in range(self.itemsToInsert):
            removed = self.removeDs(i)
            if not removed:
                print("ERROR: Unable to remove node")



