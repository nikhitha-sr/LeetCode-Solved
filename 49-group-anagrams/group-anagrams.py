class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []; anagram = {}; list_word =[]
        for word in strs:
            list_word = tuple(sorted(word))
            if list_word in anagram:
                anagram[list_word] = anagram[list_word] +[word]
            else:
                anagram[list_word] = [word]
        output = [value for value in anagram.values()]
        return output 