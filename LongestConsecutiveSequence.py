class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        longest = 0
        nums = set(nums)
        
        for num in nums:
            if num -1 not in nums:
                current = num
                length = 1
                
                while current + 1 in nums:
                    current += 1
                    length += 1
                    
                if length > longest:
                    longest = length
                    
        return longest
        