class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        
        for x in range(len(nums)):
            if nums[x]:
                nums[count] = nums[x]
                count+=1
        for x in range(count, len(nums)):
            nums[x] = 0