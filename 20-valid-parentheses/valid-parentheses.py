class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for data in s:
            if data in '({[':
                stack.append(data)
            elif len(stack)==0:
                return False
            else:    
                if data == ')' and stack[-1]!='(':
                        return False
                elif data == ']' and stack[-1]!='[':
                        return False 
                elif data == '}' and stack[-1]!='{':
                        return False                       
                top_value=stack.pop()   
        if len(stack) == 0:
            return True
        else:
            return False    

        