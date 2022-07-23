from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        mem = {}
        max_count = 0

        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                while i < length and nums[i] == 0:
                    count += 1
                    i += 1

                if count in mem:
                    mem[count] += 1
                else:
                    mem[count] = 1

                if max_count < count:
                    max_count = count
                count = 0
            
            i += 1

        ans = 0
        print(mem)
        for count in range(1, max_count + 1):
            for key in mem:
                if key >= count:
                    ans += ((key-count+1) * mem[key])

        return ans