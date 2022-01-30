# %%

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:

    ppairs = dict()

    for i, n in enumerate(nums):
        if (target - n) in ppairs:
            return [ppairs[target - n], i]
        else:
            ppairs[n] = i

    for i, n in enumerate(nums):
        for j in range(i+1, len(nums)):
            if n + nums[j] == target:
                return [i, j]

    return []

# %% test


inputs = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
]

outputs = [
    [0, 1],
    [1, 2],
    [0, 1],
]

for (nums, target), expected in zip(inputs, outputs):
    assert two_sum(nums, target) == expected
