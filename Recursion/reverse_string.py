def reverse_string(s):

    if len(s) == 1:
        return s
    
    else:
        return s[len(s)-1] + reverse_string(s[:len(s)-1])

print reverse_string("RUTVI")