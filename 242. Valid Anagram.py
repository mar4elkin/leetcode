class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = [0]*(ord('z')-ord('a')+1)
        hash_t = [0]*(ord('z')-ord('a')+1)

        for i in s:
            hash_s[ord(i)-ord('a')] += 1
        
        for k in t:
            hash_t[ord(k)-ord('a')] += 1
        
        return hash_s == hash_t