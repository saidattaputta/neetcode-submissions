class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}

        left = 0
        maxfreq = 0
        longest = 0

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0)+1
            maxfreq = max(seen[s[right]],maxfreq)

            while (right-left+1) - maxfreq > k:
                seen[s[left]] -= 1
                left +=1

            longest = max(right-left+1,longest)
        return longest
