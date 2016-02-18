class Point(object):
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

class FindMax(object):
	def __init__(self):
		return

	def maxPoints(self, points):
		dictionary = {}
		for point in points:
			
			return

def main():
	points = [Point(1,2), Point(1,1), Point(2,2), Point(1,2), Point(2,4),Point(3, 6), Point(1,3)]
	soln = FindMax()
	assert(soln.maxPoints(points)==3)

if __name__ == '__main__':
	main()