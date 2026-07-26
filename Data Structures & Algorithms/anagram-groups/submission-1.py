class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        maps = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in maps:
                maps[key] = []
            maps[key].append(word)
        return list(maps.values())