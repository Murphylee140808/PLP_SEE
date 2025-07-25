import itertools

elements = ['a', 'b', 'c', 'd']
# elements = [1, 2, 3]

# All permutations of the list:
# permutations = list(itertools.permutations(elements))
# print("Permutations of 3 Alphabets: ", permutations)
# print("Permutations of 3 Numbers: ", permutations)

combinations = list(itertools.combinations(elements, 2))
print("Combinations of the 3 Alphabets: ", combinations)
# print("Combinations of the 3 numbers: ", combinations)