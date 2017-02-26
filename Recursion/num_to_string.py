def num_to_str(num, base):

    convert_str = '0123456789ABCDEF'

    if num < base:
        return convert_str[num]
    
    else:
        return num_to_str(num/base, base) + convert_str[num % base]

print num_to_str(231, 8)
print num_to_str(2144124, 10)
print num_to_str(544, 16)