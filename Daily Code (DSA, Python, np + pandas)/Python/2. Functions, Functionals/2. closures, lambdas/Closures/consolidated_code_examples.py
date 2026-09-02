# Basic Closure:

def make_addr(n):
    def add(x):
        return x + n
    return add

add_5 = make_addr(5)
add_10 = make_addr(10)
print(add_5(5), add_10(3))

# ==============================================================================

# nonlocal: required for reassignment, not for reading

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c(), c(), c())

# ==============================================================================

# Mutation does not need "nonlocal":

def count_dict():
    count = {}
    def increment():
        k = "key"
        if k not in count:
            count[k] = 0
        else:
            count[k] += 1

        return count
    return increment

c_dict = count_dict()
print(c_dict(), c_dict())

# ==============================================================================

# Late-binding loop gotcha:

funcs = [lambda : i for i in range(3)]
print([f() for f in funcs])             #[2, 2, 2] - share same i - Refer Lambdas

funcs_fixed = [lambda i=i:i for i in range(3)]
print([f() for f in funcs_fixed])       #[0, 1, 2] - default arg binds value at
                                        # creation time

# ==============================================================================