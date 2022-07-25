from collections import ChainMap

first = {1: 1, 2: 2, 3: 3}
second = {4: 4, 5: 5}

chain = ChainMap(first, second)
print(chain)
print(5 in chain)
