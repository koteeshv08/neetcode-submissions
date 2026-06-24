class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for x, y in enumerate(nums):
            index[y] = x
        for i,n in enumerate(nums):
            difference = target-n
            if(difference in index and index[difference] != i):
                return [i, index[difference]]
        return []