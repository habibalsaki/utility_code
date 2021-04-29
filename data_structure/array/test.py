class Solution:
    def twoSum(self, nums, target):
        temp = 0
        newlist = []
        out = []
        for i in range(0, len(nums)):
            newlist.append(temp + nums[i])
            temp = nums[i]
        
        for j in range(0,len(newlist)):
            if newlist[j] == target:
                out.append(j-1)
                out.append(j)
                
        return out

nums = [3,2,4]
target = 6

sol = Solution()
print(sol.twoSum(nums,target))