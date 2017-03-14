def solution(X):

    new_numbers = []
    X_str = str(X)

    for i in range(len(X_str) - 1):

        avg = (int(X_str[i]) + int(X_str[i+1])) / 2.0
        avg = roundToUpper(avg)
        num = X_str[:i] + str(avg) + X_str[i+2:len(X_str)+1]
        num = int(num)
        new_numbers.append(num)
    
    return max(new_numbers)

def roundToUpper(num):
    n = int(num)
    return n if n-1 < num <= n else n+1

print solution(623315)
