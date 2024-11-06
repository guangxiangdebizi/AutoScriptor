# ```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            next_value = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_value)
        return fib_seq
# ```
def main():
    # fibonacci(100)
    print(fibonacci(100))
main()