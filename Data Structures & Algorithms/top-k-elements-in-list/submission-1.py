class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        maps = {}
        for num in nums:
            maps[num] = maps.get(num,0)+1
        sorted_map = sorted(maps,key=maps.get,reverse=True)
        return sorted_map[:k]