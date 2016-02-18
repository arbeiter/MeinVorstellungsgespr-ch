'''
Count the 2’s between 0 and N.  And every 2 digit counts as a 2, so if N was 7 the answer would be 1
 (just the number 2), whereas if n was 23 there would be 7 2’s {2, 12, 20, 21, 22(this counts for 2), 23}
'''
# 223

# given intmax = 2^32
# int_some = 2^16 -> 1,2,3,4,5,6,7,8,9,10,11,12
# compute all 10**n

# 234 = cache[233] + number of 2s in 234
# 235 = cache[234] + number of 2s in 235
# 232 = cache[231] + number of 2s in 232
#number of 2s in 234 => is 234/10 == 2 and num2Cache[34] = 0
#12
#

class Solution:
	def __init__(self):
		self.runningCount = 0

	def getNumberOfTwos(self,num):
		
		return num

	def countRecursive(self, num):
		if num in self.countFreqCache.keys():
			return self.countFreqCache[num]
 
		countSoFar = 0
		if (num>=2 and num<10):
			self.countFreqCache[num] = 1
			return self.countFreqCache[num]

		if(num/10) == 2:
			countSoFar += 1
			print(str((int)(num/10)))

		predescessor = (int)(num/10)

		self.countFreqCache[num] = self.countFreqCache[predescessor] + countSoFar
		return self.countFreqCache[num]

	def countTwos(self, num):
		i=0

		if num<2:
			return 0
		freq_i = 0

		i=2
		while(i<=num):
			freq_i = self.countRecursive(i)
			i+=1

		print(self.countFreqCache)
		return freq_i

soln = Solution()
print(soln.countTwos(22))
#1000 to 1
#1000 Soln(999....1)
#countTwos()
'''
# i ranges from 2 to num
#countTwos(3)
# i = 2, countFreq(2) 
# i = 3, countTwos = 
# i = 4, countFreq(2), countFreq(3)
'''
