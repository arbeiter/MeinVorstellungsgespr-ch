#Array of elements
#2d Array
from enum import Enum
from random import randint

class PaintBoard:

	def __init__(self, row, col):
		self.colorMap = {1:"B", 2:"W", 3:"R", 4:"Y"}
		self.board = self.initialize2dArray(row, col)

	def initialize2dArray(self, row, col):
		arr = [["W" for i in range(col)] for j in range(row)]
		for i in range(row):
			for j in range(col):
				val = randint(1,4)
				arr[i][j] = self.colorMap[val]
		return arr

	def paintBoard(self):
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				print(self.board[i][j], end=" ")
			print()
		print()

	def isValidCell(self, startPos, endPos):
		#row, col

		if startPos>0 and startPos<(len(self.board)):
			if endPos>0 and endPos<(len(self.board[0])):
				return True
		return False

	def floodFillHelper(self, startPos, endPos, color):
		if self.isValidCell(startPos, endPos)!=True:
			return

		if self.board[startPos][endPos] == color:
			return
		else:
			self.board[startPos][endPos] = color

		self.floodFillHelper(startPos+1, endPos, color)
		self.floodFillHelper(startPos-1, endPos, color)
		self.floodFillHelper(startPos, endPos-1, color)
		self.floodFillHelper(startPos, endPos+1, color)	

	def floodFill(self, startPos, endPos):
		print("call")
		if self.isValidCell(startPos, endPos)!=True:
			return False
		else:
			print("yay")
		color = self.board[startPos][endPos]
		self.floodFillHelper(startPos+1, endPos, color)
		self.floodFillHelper(startPos-1, endPos, color)
		self.floodFillHelper(startPos, endPos-1, color)
		self.floodFillHelper(startPos, endPos+1, color)	

def main():

	board1 = PaintBoard(4,4)
	board1.paintBoard()
	board1.floodFill(1,1)
	board1.paintBoard()
'''
	board2 = PaintBoard(20,10)
	board2.paintBoard()

	board3 = PaintBoard(4,6)
	board3.paintBoard()

	board4 = PaintBoard(5,9)
	board4.paintBoard()
'''

if __name__ == '__main__':
	#invoke main
	main()

