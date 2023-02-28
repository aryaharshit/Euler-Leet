"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

class Solution:
	def primeNumber(self, check_prime):
		for i in range(2, int(check_prime**0.5)+1):
			if check_prime % i == 0:
				return False
		return True

	def primeFactor(self, num):
		primeFacts = []
		new_nums = int(num**0.5)+1
		for x in range(2, new_nums):
			if num % x == 0:
				facts = self.primeNumber(x)
				if facts == True:
					primeFacts.append(x)
		return primeFacts[-1]

output = Solution()
result = output.primeFactor(600851475143)
print(result)