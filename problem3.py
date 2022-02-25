## Problem3 (https://leetcode.com/problems/longest-palindrome)
"""
Time COmplexity: O(n)
n = len(char) in s
Space Complexity: O(n)
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        #Ccount each character
        d = {}
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
            
        count = 0
        for k, v in d.items():
            # if even values all them
            if v % 2 == 0:
                value = v
                count += value
                d[k] = 0
            #if odd values greater than 3 then include all except the last
            elif v >= 3:
                value = v - 1
                count += value
                d[k] = 1
        #if only one single is remaining, add it.
        for k, v in d.items():
            if d[k] == 1:
                count += 1
                break
        return count
                