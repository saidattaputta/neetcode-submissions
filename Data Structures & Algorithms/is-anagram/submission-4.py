class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        maps = {}

        for char in s:
            maps[char] = maps.get(char,0)+1
        
        for char in t:
            if char not in maps or maps[char] == 0:
                return False
            maps[char] -= 1
        return True