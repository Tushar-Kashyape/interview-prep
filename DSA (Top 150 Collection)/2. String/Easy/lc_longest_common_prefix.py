def longest_common_pref(strs):
    if len(strs) == 1: return strs[0]

    res = ""
    strs.sort()
    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            break
        else:
            res += strs[0][i]
    return res


# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["ab", "a"]
print(longest_common_pref(strs))