import time

calls = 0

def fibonacci(n):
    global calls
    calls += 1

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number: "))

start = time.perf_counter()
result = fibonacci(n)
end = time.perf_counter()

print("Original Fibonacci Program")
print("Fibonacci result:", result)
print("Function calls:", calls)
print("Execution time:", end - start, "seconds")

