from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        t = len(words)
        if t == 1:
            return words
        
        l = [words[0]]  
        
        for i in range(1, t):
    
            if groups[i] != groups[i - 1]:
                l.append(words[i])

        return l
