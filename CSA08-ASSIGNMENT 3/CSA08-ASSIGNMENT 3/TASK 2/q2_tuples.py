import copy
import sys
import time

# Grid dimensions
rows, cols = 3, 4

# Incorrect grid: all rows refer to the same list
bad = [[0] * cols] * rows

bad[0][1] = 7

# TODO 1: Create separate rows using list comprehension
good = [[0] * cols for _ in range(rows)]

good[0][1] = 7

print("bad :", bad)
print("good:", good)

print(bad[0] is bad[1], good[0] is good[1])

# Tuples as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

# Aliasing
original = [[1, 2], [3, 4]]
alias = original

print("\nAliasing demonstration:")
print("Same object:", original is alias)

# Shallow copy
shallow = copy.copy(original)
slicing_copy = original[:]

# Deep copy
deep = copy.deepcopy(original)

# Modify an inner list
original[0][0] = 99

print("Original:", original)
print("Alias:", alias)
print("Shallow copy:", shallow)
print("Slicing copy:", slicing_copy)
print("Deep copy:", deep)

# Memory comparison
values_list = list(range(1000))
values_tuple = tuple(range(1000))

print("\nMemory comparison:")
print("List memory:", sys.getsizeof(values_list), "bytes")
print("Tuple memory:", sys.getsizeof(values_tuple), "bytes")

# Time creation of list and tuple
start = time.perf_counter()
list(range(100000))
list_creation_time = time.perf_counter() - start

start = time.perf_counter()
tuple(range(100000))
tuple_creation_time = time.perf_counter() - start

print("\nCreation time:")
print("List creation:", list_creation_time, "seconds")
print("Tuple creation:", tuple_creation_time, "seconds")

# Time indexing
test_list = list(range(100000))
test_tuple = tuple(range(100000))

start = time.perf_counter()
for i in range(10000):
    value = test_list[i]
list_index_time = time.perf_counter() - start

start = time.perf_counter()
for i in range(10000):
    value = test_tuple[i]
tuple_index_time = time.perf_counter() - start

print("\nIndexing time:")
print("List indexing:", list_index_time, "seconds")
print("Tuple indexing:", tuple_index_time, "seconds")

# Test a list inside a tuple
sample = ([10, 20], 30)

sample[0].append(40)

print("\nTuple containing a list:", sample)

# Test whether a list can be a dictionary key
try:
    example = {[13.0418, 80.2341]: "T. Nagar"}
except TypeError as error:
    print("\nList dictionary key error:", error)

