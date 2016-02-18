def calculateSummaryRanges(inputArr):
  i = 1
  ranges = []
  currRange = []
  currRange.append(inputArr[0])
  while i<len(inputArr):
    if(inputArr[i]-1!=inputArr[i-1]):
      currRange.append(inputArr[i-1])
      ranges.append(currRange)
      currRange = []
      currRange = [inputArr[i]]
    i+=1
  currRange.append(inputArr[i-1])
  ranges.append(currRange)
  return ranges

def main():
  print(calculateSummaryRanges([1,2,3,4,5]))
  print(calculateSummaryRanges([1,2,3,5,6]))

if __name__ == '__main__':
	main()
