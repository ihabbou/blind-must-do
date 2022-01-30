# %%

def lengthOfLongestSubstring(s: str) -> int:

    slen = len(s)-1

    while (slen > 1):
        sub_set = set()

        for start in range(len(s) - slen + 1):
            sub = s[start: start + slen]
            sub_set.add(sub)

        if len(list(filter(lambda ss: len(ss) == len(set(ss)), sub_set))) != 0:
            return slen

        slen -= 1

    return 1

# %% test


inputs = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
]

outputs = [
    3, 1, 3
]

for (s), expected in zip(inputs, outputs):
    result = lengthOfLongestSubstring(s)
    assert result == expected, f"Expected {expected}, got {result}"
