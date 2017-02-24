import stack

def infixToPostfix(infix_exp):
    op_stack = stack.Stack()
    post_exp = []

    prec  = {'*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1}

    tokens = infix_exp.split()
    for token in tokens:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            post_exp.append(token)

        elif token == '(':
            op_stack.push(token)

        elif token == ')':
            top_element = op_stack.pop()
            
            while top_element != '(':
                post_exp.append(top_element)
                top_element = op_stack.pop()

        else:
            while (not op_stack.isEmpty()) and (prec[op_stack.peek()] >= prec[token]):
                    post_exp.append(op_stack.pop())
        
            op_stack.push(token)
        
    while not op_stack.isEmpty():
        post_exp.append(op_stack.pop())
        
    return " ".join(post_exp)

print infixToPostfix("A * B + C * D")
print infixToPostfix("( A + B ) * ( C + D )")
print infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")