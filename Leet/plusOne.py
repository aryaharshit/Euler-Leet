"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

# class Solution:
#     def plusOne(self, nums):
#         for x in range(0, len(nums)):
#             if x == len(nums)-1:
#                 nums[x] = nums[x] + 1
#             if nums[x] <= 9:
#                 pass
#             else:
#                 str_num = str(nums[x])
#                 nums.pop(x)
#                 for i in str_num:
#                     nums.append(int(i))
#         return nums
            
    
# output = Solution()
# result = output.plusOne([3,1,1,9])
# print(result)


class Solution:
    def plusOne(self, nums):
        str_num = ''
        for i in nums:
            str_num += str(i)     
        new_num = int(str_num) + 1
        new_str = str(new_num)
        nums.clear()
        for i in new_str:
            nums.append(int(i))
        return nums
    
output = Solution()
result = output.plusOne([9])
print(result)