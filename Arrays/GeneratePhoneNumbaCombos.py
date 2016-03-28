dicter = {0:"",1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv",9:"wxyz"}

def find_combinations(num):
	vals = helper(str(num), [])
	return vals
	
def helper(num, res):
	if len(num)==0:
		return "".join(res)

	numlen = len(num)
	first_letter =(int)(num[0])
	final_res = []
	
	stringer = list(dicter[first_letter])

	for val in stringer:
		yep = res[:]
		yep.append(val)
		val_so_far = helper(num[1:], yep)
		final_res.append(val_so_far)

	return final_res

print find_combinations(235)
