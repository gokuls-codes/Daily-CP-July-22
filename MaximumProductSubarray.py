from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_p = min_p = res = nums[0]

        for i in range(1, len(nums)):
            temp_max_p = max(nums[i], max_p * nums[i], min_p * nums[i])
            min_p = min(nums[i], max_p * nums[i], min_p * nums[i])

            max_p = temp_max_p

            res = max(res, max_p)

        return res

print(Solution().maxProduct([-4,-3,-2]))