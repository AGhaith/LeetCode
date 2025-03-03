class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stackopen = []
        for i in s:
            if (i == '('):
                stackopen.append(i)
            else:
                if(stackopen):
                    stackopen.pop()
                else:
                    continue
        return len(stackopen)
