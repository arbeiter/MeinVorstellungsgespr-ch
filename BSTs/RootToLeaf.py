pathsSoFar = []

def findPaths(self):
	listSoFar = [self.root]
	findPathsToRootHelper(self.root, listSoFar)

def findPathsToRootHelper(self, node, pathsSoFar):

	if node.left == None and node.right == None:
		currPath = pathsSoFar[:]
		currPath.append(node)
		return currPath

	pathsLeft = pathsSoFar[:]
	pathsLeft.append(node)

	pathsRight = pathsSoFar[:]
	pathsRight.append(node)

	listAtLevel.append(findPathsToRootHelper(node.left, pathsLeft))
	listAtLevel.append(findPathsToRootHelper(node.right, pathsRight))

	return listAtLevel
