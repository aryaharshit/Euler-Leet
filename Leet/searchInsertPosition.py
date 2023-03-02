"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        mid = 0

        while low <= high:
            mid = (high+low)//2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low 

output = Solution()
result = output.searchInsert([1,3,5,6], 7)
print(result)       
