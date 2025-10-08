class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        t = [0 for _ in range(len(nums))]
        t[0] = nums[0]
        t[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            t[i] = max(nums[i] + t[i-2], t[i-1])

        
        return t[-1]
