class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}
        left = 0
        long = 0
        maxfreq = 0

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0)+1
            maxfreq = max(maxfreq,seen[s[right]])
            if (right-left+1) - maxfreq > k:
                seen[s[left]] -= 1
                left+=1
            long = max(long,right-left+1)
        return long