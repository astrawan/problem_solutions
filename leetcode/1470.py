class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = []
        for a, b in zip(nums[:n], nums[n:]):
            res.append(a)
            res.append(b)

        return res
