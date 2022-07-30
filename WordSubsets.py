class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        m = len(words2)
        counters = [{chr(x):0 for x in range(97, 123)} for _ in range(m)]
        for i in range(m):
            for letter in words2[i]:
                counters[i][letter] += 1
                            
        max_count = {chr(letter):max([counters[i][chr(letter)] for i in range(m)]) for letter in range(97, 123)}
        
        ans = []
        
        for word in words1:
            counter = {chr(x):0 for x in range(97, 123)}
            for letter in word:
                counter[letter] += 1
                flag = 1
            for i in range(97, 123):
                if counter[chr(i)] < max_count[chr(i)]:
                    flag = 0
                    break
            if flag:
                ans.append(word)
                
        return ans