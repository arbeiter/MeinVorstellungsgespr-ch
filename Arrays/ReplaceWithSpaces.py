def addSpaces(input_string):
    print(input_string)
    i = 0
    j = 0

    count_spaces = 0
    while i<len(input_string):
        if input_string[i]==' ':
            count_spaces+=1
        i+=1

    orig_string = input_string

    i=len(orig_string)-1
    print("i is" + str(i))
    input_string+=str(''.join([' ']*count_spaces*2))

    j=len(input_string)
    input_string = list(input_string)
    print("j is" + str(j))
    print("empty string is "+str(input_string[i]))

    while i>0:
        if input_string[i]==' ':
            print("empty")
            j = j - 3
            input_string[j] = '%'
            input_string[j+1] = '2'
            input_string[j+2] = '0'
        else:
            j = j - 1
            input_string[j] = input_string[i]
        i = i - 1
    return ''.join(input_string)

first_string = addSpaces("a man went home")
print(first_string)
