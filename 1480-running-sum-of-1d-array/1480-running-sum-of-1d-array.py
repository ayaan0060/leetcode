class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[nums[0]]
        for i in range(1,n):
            x=res[i-1] + nums[i]
            res.append(x)
        return res
