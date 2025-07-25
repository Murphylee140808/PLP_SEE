def fibonacci_memo(n, memo={}):
    """Compute the nth Fibonacci number using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
print("Fibonacci numbers (with memoization):")
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_memo(i)}")