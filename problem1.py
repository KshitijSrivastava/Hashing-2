## Problem1 (https://leetcode.com/problems/subarray-sum-equals-k/)

"""
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        out = 0
        
        #hash map storing the prefix sum
        d = {}
        d[0] = 1
        
        curr_sum = 0
        for num in nums:
            #calculating the current sum
            curr_sum += num
            
            #if curr_sum - k in the d, add the number of pairs found 
            if curr_sum - k in d:
                out += d[ curr_sum - k ]
                
            #add the current sum to the prefix hashmap
            if curr_sum not in d:
                d[curr_sum] = 0 
            d[curr_sum] += 1
            
        #return the number of pairs
        return out