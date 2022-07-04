class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        k = k % len(nums)

        for _ in range(len(nums)-k):
            temp = nums.pop(0)
            nums.append(temp)