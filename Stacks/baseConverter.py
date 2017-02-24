import stack

def baseConverter(value, base):
    ans = []
    digits = "0123456789ABCDEF"
    rem_stack = stack.Stack()

    while value > 0:
        rem_stack.push(value % base)
        value = value//base

    while not rem_stack.isEmpty():
        ans.append(digits[rem_stack.pop()])

    return ''.join(ans)

print baseConverter(31,16)
print baseConverter(31,8)
print baseConverter(31,2)
