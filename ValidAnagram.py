class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        if len_s != len_t:
            return False
        
        counter = defaultdict(int)
        for i in range(len_s):
            counter[s[i]] += 1
            counter[t[i]] -= 1
            
        for key in counter:
            if counter[key] != 0:
                return False
            
        return True