from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        for num in nums:
            if num == 0:
                return 0
        
        
        negatives = sum(1 for num in nums if num < 0)
      
        return 1 if negatives % 2 == 0 else -1
