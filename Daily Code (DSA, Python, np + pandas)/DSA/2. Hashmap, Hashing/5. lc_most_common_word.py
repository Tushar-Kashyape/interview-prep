"""
819. Most Common Word

Given a string paragraph and a string array of the banned words banned, return the
most frequent word that is not banned. It is guaranteed there is at least one word
that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in
lowercase.

Note that words can not contain punctuation symbols.



Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
banned = ["hit"]

Output: "ball"

Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

Constraints:
1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
"""

"""
HELP TAKEN:

. removing punctuations from string using string.punctuation
. restructuring one line conditionals for correct results

<action 1 on ele> if (condition 1) else <action 2 on ele> for element in iterable 
"""

import string
from typing import Counter

def most_common_word(paragraph: str, banned: list[str]) -> str:
    curated_para = "".join(char if char not in string.punctuation else " " for char
                           in paragraph).lower()

    para_word_counts = Counter(curated_para.split())

    for w in banned:
        if w in para_word_counts:
            para_word_counts.pop(w)

    return para_word_counts.most_common()[0][0]

paragraph = input("Enter text: ")
banned = input("Enter words to ban: ").split()
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
print(most_common_word(paragraph, banned))
