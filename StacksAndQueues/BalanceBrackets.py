class Solution(object):
    def isValid(self, s):
        if len(s)<=1:
            return False

        stack=[s[0]]
        for elem in s[1:]:
            toPop = self.check_if_opposite(stack[-1],elem)
            stack.append(elem)
            if toPop:
                stack.pop()
                stack.pop()
        return len(stack)==0
            
    def check_if_opposite(self, input1, input2):
        if input1 == '(' and input2==')':
            return True
        elif input1=='{' and input2=='}':
            return True
        elif input1=='[' and input2==']':
            return True
        return False

s = Solution()
assert(s.isValid("[{])}]")==False)
assert(s.isValid("[{}]")==True)
