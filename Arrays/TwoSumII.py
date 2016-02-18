'''Question: 
Given an array of integers, find two numbers such that they add up to a specific target number. 

The function twoSum should return indices of the two numbers 
such that they add up to the target,
where index1 must be less than index2. 

Please note that your returned answers 
(both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
'''
def findTwoSum(sortedArr, num):
	i=0
	j = len(sortedArr)-1

	while i<len(sortedArr) and j>0:
		if sortedArr[i]+sortedArr[j]==num:
			print(i)
			print(j)
			return i+1, j+1
		elif sortedArr[i]+sortedArr[j]<num:
			i = i+1
		elif sortedArr[i]+sortedArr[j]>num:
			j = j-1
	return -1,-1

def main():
	assert(findTwoSum([1,3,5,9], 6)==(1,3))
	assert(findTwoSum([1,4,5,6], 7)==(1,4))

if __name__ == '__main__':
	main()
