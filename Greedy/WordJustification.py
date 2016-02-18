class Justification(object):
	def fullJustify(self, inputWord, maxWidth):
		i = 0
		sentences = []
		copyList = inputWord[:]
		while len(copyList)!=0:
			sentenceSoFar = []
			currPos = 0
			while len(sentenceSoFar)<=maxWidth:
				currentElement = copyList[currPos]
				if len(sentenceSoFar)+len(currentElement)+1<=maxWidth:
					sentenceSoFar.append(currentElement)
					#check if word's an exact match
					if len(sentenceSoFar)-len(currentElement)!=maxWidth:
						sentenceSoFar.append(" ")
					#if not add a space to the end
					del copyList[currPos]
				currPos +=1
			if len(sentenceSoFar)>0:
				sentences.append(sentenceSoFar)
		return sentences

def main():
	print("blah")
	just = Justification()
	#Test case 1
	inputList = ["watashi", "no", "fureru", "princess", "kaguya"]
	res = just.fullJustify(inputList, 8)
	#Test case 2

if __name__ == '__main__':
	main()
