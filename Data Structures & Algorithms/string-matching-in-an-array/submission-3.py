class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for test_word in words:
            for word in words:
                if test_word != word:
                    if test_word in word:
                        substrings.append(test_word)
                        break
        return substrings
        



        