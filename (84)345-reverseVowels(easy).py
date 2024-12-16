# 345. Reverse Vowels of a String
# Oct 6, 2024
# Beats 12.52% Runtime
# Beats 12.38% Memory

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        lst = []

        for ch in s:
            if ch in st:
                lst.append(ch)

        string = ""
        for i in range(len(s)):
            if s[i] in st:
                string += lst.pop()
            else:
                string += s[i]
                
        return string
