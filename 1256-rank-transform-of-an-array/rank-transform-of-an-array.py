class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        result = []
        d1 = {}
        l1 = sorted(arr)

        rank = 1
        for i in range(len(l1)):
            if l1[i] not in d1:
                d1[l1[i]] = rank
                rank += 1

        for i in arr:
            result.append(d1[i])

        return result