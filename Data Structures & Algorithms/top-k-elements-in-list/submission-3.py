class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = {}

        for num in nums:
            dict[num] = dict.get(num,0)+1
        
        sorted_dict = sorted(dict,key=dict.get,reverse=True)
        return sorted_dict[:k]