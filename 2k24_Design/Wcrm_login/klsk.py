import numpy as np
from typing import List, Dict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]* len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix = prefix* nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i]* postfix
            postfix = postfix * nums[i]
        return ans







# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]

print(Solution().productExceptSelf(nums))