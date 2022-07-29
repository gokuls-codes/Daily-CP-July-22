
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            to_change = {}
            changed = set()
            flag = 1
            for i in range(len(pattern)):
                if pattern[i] in to_change:
                    if to_change[pattern[i]] != word[i]:
                        flag = 0
                        break
                else:
                    if word[i] not in changed:
                        to_change[pattern[i]] = word[i]
                        changed.add(word[i])
                    else:
                        flag = 0
                        break
        
            if flag:
                ans.append(word)
                
        return ans