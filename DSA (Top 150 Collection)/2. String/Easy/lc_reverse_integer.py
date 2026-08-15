def reverse_int(x):
    x_str = str(x)

    if x == 0:
        return 0
    elif x_str[0] == "-":
        rev = -1 * int(x_str[:0:-1])
        return rev if rev >= -2 ** 31 else 0
    elif x_str[-1] == "0":
        return int(x_str[-2::-1])
    else:
        rev = int(x_str[::-1])
        return rev if rev <= 2 ** 31 - 1 else 0

x = 123
print(reverse_int(x))