from typing import List
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mem = defaultdict(list)
        for word in words:
            mem[word[0]].append(word)

        ans = 0

        for letter in s:
            strings = mem[letter]
            mem[letter] = []
            # print(strings)
            for string in strings:
                if len(string) == 1:
                    ans += 1

                else:
                    mem[string[1]].append(string[1:])

        return ans


print(Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))