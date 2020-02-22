
# Big-O time complexity of O(n)
hash_table = [[] for i in range(1024)]


# Big-O time complexity of O(1)
def insert(key, value):
    index = key % 40
    hash_table[index].append(value)


# Big-O time complexity of O(1)
def get(key):
    index = key % 40
    return hash_table[index][0]
