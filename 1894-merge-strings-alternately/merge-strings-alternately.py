class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = len(word1)
        extra_lettr = word2
        if len(word2) < length:
            length = len(word2)
            extra_lettr = word1
        elif length == len(word2):
            extra_lettr = ""              
        new_str=""
        for i in range(length):
            new_str = new_str + word1[i]+word2[i]
        new_str=new_str+extra_lettr[i+1:]
        return new_str


        