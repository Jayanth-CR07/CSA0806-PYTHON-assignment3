import time

# Nested dictionary containing train timetable details
timetable = {
    "Train101": {
        "train_name": "Chennai Express",
        "station": "Chennai",
        "day": "Monday",
        "departure": "06:30"
    },
    "Train102": {
        "train_name": "Bangalore Express",
        "station": "Chennai",
        "day": "Monday",
        "departure": "08:15"
    },
    "Train103": {
        "train_name": "Coimbatore Express",
        "station": "Salem",
        "day": "Monday",
        "departure": "07:45"
    },
    "Train104": {
        "train_name": "Madurai Express",
        "station": "Chennai",
        "day": "Tuesday",
        "departure": "09:00"
    },
    "Train105": {
        "train_name": "Mysore Express",
        "station": "Salem",
        "day": "Monday",
        "departure": "06:00"
    }
}

# Display the complete timetable
print("TRAIN TIMETABLE")
print("-" * 50)

for train_id, details in timetable.items():
    print(
        train_id,
        "|", details["train_name"],
        "|", details["station"],
        "|", details["day"],
        "|", details["departure"]
    )

# Search trains by station and day
search_station = input("\nEnter station: ").strip()
search_day = input("Enter day: ").strip()

matching_trains = []

for train_id, details in timetable.items():
    if (
        details["station"].lower() == search_station.lower()
        and details["day"].lower() == search_day.lower()
    ):
        matching_trains.append((train_id, details))

# Sort matching trains by departure time
matching_trains.sort(key=lambda item: item[1]["departure"])

print("\nMatching trains:")
if matching_trains:
    for train_id, details in matching_trains:
        print(
            train_id,
            "-", details["train_name"],
            "| Departure:", details["departure"]
        )
else:
    print("No trains found for the given station and day.")

# Measure search time
start = time.perf_counter()

for _ in range(10000):
    for details in timetable.values():
        if (
            details["station"].lower() == search_station.lower()
            and details["day"].lower() == search_day.lower()
        ):
            pass

search_time = time.perf_counter() - start

print("\nSearch performance:")
print("Time for 10000 searches:", search_time, "seconds")

# Create a station index for faster searching
station_index = {}

for train_id, details in timetable.items():
    key = (details["station"].lower(), details["day"].lower())
    station_index.setdefault(key, []).append((train_id, details))

start = time.perf_counter()

for _ in range(10000):
    indexed_results = station_index.get(
        (search_station.lower(), search_day.lower()), []
    )

index_time = time.perf_counter() - start

print("Time for 10000 indexed searches:", index_time, "seconds")

print("\nIndexed search results:")
for train_id, details in sorted(
    indexed_results, key=lambda item: item[1]["departure"]
):
    print(train_id, "-", details["train_name"], "|", details["departure"])

