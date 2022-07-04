class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))]
        right = [1 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            
            if ratings[-i-1] > ratings[-i]:
                right[-i-1] = right[-i] + 1

        candies = 0
        for i in range(len(ratings)):
            candies += max(left[i], right[i])

        return candies