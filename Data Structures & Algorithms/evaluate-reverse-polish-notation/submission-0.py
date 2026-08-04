class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numstack = []

        for t in tokens:

            if t == '+':
                a = numstack.pop()
                b = numstack.pop()
                numstack.append(a+b)
            elif t == '-':
                a = numstack.pop()
                b = numstack.pop()
                numstack.append(b-a)
            elif t == '*':
                a = numstack.pop()
                b = numstack.pop()
                numstack.append(b*a)
            elif t == '/':
                a = numstack.pop()
                b = numstack.pop()
                numstack.append(int(b/a))
            else:
                numstack.append(int(t))
        return numstack[-1]