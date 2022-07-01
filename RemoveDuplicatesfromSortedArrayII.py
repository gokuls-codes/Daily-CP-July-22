class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        i = 1
        filled = 1
        count = 0
        
        while i < len(nums):
            if nums[i]!=nums[filled-1]:
                nums[filled] = nums[i]
                filled += 1
                count = 0
            elif count==0:
                nums[filled] = nums[i]
                filled += 1
                count += 1
            i += 1
        
        return filled