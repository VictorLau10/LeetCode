# 884. Uncommon Words from Two Sentences
# Sep 17, 2024
# Beats 12.92% Runtime
# Beats 47.12% Memory

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        d = {}
        s = s1 + " " + s2
        lst = s.split()
        uncommon = []
        for word in lst:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

        for word in d:
            if d[word] == 1:
                uncommon.append(word)

        return uncommon

        
