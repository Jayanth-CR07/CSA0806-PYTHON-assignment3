import random
import time

# Generate rainfall readings for 365 days
readings = [random.randint(0, 100) for _ in range(365)]

# Calculate weekly rainfall totals
weekly_totals = []

for i in range(0, len(readings), 7):
    weekly_totals.append(sum(readings[i:i + 7]))

print("Total number of readings:", len(readings))
print("Weekly rainfall totals:", weekly_totals)

# Find maximum rainfall
max_rainfall = max(readings)
print("\nMaximum rainfall:", max_rainfall)
print("Wettest day:", readings.index(max_rainfall) + 1)

# Find minimum rainfall
min_rainfall = min(readings)
print("Minimum rainfall:", min_rainfall)
print("Driest day:", readings.index(min_rainfall) + 1)

# Naive moving average
def naive_average(data):
    if len(data) < 7:
        return []

    result = []

    for i in range(len(data) - 6):
        average = sum(data[i:i + 7]) / 7
        result.append(average)

    return result

# Running-sum moving average
def running_average(data):
    if len(data) < 7:
        return []

    result = []
    current_sum = sum(data[:7])
    result.append(current_sum / 7)

    for i in range(7, len(data)):
        current_sum = current_sum + data[i] - data[i - 7]
        result.append(current_sum / 7)

    return result

# Calculate moving averages
naive_result = naive_average(readings)
running_result = running_average(readings)

print("\nFirst 5 moving averages:", running_result[:5])

# Find dry days (0 mm rainfall)
dry_days = []

for i, value in enumerate(readings):
    if value == 0:
        dry_days.append(i + 1)

print("Dry days:", dry_days)

# Compare execution times
start = time.perf_counter()
naive_average(readings)
naive_time = time.perf_counter() - start

start = time.perf_counter()
running_average(readings)
running_time = time.perf_counter() - start

print("\nNaive execution time:", naive_time)
print("Running-sum execution time:", running_time)

# Test empty and short lists
print("\nEmpty list test:", running_average([]))
print("Short list test:", running_average([10, 20, 30]))

# Verify both methods produce the same result
print(
    "Both methods give the same result:",
    all(abs(a - b) < 1e-9 for a, b in zip(naive_result, running_result))
)

