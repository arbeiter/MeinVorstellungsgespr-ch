def serializeTreeHelper(root_node):
    out_list = serializeTree(root_node)
    print out_list
    
def serializeTree(root_node):
    if root_node==None:
        return ['#']

    out_list = []
    level_list = []
    level_list.append(root_node)

    while level_list!=None:
        temp = level_list[0]
        out_list.append(temp)
        del(level_list[0])
        level_list.append(temp.left)
        level_list.append(temp.right)

    out_list = [x if x not None else '#' for x in level_list]
    return out_list

def deserializeTree(root_node):
    if root_node = node:
        return