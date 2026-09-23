class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not len(nums):
            return []
        
        prefix = [1]
        for i in nums[:-1]:
            prefix.append(prefix[-1] * i)
        print(prefix)

        sufix = [1]
        for i in reversed(nums[1:]):
            sufix.append(sufix[-1] * i)
        sufix.reverse()
        print(sufix)

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * sufix[i]
        
        return res