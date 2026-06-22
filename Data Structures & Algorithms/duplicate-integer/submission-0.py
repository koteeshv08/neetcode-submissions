class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=1
        nums.sort()
        for x in nums:
            if i<len(nums) and x==nums[i]:
                return True
            i=i+1
        return False
