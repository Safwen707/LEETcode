class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def sumCouple(nums: List[int],count:int)-> int:
            sortedd=[i for i in nums]
            sortedd.sort()
            print(sortedd)
            print(nums)

            if not nums or sortedd==nums:
                 return count
            if len(nums)==1:
                return count+1
            
            
            d={(i,i+1):nums[i]+nums[i+1] for i in range(len(nums)-1)}
            minn=float('inf')
            ToBeReplaced=(0,0)

            for t,s in d.items():
                if s<minn:
                    minn=s
                    ToBeReplaced=t
            print(ToBeReplaced)
            nums[ToBeReplaced[0]]=minn
            nums.pop(ToBeReplaced[1])
            count+=1
            
            return sumCouple(nums,count)
        return sumCouple(nums,0)

                
                


            

            
            