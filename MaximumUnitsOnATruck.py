class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        i = 0
        while i < len(boxTypes) and truckSize >= boxTypes[i][0]:
            ans += boxTypes[i][0] * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1
        
        if i < len(boxTypes):
            ans += truckSize * boxTypes[i][1]
        return ans