
class Solution:
    def countMin(self, Str):
        # code here
        n = len(Str)
        mem = [[0 for _ in range(n+1)] for _ in range(n+1)]

        def lcs(str1, str2):
            for i in range(n+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        mem[i][j] = 0

                    elif str1[i-1] == str2[j-1]:
                        mem[i][j] = mem[i-1][j-1] + 1
                    
                    else:
                        mem[i][j] = max(mem[i-1][j], mem[i][j-1])

            return mem[n][n]

        rev = list(Str)
        rev.reverse()

        rev = "".join(rev)

        return n - lcs(Str, rev)

print(Solution().countMin("abcd"))