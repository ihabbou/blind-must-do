# %%

def longestPalindrome(s: str) -> str:

    longest = ""

    for i, _ in enumerate(s):
        palcentre = s[i]
        palright = ""
        l = i
        c = i - 1
        r = i + 1
        while c >= 0 and l >= 0 and r < len(s):
            if s[l] == s[r]:
                palright = s[l:r+1]
                longest = max([palright, longest], key=lambda s: len(s))
            if s[c] == s[r]:
                palcentre = s[c:r+1]
                longest = max([palcentre, longest], key=lambda s: len(s))

            r += 1
            c -= 1
            l -= 1

    return longest

# %% test


inputs = [
    "babad",
    "cbbd",
]

outputs = [
    "aba",  # "bab", #
    "bb",
]

for (s), expected in zip(inputs, outputs):
    print(expected)
    result = longestPalindrome(s)
    assert result == expected, f"Expected {expected}, got {result}"
