# %%

from typing import List


def max_area(height: List[int]) -> int:

    highest = (-1, -1)
    maximum = -1

    for i, h1 in enumerate(height):
        for j, h2 in enumerate(height):
            area = min(h1, h2) * abs(j-i)
            if area > maximum:
                maximum = area
                highest = (i, j)
    # print(" idx=", highest)
    return maximum

# %% test


inputs = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1, 1],
]

outputs = [
    49,
    1,
]

for height, expected in zip(inputs, outputs):
    result = max_area(height)
    assert result == expected, f"Expected {expected}, got {result}"
