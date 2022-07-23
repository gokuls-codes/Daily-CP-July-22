#User function Template for python3
class Solution:
    def maxSubstring(self, S):
		# code here
        if '0' not in S:
            return -1

        current = 0
        maximum = 0

        for i in range(len(S)):
            val = 1 if S[i] == '0' else -1
            current += val

            if current < 0:
                current = 0

            if current > maximum:
                maximum = current

        return maximum
 
print(Solution().maxSubstring("0001001010000000100111001001011000011111011010001011001010101101100111000000001110110001010010101000111111110010110000001001011001000111101111011100101000011010101101000000000000000000001000001110010001011010010110001001101000001011000001111100011100010011110011110110100101100000011001111100010001000111101011100101100101100011100101110100011011011101010100110110000111001111101010101101010100000001001001011100101001111010001001011110110100100000001011000011011010111001101101000110100000001011011100101010001000010011110010101000001010010000001011110100100100101010010010110100111011111011000100010110000100111011001001100100111110001011101101000100001000010110011111000001101000001010010110101101011000011001000100011001010100000110011001001010110100011011111010110101011011101110110001011001000100010011111110001001011011001001111001001000100010110011010010000000000110000100000100001011110100010101010000011001011110110001110010110001100000111011011010001110011010000010100001101100111001010110111011000001101001000011001100111011110000001001111100100000001101010110110101110010011000000010010011111111101110000011001000100001000001100010011011111100010010011001010101011100001101111110101100000111010001010011000101101110100110010110110001001100000011100101111110010110010110111101111101010111111001101001101111110011011110111001110000011000010111011000010000011000110000011100011001010001010110010001000111101010011010110010010011110001010010010101111100101000101100110110101110010000110111011001011110001101101001011101111011100101101000100011110111111111101110001111001110111000011010110111001000100001100001010110110100111001101001111000111110110001111111000111010001011011011101101001101111100111000110111100101000011010111000100110100011000011010011000111110101011100111101101110000001110010100110101011110001010011111100000100101000010001100000111000100011001001001100001100000101110001011000010010101001011101011011110000010001101101000101001110100010100001101011001101010011000111110100111010000100001101111000000010011001000111010111001110011100000110110001110100010010100011101100001011100100111010111001010110110010001101110100011111111001011101000110011111001110110001000111010011001111010110010100000111100000001001100100010110001101000100101101110110011001101111101000000100011101011101011010111001101101111011111010001110000000100010100010101000110110011110001001011000110100001000010000011111011110010100011110000101000100111110010010110000100101110011000000000110000100000000000000101000010011001011111111001111011011110110100100011110100111101101010101100010100000011011011010111111001111110010100101101011110010100001010010010000100110101000001000111001111000100111111111010101111111100000010100111010010001101000100000011100100101011001000100110001101000110000111100110010100011101001100100011011000100110110011111101001010100101001010111110110011011110110011001111101010010011000001000001111100010110101100111110100000011000100000010010101001010101101111110010111011001100100111010110001100000100011011101101110111001011111011111101111000000111011000" ))