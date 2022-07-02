class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        if horizontalCuts == [] and verticalCuts == []:
            return (h * w)%(10**9 + 7)

        horizontalCuts.sort()
        verticalCuts.sort()
        
        heights = [horizontalCuts[0]]
        for i in range(1, len(horizontalCuts)):
            heights.append(horizontalCuts[i] - horizontalCuts[i-1])
        heights.append(h - horizontalCuts[-1])
        
        widths = [verticalCuts[0]]
        for i in range(1, len(verticalCuts)):
            widths.append(verticalCuts[i] - verticalCuts[i-1])
        widths.append(w - verticalCuts[-1])

        return (max(widths) * max(heights))%(10**9 + 7)