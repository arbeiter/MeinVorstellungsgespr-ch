'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

first idea:
a(a) : a -> match a with a[i], call isMatch(a[1])
aa: aa -> match a with a, call isMatch(a[1])
aaa: aa -> match a with a(isMatch("aa", "a"))
aa:a*-> match a with a(isMatch(a, a*){ curr = a*} -> Terminate recursion when len(a)=0) 

aab:a*b* -> 
		ismatch(aab, a*b*)
			isMatch(ab, a*b*)
				isMatch(b, b*)
					val == ""
						return false

ab:.*->
		isMatch(ab, .*)
			isMatch(b, *)
				val == ""
					return false

aab->c*a*b
If ., and string match: use an or sort expression.
						isMatch(aa, .*) or isMatch(aa,.*)

   a aa b bb
a  T
a* T T
b      T T
b*     T T
'''

def match(regex_string, input_string):
	#regex string is of form regex_string
	i, j = 0, 0

	for i in range(len(input_string)):
		if(input_string[i]==regex_string[i]):
						
	return False

# A function to run test cases
def test(first, second):
    if match(first, second):
        print("Yes")
    else:
        print("No")

# Driver program
test("g*ks", "geeks") # Yes
test("ge?ks*", "geeksforgeeks") # Yes
test("g*k", "gee") # No because 'k' is not in second
test("*pqrs", "pqrst") # No because 't' is not in first
test("abc*bcd", "abcdhghgbcd") # Yes
test("abc*c?d", "abcd") # No because second must have 2 instances of 'c'
test("*c*d", "abcd") # Yes
test("*?c*d", "abcd") # Yes

if __name__ == '__main__':
	main()

def main():
	print("Main")
	return
