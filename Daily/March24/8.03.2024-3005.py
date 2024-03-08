class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        maxFrequency = -1

        for element in counter:
            if counter[element]>maxFrequency:
                maxFrequency = counter[element]

        totalFrequency = 0

        for element in counter:
            if counter[element]==maxFrequency:
                totalFrequency+=maxFrequency

        return totalFrequency
