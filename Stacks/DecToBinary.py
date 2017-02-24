import stack

def baseConverter(decimal, base):

    digits = "0123456789ABCDEF"
    rem_stack = stack.Stack()

    while decimal > 0:
        rem_stack.push( decimal % base )
        decimal = decimal // base
    
    ans = ""
    while not rem_stack.isEmpty():
        ans = ans + digits[rem_stack.pop()]
    
    return ans

print baseConverter(444,16)
print baseConverter(234,8)
print baseConverter(233,2)

