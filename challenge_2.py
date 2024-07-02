# Challenge 2

from math import gcd
from functools import reduce

def count_color_subsets(array):
    # Count the quantity of each color
    color_counts = {'r': 0, 'b': 0, 'g': 0}
    for color in array:
        if color in color_counts:
            color_counts[color] += 1

    # Calculate the DCM of the quantities of each color.
    counts = list(color_counts.values())
    overall_gcd = reduce(gcd, counts)

    # Verify if it can be divided into equal subsets
    if overall_gcd == 0:
        return 0

    return overall_gcd







# Tests - KO
print(count_color_subsets(['r', 'r', 'b', 'b', 'g', 'g'])) # Expected output: 1 , Real output: "2"
print(count_color_subsets(['r', 'r', 'b', 'b', 'g']))      # Expected output: 0 , Real output: "1"
print(count_color_subsets(['r', 'b', 'g', 'g', 'b', 'r'])) # Expected output: 3 , Real output: "2"
