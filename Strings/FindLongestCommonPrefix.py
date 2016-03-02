#0, n
#list of strings
#given a list of strings, compare all the elements at a position

def get_longest_prefix(**str_args):
    inputter = list(str_args)
    pos = 0
    while compare_elems(input_list, pos) is True:
        pos+=1
    return str_args[0][:pos]

def compare_elems(input_list, pos):
    are_equal = False
    if len(input_list)==0:
        return False
    
    if pos>len(input_list[0][pos]):
        curr_elem = input_list[0][pos]
        
    for elem in input_list:
        if pos>len(elem):
            return False
        if elem[pos]!=curr_elem:
            return False
        
    return True
