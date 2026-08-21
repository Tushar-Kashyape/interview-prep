"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter

def can_construct(ransom_note, magazine):

    counter_r = Counter(ransom_note)
    counter_m = Counter(magazine)

    # determine if all characters of string1 exist in string2 with at least the same
    # frequency (often used to see if an anagram/ word can be formed from a pool of letters)
    if not counter_r <= counter_m:
        return False
    else:
        return True

ransom_note = "aa"
magazine = "aab"
print(can_construct(ransom_note, magazine))