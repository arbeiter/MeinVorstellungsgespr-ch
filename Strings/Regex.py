'''
‘.’ Matches any single character.
‘*’ Matches zero or more of the preceding element.
The matching should cover the entire input_str string (not partial).

The function prototype should be:
bool assert(isMatch(const char *s, const char *p)

Some examples:
'''

#Attempt 1->
def isMatch(input_str, pattern):
	input_str_ptr = 0
	pattern_ptr = 0
	isMatch = True
	while input_str_ptr<=len(input_str) and  pattern_ptr<=len(pattern):
		if input_str[input_str_ptr]==pattern[pattern_ptr]:
			input_str_ptr += 1
			pattern_ptr += 1
		elif pattern[pattern_ptr] == '.':
			if pattern_ptr + 1 <= len(pattern):
				if(pattern[pattern_ptr+1]=='*'):
					input_str_ptr += 1
		elif pattern[pattern_ptr]=='*':
			if pattern_ptr - 1 >= 0:
				curr_letter = pattern[pattern_ptr-1] 		
	return
		#Check for equality
		#check for .*
		#check for char*
		#ab,a* : match a with a*,
		#aab, a*b : a matches a-> if value match, if pattern_ptr+1 exists and pattern_ptr+1 = * then move input_str_ptr+=1, pattern_ptr
		#aa, a* 
		#ab, a*b : match a with a*, match b with a*(True), match b with b : True
		#.*

		#b,a* : match b with a* False
		#aab,a*b
		#aa,.*
		#aab, c*a*b*
	#a*X
	#b*X
	#.*X
	#aX
	#bX
    return

def main():
	assert(isMatch("aa","a")==False)
	assert(isMatch("aa","aa")==True)
	assert(isMatch("aaa","aa")==False)
	assert(isMatch("aa", "a*")==True)
	assert(isMatch("aa", ".*")==True)
	assert(isMatch("ab", ".*")==True)
	assert(isMatch("aab", "c*a*b")==True)
	assert(isMatch("aab", "c*a*")==True)
