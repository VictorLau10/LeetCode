# 1331. Rank Transform of an Array
# Oct 3, 2024
# Beats 5.04% Runtime
# Beats 5.00% Memory

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Create a list of lists with the number being the first element and its index being the second
        indexList = []
        for i in range ( len(arr) ):
            indexList.append( [arr[i], i] )

        indexList.sort()
        
        # Add third element to be the rank
        rank = 1
        i = 0
        while i < len(indexList):
            if i > 0 and indexList[i - 1][0] == indexList[i][0]:
                indexList[i].append( indexList[i-1][2] )
            else:
                indexList[i].append(rank)
                rank += 1
            i += 1

        # Edit original array with new ranks
        for i in range ( len(indexList) ):
            arr[ indexList[i][1] ] = indexList[i][2]

        return(arr)

 
