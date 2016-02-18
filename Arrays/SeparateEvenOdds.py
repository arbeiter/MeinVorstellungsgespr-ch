def separateEvensAndOdds(input_arr):
    #if empty arr
    #if len = 1,2

    #len>2
    i, j = 0, 0
    while i<len(input_arr):
        if input_arr[i]%2 == 1:
            j = i
            print(j)
            while j <len(input_arr) and input_arr[j]%2 != 0:
                j = j + 1
            if j<len(input_arr):
                temp = input_arr[i]
                input_arr[i] = input_arr[j]
                input_arr[j] = temp
                print("SWAP")           
        i = i + 1
    print(input_arr)

separateEvensAndOdds([])
