from typing import List

# class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
        # MAx = float('-inf')
        # temp = 0
        # for i in range(len(nums)):  
            # temp += nums[i]
           #  if temp > MAx:
                # MAx = temp
           #  if temp<0:
                # temp=0
        # return MAx    
# divide and conquer


    
class Solution:
    def divide(self, nums: List[int]):
        mid = len(nums) // 2
        if len(nums) == 1:
            return nums[0]
        
        left=self.divide(nums[0:mid])
        right=self.divide(nums[mid:len(nums)])

        leftSum = float("-inf")
        temp = 0
        for i in range(mid - 1, -1, -1):
            temp += nums[i]
            if leftSum < temp:
                leftSum = temp

        rightSum = float("-inf")
        temp = 0
        for i in range(mid, len(nums)):
            temp += nums[i]
            if rightSum < temp:
                rightSum = temp

        crossSum = leftSum + rightSum
        return max(left, right, crossSum)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.divide(nums)
