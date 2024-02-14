class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash_s = [0]*(ord('z')-ord('a')+1)
        group = {}

        def dum_hash(val):
            _hash = [0]*(ord('z')-ord('a')+1)
            for i in val:
                _hash[ord(i)-ord('a')] += 1
            return tuple(_hash)

        for index, val in enumerate(strs):
            if dum_hash(val) in group:
                group[dum_hash(val)].append(val)
            else:
                group[dum_hash(val)] = [val]
        
        return group.values()
            