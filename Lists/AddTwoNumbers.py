def rotateArray(a, b):
    b= b%len(a)
    ret = []
    for i in range(len(a)-b):
        ret.append(a[i + b])
        
    for i in range(0,b):
        ret.append(a[i])
    return ret

def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in range(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B

def main():
    print(performOps([5,10,2,1]))
    for i in range(0,3):
        print(i)
    #case 1:#1->3->5
            #2->4
            #3->7->5
    #case 2: 5->3
    #        8->4->9
    #        3->8->9
    #case 3: 9->9->9
    #        9->9
    #        8->9->0->1
    #carry over hard to handlev   

if __name__ == '__main__':
    main()