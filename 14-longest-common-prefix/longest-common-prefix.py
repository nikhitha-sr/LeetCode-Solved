class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word=strs[0]

        for word in strs:
            while not word.startswith(first_word):
                first_word=first_word[:-1]
        return first_word        
                