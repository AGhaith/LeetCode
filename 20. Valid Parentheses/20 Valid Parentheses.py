class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack1=[] 
        
        
        for i in s:
            if i in ['(','[','{']:
                stack1.append(i)
            elif i in [')',']','}']:
                if len(stack1) == 0:
                    return False
                if i == ')' and stack1[-1] == '(':
                    stack1.pop()
                elif i == ']' and stack1[-1] == '[':
                    stack1.pop()
                elif i == '}' and stack1[-1] == '{':
                    stack1.pop()
                else:
                    return False                
        if len(stack1) == 0 :
            return True
        return False
        
        
        