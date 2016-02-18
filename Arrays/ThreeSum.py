'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''
def findThreeSum(arr):
#Two solution sketches
	#use a hashtable to store all possible (a+b)
	#iterate over arr
	#if -(arr[i]) exists in the table
	#return(a,b,arr[i])

	#sort elements in arr
	#find all combinations[i,j]->sum
	#use binary search to find (0-(a[i]+a[j])), such that index not i or j
	#log n, nlogn, n^2
