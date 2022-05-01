# %%

from typing import List, Set


def threesum(nums: List[int]) -> List[List[int]]:

    ppairs = dict()
    sums = set()

    for i, n in enumerate(nums):
        for j, m in list(enumerate(nums))[i+1:]:
            if (i != j):
                ppairs[n + m] = (i, j)

    for i, n in enumerate(nums):
        if -n in ppairs:
            if i not in ppairs[-n]:
                idx = ppairs[-n]
                triplet = tuple(sorted([nums[idx[0]], nums[idx[1]], n]))
                sums.add(triplet)

    return [list(t) for t in sums]

# %% test


inputs = [
    [-1, 0, 1, 2, -1, -4],
    [],
    [0],
]

outputs = [
    [[-1, -1, 2], [-1, 0, 1]],
    [],
    [],
]

for nums, expected in zip(inputs, outputs):
    result = threesum(nums)
    assert result == expected, f"\nExpected {expected}, \ngot\t {result}"
