class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        res = []
        for n in nums:
            if my_dict.get(n) == None:
                my_dict[n] = 0
            my_dict[n] += 1

        s = [key for key, value in sorted(
            my_dict.items(), 
            key=lambda x: x[1], 
            reverse=True)]
        print(s)
        flag = 0
        for i in range(k):
            res.append(s[i])

        return res
