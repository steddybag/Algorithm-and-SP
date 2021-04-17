from itertools import permutations

a = set()
a |= set(i for i in range(10))
print(permutations([1,2,3],2))
print(list(permutations([1,2,3],2)))
