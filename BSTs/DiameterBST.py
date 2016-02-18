class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST(object):
	
	def __init__(self):
		self.root = None

	def insertDataHelper(self, currNode, newNode):
		if newNode.data < currNode.data:
			if currNode.left == None:
				currNode.left =newNode
				return
			else:
				self.insertDataHelper(currNode.left, newNode)
		else:
			if currNode.right == None:
				print("insert to the right" + str(newNode.data))
				currNode.right =newNode
				return
			else:
				self.insertDataHelper(currNode.right, newNode)

	def insertData(self, data):
		newNode = Node(data)
		if self.root == None:
			self.root = newNode
		else:
			print("insert datar"+str(newNode.data))
			self.insertDataHelper(self.root, newNode)

	def printTree(self):
		self.printTreeHelper(self.root)

	def printTreeHelper(self, currNode):
		if currNode == None:
			return
		self.printTreeHelper(currNode.left)
		print(currNode.data, end="")
		self.printTreeHelper(currNode.right)

	def printDiameter(self):
		printDiameterHelper(self.root)

	def printDiameterHelper(self, node):
		return

def main():
	bst = BST()
	bst.insertData(6)
	bst.insertData(2)
	bst.insertData(8)
	bst.printTree()

if __name__ == '__main__':
	main()
