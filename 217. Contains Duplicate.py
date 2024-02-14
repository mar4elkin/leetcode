class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp = set()
        for idx, x in enumerate(nums):
            if x in tmp:
                return True
            else:
                tmp.add(x)
            
        return False