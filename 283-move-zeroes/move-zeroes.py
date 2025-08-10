class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=-1
        n=len(nums)
        c=nums[0:n-1].count(0)
        for i in range(c):
            for j in range(n-1):
                if nums[j]==0:
                    nums[j],nums[j+1]=nums[j+1],nums[j]