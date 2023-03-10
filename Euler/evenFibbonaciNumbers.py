"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

class Solution:
	def evenFibbonaci(self, num1, num2):
		num3 = 0
		evenFibbo = []
		while num3 < 4000000:
			num3 = num1 + num2
			if num3 >= 4000000:
				break
			if num3 % 2 == 0:
				evenFibbo.append(num3)
			num1 = num2
			num2 = num3
		return sum(evenFibbo)

output = Solution()
result = output.evenFibbonaci(1,1)
print(result)