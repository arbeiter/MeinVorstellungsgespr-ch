'''
Given a map and a string find all interpretations of the string
{ "1": a, 
  "2": b, 
  "3": c, 
  ..., 
  "26": z }

Example 1:

"112" - 3 interpretations
"al", "aab", "kb"

(1, 12), (1, 1, 2) , (11, 2)
split 1, (recurse 12)

112

112-> [1][12] -> key over([1]), keyover([12])
112-> [11][2] -> key over([11]), key over([2])
112-> [112] -> key(over set)

112 -> 112

1
2
12

Example 2:

"345" - 1 interpretation
"cdf"

Assume the mapping is already given to you and passed in as a parameter
Can be solved in O(n) runtime
'''
