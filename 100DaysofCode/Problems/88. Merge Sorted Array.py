class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = nums1[:m]
        print(r)
        nums1.clear()
        nums1.extend(r)
        nums1.extend(nums2)
        print(nums1)
        nums1.sort()