class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first, second = 0, 0
        minInteger = -1
        while first<=len(nums1)-1 and second<=len(nums2)-1:
            if nums1[first]== nums2[second]:
                minInteger = nums1[first]
                break
            if nums1[first]<nums2[second]:
                first+=1
            else:
                second+=1
        return minInteger
