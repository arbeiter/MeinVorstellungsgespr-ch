'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), 
write a program to output the skyline formed by these buildings collectively (Figure B).

Input : [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 
Output: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]]

#Coalesce x intervals
#[2-12] : [2,9,10],[3,7,15],[5,12,12]
#for each x interval:
# go from left to right
#  2 9 10
#  3 7 15
#  5 12 12
#  2 3 4 5 6 7 8  9 10 11 12 13 14 15
#  9,9,9,12,12,12,12,12,12,12,12,7,7,7

#  (9,3), (12,7), (7,3)
#  [2,10],
# Use a max heap for every pos
	# Time complexity :
	#		1. O(interval size)
	#		2. 
'''

