class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        k=0
        while(l<=r):
            if(nums[l]>nums[r]):
                l+=1
            else:
                r-=1
            k = min(nums[l],nums[r])
        return k