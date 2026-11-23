import time
import sys

# Sensor readings in Celsius
readings = [25, 30, -999, 35, 40, -999, 28, 50, 32, 100]

# 1. Remove invalid readings using list comprehension
cleaned_readings = [
    value for value in readings
    if value != -999 and 0 <= value <= 60
]

print("Original sensor readings:", readings)
print("Cleaned sensor readings:", cleaned_readings)

# 2. Convert Celsius to Fahrenheit using list comprehension
fahrenheit = [
    (value * 9 / 5) + 32
    for value in cleaned_readings
]

print("\nTemperature in Fahrenheit:", fahrenheit)

# 3. Find readings above 35°C
high_temperatures = [
    value for value in cleaned_readings
    if value > 35
]

print("\nHigh temperature readings:", high_temperatures)

# 4. Count alarm readings
alarm_count = len(high_temperatures)

print("Number of alarm readings:", alarm_count)

# 5. Compare loop and list comprehension performance
large_readings = list(range(100000))

start = time.perf_counter()
loop_result = []
for value in large_readings:
    if value % 2 == 0:
        loop_result.append(value)
loop_time = time.perf_counter() - start

start = time.perf_counter()
comprehension_result = [
    value for value in large_readings
    if value % 2 == 0
]
comprehension_time = time.perf_counter() - start

print("\nPerformance comparison:")
print("Loop time:", loop_time, "seconds")
print("List comprehension time:", comprehension_time, "seconds")
print("Results are equal:", loop_result == comprehension_result)

# 6. Compare map() and filter()
start = time.perf_counter()
map_result = list(map(lambda x: x * 2, large_readings))
map_time = time.perf_counter() - start

start = time.perf_counter()
filter_result = list(filter(lambda x: x % 2 == 0, large_readings))
filter_time = time.perf_counter() - start

print("\nMap and filter comparison:")
print("Map time:", map_time, "seconds")
print("Filter time:", filter_time, "seconds")

# 7. Compare memory size of list and generator
square_list = [x * x for x in range(1000)]
square_generator = (x * x for x in range(1000))

print("\nMemory comparison:")
print("List memory:", sys.getsizeof(square_list), "bytes")
print("Generator memory:", sys.getsizeof(square_generator), "bytes")

# 8. Edge cases
empty_readings = []
empty_cleaned = [
    value for value in empty_readings
    if value != -999 and 0 <= value <= 60
]

print("\nEmpty input result:", empty_cleaned)

invalid_readings = [-999, -10, 100, -999]
invalid_cleaned = [
    value for value in invalid_readings
    if value != -999 and 0 <= value <= 60
]

print("All-invalid input result:", invalid_cleaned)

