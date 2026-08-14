def word_pattern(pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        elif len(set(pattern)) != len(set(words)):
            return False
        else:
            pattern_map = {}
            for char, word in zip(pattern, words):
                if char not in pattern_map:
                    pattern_map[char] = word
                else:
                    if pattern_map[char] != word:
                        return False
            return True

pattern = "abba"
s = "dog cat cat dog"
print(word_pattern(pattern, s))