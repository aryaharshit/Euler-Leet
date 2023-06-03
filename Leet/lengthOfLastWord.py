"""
Given a string s consisting of words and spaces,
return the length of the last word in the string.
A word is a maximal substring
consisting of non-space characters only.
"""


# class Solution:
# 	def lengthOfLastWord(self, s):
# 		num = len(s)
# 		for n in reversed(range(num)):
# 			if s[n] == " ":
# 				space = n
# 				print("num, space", num, space)
# 				if space+1 == num:
# 					for x in reversed(range(num)):
# 						if s[x].isalpha():				
# 							last_word = s[space+1: x]
# 							return len(last_word)
# 				else:
# 					last_word = s[space+1:num]
# 					return len(last_word)
# output=Solution()
# result=output.lengthOfLastWord("My name is Harshit Arya     ")
# print(result)


# class Solution:
# 	def lengthOfLastWord(self, s):
# 		num = len(s)
# 		print("num", num)
# 		# count = 0
# 		# extra_space = 0
# 		# for n in reversed(range(num)):
# 		# 	if s[n] == " ":
# 		# 		extra_space = extra_space + 1
# 		for x in reversed(range(num)):
# 			if s[x].isalpha()						
# 				return x
# 		# return extra_space		

# output=Solution()
# result=output.lengthOfLastWord("My name is Harshit Arya   ")
# print(result)

class Solution:
	def lengthOfLastWord(self, s):
		num = len(s)
		print(num)
		for n in reversed(range(num)):
			if s[n] == " ":
				space = n
				print("space", space)
				if space + 1 < num:
					last_word = s[space+1:num]
					return len(last_word)
				else: 
					for x in reversed(range(num)):
						if s[x].isalpha():
							print("x",x)						
							return s[space+1:x]
output=Solution()
result=output.lengthOfLastWord("My name is Harshit Arya   ")
print(result)