class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [i**2 for i in nums]
        res.sort()

        return res
