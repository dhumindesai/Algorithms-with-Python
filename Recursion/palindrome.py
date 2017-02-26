def is_palindrome(s):

    if len(s) < 2:
        return True
    
    if s[len(s) - 1] == s[0]:
        return is_palindrome(s[1:len(s)-1])
    
    else:
        return False
    #return bool (( s[len(s) - 1] == s[0] ) * is_palindrome(s[1:len(s)-1]))

print is_palindrome('wassamassaw')