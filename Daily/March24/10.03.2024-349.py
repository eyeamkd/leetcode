class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = set()
        res2 = set()

        for num in nums1:
            res1.add(num)
        for num in nums2:
            if num in res1:
                res2.add(num)

        return list(res2)
