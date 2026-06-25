class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sum = []
        nums.sort()
        #print(nums)
        if(len(nums)==0):
            return 0
        elif(len(nums)==1):
            return 1
        else:
            k=1
            for i in range(1,len(nums)):
                if(nums[i]-nums[i-1] == 1):
                    k+=1
                    print(k)
                elif(nums[i-1]-nums[i] == 0):
                    continue
                else:
                    sum.append(k)
                    k=1
            sum.append(k)
            print(sum)
        return max(sum)