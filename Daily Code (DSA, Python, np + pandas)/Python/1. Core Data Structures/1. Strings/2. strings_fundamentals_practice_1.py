from collections import defaultdict


def group_shifted_strings(strings):
    diff_dict = defaultdict(list)

    for s in strings:
        diff = []
        for i in range(1, len(s)):
            diff.append((ord(s[i]) - ord(s[i - 1])) % 26)

        diff_dict[tuple(diff)].append(s)

    return list(diff_dict.values())

strs = input("Enter strings: ").split()
# strs = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(group_shifted_strings(strs))