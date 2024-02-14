class Solution:
    def twoSum(self, nums, target: int):
        tmp = {}
        for idx, x in enumerate(nums):
            if target - x not in tmp:
                tmp[x] = idx
            else:
                return [tmp[target - x], idx]