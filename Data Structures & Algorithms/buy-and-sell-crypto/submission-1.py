class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res = 0
        for i in range(len(p) - 1):
            for j in range(i + 1, len(p)):
                tmp = p[j] - p[i]
                if tmp > res:
                    res = tmp
        if res > 0:
            return res
        else:
            return  0
            