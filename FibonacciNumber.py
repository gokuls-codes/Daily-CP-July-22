class Solution:
    def fib(self, n: int) -> int:
        mem = [0, 1]

        def dp(num):
            if num < len(mem):
                return mem[num]
            
            mem.append(dp(num-1) + dp(num-2))

            return mem[num]

        return dp(n)

