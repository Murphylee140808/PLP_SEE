# Simple Explanation:
#Instead of adding all numbers at once, recursion breaks the problem into:
#"Add the first number"
#"Then add the sum of the rest"
#If you have a list like [1, 2, 3, 4], the recursive sum works like this:

# sum([1, 2, 3, 4]) 
# = 1 + sum([2, 3, 4])
# = 1 + 2 + sum([3, 4])
# = 1 + 2 + 3 + sum([4])
# = 1 + 2 + 3 + 4 + sum([])
# = 1 + 2 + 3 + 4 + 0
# = 10

# def sum_n(n):
#     """Return the sum of the first n natural numbers."""
#     if n == 0:
#         return 0
#     else:
#         return n + sum_n(n - 1)
    
#     # Test the recursive sum against the formula: n(n+1)/2
#     for i in range(1, 11):
#         recur_sum = sum_n(i)
#         formula_sum = i * (i + 1) //2
#         print (f"n = {i}: Recursive Sum = {recur_sum}, Formula Sum = {formula_sum}")

def sum_n(n):
 """Return the sum of the first n natural numbers using recursion."""
 if n == 0:
   return 0
 else:
   return n + sum_n(n - 1)

# Test the recursive sum against the formula: n(n+1)/2

for i in range(1, 11):
   recursive_sum = sum_n(i)
   formula_sum = i * (i + 1) // 2
   print(f"n = {i}: Recursive Sum = {recursive_sum}, Formula Sum = {formula_sum}")