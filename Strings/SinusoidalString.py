arr = [][]

def sinusoidal(stringer):
	isFirstLine = False
	i=0
	while i<len(stringer):
		if(i%2==0):
			offsetter(a[i], 1)
		else:
			offset = isFirstLine ? 0 : 2
			offsetter(a[i], offset)
			isFirstLine = False
	return

def offsetter(element, offset):
	for i in range(offset):
		print()
	print(element, end="")

def main():
	return

if __name__ == '__main__':
	main()
