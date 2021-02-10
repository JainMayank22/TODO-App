class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        for i in range(1,len(nums)):
            
            if nums[x]<nums[i]:
                x+=1
                nums[x] = nums[i]
        return x+1