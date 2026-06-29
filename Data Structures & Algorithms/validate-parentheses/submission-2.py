class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose={")":"(","}":"{","]":"["}   #hash
        stack=[]
        for i in s:
            if i in opentoclose:
                if stack and stack[-1]==opentoclose[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False
            