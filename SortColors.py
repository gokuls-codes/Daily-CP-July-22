class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        i = 0
        for key in [0,1,2]:
            for j in range(counter[key]):
                nums[i] = key
                i += 1
        