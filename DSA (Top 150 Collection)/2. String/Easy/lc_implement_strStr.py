def strsr(haystack, needle):
    return -1 if not needle in haystack else haystack.find(needle)

haystack, needle  = "sadbutsad", "sad"
print(strsr(haystack, needle))