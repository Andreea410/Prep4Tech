class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        while word1 and word2:
            new_word += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        new_word += word1
        new_word += word2
        return new_word
