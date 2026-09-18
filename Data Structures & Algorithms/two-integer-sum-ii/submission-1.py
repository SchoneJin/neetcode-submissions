class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        res = []
        i = 0
        j = len(num) - 1
        while i < j:
            if num[i] + num[j] > target:
                j -= 1
            if num[i] + num[j] < target:
                i += 1
            if num[i] + num[j] == target:
                res.append(i + 1)
                res.append(j + 1)
                break

        return res
        