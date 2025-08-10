from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MAx = float('-inf')
        temp = 0
        for i in range(len(nums)):  
            temp += nums[i]
            if temp > MAx:
                MAx = temp
            if temp<0:
                temp=0
        return MAx    
# divide and conquer


    
