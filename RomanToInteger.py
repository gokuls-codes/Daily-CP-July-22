class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        ones = 0
        tens = 0
        hundreds = 0
        thousands = 0
        
        for character in s:
            if character == 'M':
                thousands += 1
                if hundreds != 0:
                    hundreds *= -1
            elif character == 'D':
                thousands += 0.5
                if hundreds != 0:
                    hundreds *= -1
            elif character == 'C':
                hundreds += 1
                if tens != 0:
                    tens *= -1
            elif character == 'L':
                hundreds += 0.5
                if tens != 0:
                    tens *= -1
            elif character == 'X':
                tens += 1
                if ones != 0:
                    ones *= -1
            elif character == 'V':
                tens += 0.5
                if ones != 0:
                    ones *= -1
            else:
                ones += 1
                
        return int(1000*thousands + 100*hundreds + 10*tens + ones)