class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        cur = suits[0]
        flag = 1
        for i in range(1, 5):
            if suits[i] != cur:
                flag = 0

        if flag:
            return "Flush"

        counter_ranks = Counter(ranks)
        counts = list(counter_ranks.values())

        maximum = max(counts)

        if maximum >= 3:
            return "Three of a Kind"
        
        if maximum == 2:
            return "Pair"

        return "High Card"