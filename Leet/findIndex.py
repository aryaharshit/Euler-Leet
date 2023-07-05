'''
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
'''

import re
class Solution:
    def strStr(self, haystack, needle):
        x = re.search(needle, haystack)

        if x:
            for i in range(len(haystack)):
                search_term = haystack[i : i + len(needle)]
                if search_term == needle:
                    return i
        else:
            return -1

output = Solution()
result = output.strStr('mississipi', 'issip')
print(result)  