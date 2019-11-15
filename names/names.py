import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                tree = self.left
                tree.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                tree = self.right
                tree.insert(value)
    
    def multi_insert(self, lst):
        for x in lst:
            self.insert(x)
    
    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value:
                if self.left is None:
                    return False
                else:
                    tree = self.left
            else:
                if self.right is None:
                    return False
                else:
                    tree = self.right
            return tree.contains(target)

    def duplicates(self, lst):
        for x in lst:
            if self.contains(x):
                if x not in duplicates:
                    duplicates.append(x)
        

pineTree = Tree(" ")
pineTree.multi_insert(names_1)
pineTree.duplicates(names_2)

#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")

#print (f"runtime: {end_time - start_time} seconds")
#for x in duplicates:
#    if x in names_1:
#        print(f"{x} in names_1")
#    else:
#        print(f"{x} not in names_1")
#    if x in names_2:
#       print(f"{x} in names_2")
#    else:
#        print(f"{x} not in names_2")
