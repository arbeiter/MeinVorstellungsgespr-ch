'''A group of two or more people wants to meet and minimize the total travel distance.
  You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
  The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

Solve for x
Solve for y

	 0   1     2     3    4
1	 1 - 0 -   0  - 0 -   1
	 |   |     |     |    |
2	 0 - 0 -   0 -  1 -   0 
	 |   |     |     |    |
3	 1 - 0 -   1  -  0 -  0


	 0   1     2     3    4
1	 1 - 0 - [ 0 ] - 0 -  1
	 |   |     |     |    |
2	 0 - 0 -  [0] -  1 -  0 ==
	 |   |     |     |    |
3	 1 - 0 -   1  -  0 -  0


	 0   1     2     3    4
1	 1 - 0 - [ 0 ] - 0 -  1
	 |   |     |     |    |
2	 0 - 0 -  [0] -  1 -  0 ==
	 |   |     |     |    |
3	 1 - 0 -   1  -  0 -  0


			   k

[0,0] [0,4] [4,0] 

Approach 1:

1. Find the mid point between horizontal points
2. Find the mid point vertical points
3. 	Pick horizontal vertex
	Pick vertical vertex

Approach 2:
1. Sort all points? Find the median?

Approach 3:
1. Find the kth largest

Problem: Given 3 unsorted integer array, 
find out the minimum triangle between the three arrays. 
That is, find out arr1[i], arr2[j] and arr3[k] 
such that dist = |arr1[i]-arr2[j]| + |arr2[j]-arr3[k]| + |arr1[i]-arr3[k]| is a minimum.
'''
