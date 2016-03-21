def plusOne(digits):
    if len(digits)==0:
        return []

    if digits == None:
        return []

    new_list= [0]*len(digits)
    actual = digits[::-1]
    new_list[0] = 1
    carry = 0

    for index, i in enumerate(actual):
        summer = 0
        summer = (new_list[index]+i+carry)%10
        print summer,i, new_list[index]+i+carry
        carry = (new_list[index]+i+carry)/10
        new_list[index] = summer
        print index,i, new_list, carry

    if carry!=0:
        new_list.append(carry)
    return new_list[::-1]
