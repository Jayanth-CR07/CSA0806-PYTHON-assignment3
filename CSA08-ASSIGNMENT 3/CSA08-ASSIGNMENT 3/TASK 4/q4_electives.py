import time
import random

# Students registered for electives
ai_elective = {
    "192311001", "192311004",
    "192311007", "192311009"
}

iot_elective = {
    "192311002", "192311004",
    "192311009", "192311010"
}

all_students = {
    f"1923110{i:02d}"
    for i in range(1, 11)
}

# Find students in both electives
both = ai_elective & iot_elective

# Find students in exactly one elective
exactly_one = ai_elective ^ iot_elective

# Find students in neither elective
neither = all_students - (ai_elective | iot_elective)

print("clash      :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither    :", sorted(neither))

# Demonstrate set methods
print("\nUsing set methods:")
print("Intersection:", sorted(ai_elective.intersection(iot_elective)))
print("Symmetric difference:", sorted(ai_elective.symmetric_difference(iot_elective)))
print("Union:", sorted(ai_elective.union(iot_elective)))
print("Difference:", sorted(ai_elective.difference(iot_elective)))

# Test duplicate removal
registrations = [
    "192311001", "192311004",
    "192311001", "192311007"
]

unique_registrations = set(registrations)

print("\nOriginal registrations:", registrations)
print("Unique registrations:", sorted(unique_registrations))

# Compare membership testing in a list and a set
numbers = list(range(100000))
number_set = set(numbers)
target = 99999

start = time.perf_counter()
target in numbers
list_time = time.perf_counter() - start

start = time.perf_counter()
target in number_set
set_time = time.perf_counter() - start

print("\nMembership testing:")
print("List search time:", list_time)
print("Set search time:", set_time)

# Test empty and identical electives
empty_elective = set()

print("\nEmpty elective intersection:",
      sorted(ai_elective & empty_elective))

print("Identical elective intersection:",
      sorted(ai_elective & ai_elective))

