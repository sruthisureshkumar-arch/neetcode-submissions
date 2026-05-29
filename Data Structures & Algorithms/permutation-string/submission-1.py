
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        target = Counter(s1)

        for i in range(len(s2) - k + 1):
            if Counter(s2[i:i+k]) == target:
                return True

        return False
        