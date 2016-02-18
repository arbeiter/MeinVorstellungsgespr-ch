'''
Max binary gap
Given 9: 1001: Answer's 2
Given 5: 101: Answer's 1
Given 8: 1000: Answer's 3
Given 11: 1011 : Answer's 1
Given 43: 101011: Answer's 1
Given 37: 100101 : Answer's 2
'''
def getMaxBinaryGap(num):
    oneSeen = False
    maxCount = 0
    count = 0
    while num!= 0:
        if num%2 == 1:
            oneSeen = True
            count = 0
        else:
            if oneSeen==True:
                count+=1
        if count>maxCount:
            maxCount = count
        num = num >> 1
    return maxCount

def printBinary(num):
    curr = num
    lister = []
    while(curr!=0):
        lister.append(curr%2)
        curr = curr >> 1
    lister = lister[::-1]
    outStr = "".join(str(x) for x in lister)
    print(outStr)

printBinary(9)
print(getMaxBinaryGap(9))