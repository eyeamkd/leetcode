class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)
        res = ""

        for char in order:
            if char in counter:
                res += char*counter[char]
                del counter[char]

        for char in counter:
            res+=char*counter[char]

        return res
