class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        n = len(nums)
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right )//2
            if nums[mid] == target:
                if mid != 0 and nums[mid - 1] == target:
                    right = mid - 1
                else:
                    start = mid
                    break
                    
            elif nums[mid] < target:
                left = mid + 1
                
            else:
                right = mid - 1
                
        # print(start)
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right )//2
            if nums[mid] == target:
                if mid != n-1 and nums[mid + 1] == target:
                    left = mid + 1
                else:
                    end = mid
                    break
                    
            elif nums[mid] < target:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return [start, end]