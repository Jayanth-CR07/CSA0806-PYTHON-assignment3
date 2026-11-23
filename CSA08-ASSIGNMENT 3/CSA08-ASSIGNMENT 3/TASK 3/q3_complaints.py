import time
import random
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}


# Count word frequencies using a dictionary
def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().split()

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


# Find the top k frequent words
def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]


# Group complaints by district
def group_by_district(complaints):
    districts = {}

    for complaint in complaints:
        district = complaint["district"]

        districts.setdefault(district, []).append(
            complaint["text"]
        )

    return districts


# Count complaints by crop
def group_by_crop(complaints):
    crops = {}

    for complaint in complaints:
        crop = complaint["crop"]

        crops.setdefault(crop, []).append(
            complaint["text"]
        )

    return crops


# Main program
word_counts = frequencies(calls, STOP)

print("Word frequencies:", word_counts)
print("Top 3 words:", top(word_counts, 3))


# Sample complaint records
complaints = [
    {
        "district": "Chennai",
        "crop": "Rice",
        "text": "Seeds not received"
    },
    {
        "district": "Madurai",
        "crop": "Wheat",
        "text": "Fertiliser price high"
    },
    {
        "district": "Chennai",
        "crop": "Rice",
        "text": "Seeds delayed"
    },
    {
        "district": "Salem",
        "crop": "Cotton",
        "text": "Water supply problem"
    }
]

print("\nComplaints by district:")
print(group_by_district(complaints))

print("\nComplaints by crop:")
print(group_by_crop(complaints))


# Compare dictionary counting and Counter
large_calls = calls * 1000

start = time.perf_counter()
dictionary_result = frequencies(large_calls, STOP)
dictionary_time = time.perf_counter() - start

start = time.perf_counter()
counter_result = Counter(
    word
    for text in large_calls
    for word in text.lower().split()
    if word not in STOP
)
counter_time = time.perf_counter() - start

print("\nDictionary counting time:", dictionary_time)
print("Counter counting time:", counter_time)
print(
    "Both methods agree:",
    dictionary_result == dict(counter_result)
)

