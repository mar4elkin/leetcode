class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls = []
        lt = []

        for idx, x in enumerate(s):
            if x == '#':
                if len(ls) > 0:
                    ls.pop()
            else:
                ls.append(x)
        for idx, x in enumerate(t):
            if x == '#':
                if len(lt) > 0:
                    lt.pop()
            else:
                lt.append(x)

        return ls == lt