class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            words1 = defaultdict(int)
            for x in s:
                words1[x] += 1
            words2 = defaultdict(int)
            for y in t:
                words2[y] += 1
            if (words1 != words2):
                return False
            else:
                return True