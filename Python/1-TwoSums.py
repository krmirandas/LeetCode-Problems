#! /usr/bin/python3
from typing import List
# import sys

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        for i, value in enumerate(nums): 
            complement = target - value
            if complement in positions:
                return [positions[complement], i]
            else: 
                positions[value] = i
        
        
solution = Solution()
r = solution.twoSum([2,7,11,15], 9)
print(r)
# lines = sys.stdin.readlines()


