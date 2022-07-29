class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {coin:1 for coin in coins}
        mem[0] = 0
        
        def dp(a):
            if a < 0:
                return -1
            if a in mem:
                return mem[a]
            
            lst = []
            for coin in coins:
                if a - coin > 0:
                    v = dp(a-coin)
                    if v != -1:
                        lst.append(v)
                    
            if len(lst) > 0:
                mem[a] = min(lst) + 1
                return mem[a]
            else:
                mem[a] = -1
                return -1
            
        return dp(amount)