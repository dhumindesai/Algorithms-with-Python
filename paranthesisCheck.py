import stack

def paranthesisCheck(pattern):
    s = stack.Stack()

    ln  = len(pattern)
    for i in range(ln):
        if pattern[i] in '({[':
            s.push(pattern[i])
        elif pattern[i] in ')}]':
            if s.isEmpty():
                return False
            else:
                if not matches(s.pop(),pattern[i]):
                    return False
    
    if s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = '({['
    closes = ')}]'
    return opens.index(open) == closes.index(close)

print paranthesisCheck('[{ {[]} () () (()) }]')
print paranthesisCheck('(([((({}((()))')