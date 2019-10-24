def recur_sum(n):
    """Function to return the sum
    of natural numbers using recursion"""

    if n <= 1:
        return n

    else:
        return n + recur_sum(n-1)

print(recur_sum(10))
