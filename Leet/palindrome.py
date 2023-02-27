"""
Given an integer x, return true if x is a
palindrome, and false otherwise.
"""
class Solution:
    def isPalindrome(self, x):
      y = str(x)
      z = y[::-1]
      
      if y == z:
        return True
      else:
        return False
  
output = Solution()
result = output.isPalindrome(121)
print(result)  