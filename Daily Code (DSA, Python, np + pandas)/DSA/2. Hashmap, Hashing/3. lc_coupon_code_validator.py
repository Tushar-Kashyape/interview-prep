"""
3606. Coupon Code Validator

You are given three arrays of length n that describe the properties of n coupons:
code, businessLine, and isActive. The ith coupon has:

code[i]: a string representing the coupon identifier.
businessLine[i]: a string denoting the business category of the coupon.
isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:

code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9)
and underscores (_).

businessLine[i] is one of the following four categories:
"electronics", "grocery", "pharmacy", "restaurant".

isActive[i] is true.

Return an array of the codes of all valid coupons, sorted first by their businessLine
in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in
lexicographical (ascending) order within each category.



Example 1:

Input:
code = ["SAVE20","","PHARMA5","SAVE@20"],
businessLine = ["restaurant","grocery","pharmacy","restaurant"],
isActive = [true,true,true,true]

Output: ["PHARMA5","SAVE20"]

Explanation:

First coupon is valid.
Second coupon has empty code (invalid).
Third coupon is valid.
Fourth coupon has special character @ (invalid).

Example 2:

Input:
code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"],
businessLine = ["grocery","electronics","invalid"],
isActive = [false,true,true]

Output: ["ELECTRONICS_50"]

Explanation:

First coupon is inactive (invalid).
Second coupon is valid.
Third coupon has invalid business line (invalid).


Constraints:

n == code.length == businessLine.length == isActive.length
1 <= n <= 100
0 <= code[i].length, businessLine[i].length <= 100
code[i] and businessLine[i] consist of printable ASCII characters.
isActive[i] is either true or false.
"""

"""
NO LOOK CODE/ HELP TAKEN

. "" -> should be checked beforehand.
"""

def validate_coupon(codes: list[str], business_lines: list[str],
                    is_active: list[bool]) -> list[str]:

    result = []
    valid_business = {"electronics", "grocery", "pharmacy", "restaurant"}

    for code, business_line, status in list(zip(codes, business_lines, is_active)):

        def validate_code(code):

            if not code:
                return False

            for c in code:
                if not c.isalnum() and c != "_":
                    return False

            return True

        if status and validate_code(code) and business_line in valid_business:
            result.append((business_line, code))

    return [c for (b, c) in sorted(result)]


codes = input("Enter coupon codes: ").split()
business_lines = input("Enter business line: ").split()
is_active = list(map(bool, input("Is coupon active: ").split()))

# codes = ["SAVE20","","PHARMA5","SAVE@20"]
# business_lines = ["restaurant","grocery","pharmacy","restaurant"]
# is_active = [True, True, True, True]

print(validate_coupon(codes, business_lines, is_active))
