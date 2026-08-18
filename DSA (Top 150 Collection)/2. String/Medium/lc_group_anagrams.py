def group_anagrams(strs):
    res, dic = [], {}

    if len(strs) <= 1:
        res.append(strs)
        return res

    for s in strs:
        sorted_str = "".join(sorted(s))

        if sorted_str in dic:
            dic[sorted_str].append(s)
        else:
            dic[sorted_str] = [s]

    return list(dic.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))