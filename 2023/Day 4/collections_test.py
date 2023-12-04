from collections import Counter

# Define two tuples with some matching and duplicate values
tuple1 = (1, 2, 3, 4, 4, 5)
tuple2 = (4, 5, 5, 6, 7, 8)

# Use Counter to count occurrences in each tuple
counter1 = Counter(tuple1)
counter2 = Counter(tuple2)

# Find the common values by taking the intersection of Counters
common_counter = counter1 & counter2

# Convert the result back to a list if needed
result_list = list(common_counter.elements())

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Common values:", result_list)
