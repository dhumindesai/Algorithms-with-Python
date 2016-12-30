import stack

def paranthesisCheck(pattern):
    s = stack.Stack()

    ln  = len(pattern)
    for i in range(ln):
        if pattern[i] == '(':
            s.push(pattern[i])
        elif pattern[i] == ')':
            if s.isEmpty():
                return False
            else:
                s.pop()
    
    if s.isEmpty():
        return True
    else:
        return False

print paranthesisCheck('( () () (()) )')
print paranthesisCheck('(((((((()))')