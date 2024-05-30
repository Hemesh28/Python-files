#Down Up Solution -> O(N)
# def fibonacci_memo(n, memo=None):
#     if memo is None:
#         memo = {}
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
#     return memo[n]

# print(fibonacci_memo(999))  # Output: 55


def fibonacci_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibonacci_tab(20577))  # Output: 55