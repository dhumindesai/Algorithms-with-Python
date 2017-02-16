import stack

def evalPostfix(postfix_str):
    operand_stack = stack.Stack()

    postfix_list = postfix_str.split()

    for element in postfix_list:
        if element in '*/+-':
            op_2 = operand_stack.pop()
            op_1 = operand_stack.pop()
            result = doMath(op_1,op_2, element)
            operand_stack.push(result)
        else: 
            operand_stack.push(int(element))
    
    return operand_stack.pop()



def doMath(op_1,op_2,operator):
    result = 0
    if (operator == '*'):
        result = op_1 * op_2

    if (operator == '/'):
        result = op_1 / op_2

    if (operator == '+'):
        result = op_1 + op_2

    if (operator == '-'):
        result = op_1 - op_2
    
    return result

print evalPostfix("4 5 6 * +")
print evalPostfix("7 8 + 3 2 + /")