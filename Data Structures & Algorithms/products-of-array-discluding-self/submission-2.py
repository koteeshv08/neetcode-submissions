class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        nums1 = nums.copy()
        for i in range(len(nums)):
            nums1.pop(i)
            #print(nums1)
            l.append(math.prod(nums1))
            nums1 = nums.copy()
        return l