def max_weighted_celebs(intervals):
    events = []
    for start, end, weight in intervals:
        events.append((start, "arrival", weight))
        events.append((end, "departure", weight))


    events.sort(key=lambda x: (x[0], x[1] == "departure"))


    current_weight = 0
    max_weight = 0
    max_interval_start = 0
    active_celebs = []

    for time, event_type, weight in events:
        if event_type == "arrival":
            active_celebs.append((time, weight))  
            current_weight += weight
        elif event_type == "departure":

            active_celebs = [(t, w) for t, w in active_celebs if t >= time - 1]
            current_weight = sum(w for _, w in active_celebs)


        if current_weight > max_weight:
            max_weight = current_weight
            max_interval_start = time - 1

    return max_interval_start, max_interval_start + 1, max_weight



intervals = [
    (6, 7, 5),  # Beyonce
    (7, 9, 3),  # Taylor
    (10, 11, 1),  # Brad
    (10, 12, 2),  # Katy
    (8, 10, 4),  # Tom
    (9, 11, 6),  # Drake
    (6, 8, 7),  # Alicia
]

start_time, end_time, max_weight = max_weighted_celebs(intervals)
print(f"Visit {start_time} to {end_time} to maximize weight score of {max_weight}.")
