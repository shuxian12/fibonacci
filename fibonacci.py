
def fibonacci(n : int):
    if n < -1:
        raise ValueError("Input cannot be negative")
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = 10
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")  