class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        if s == t:
            return s

        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c,0)+1
        
        have = 0
        needcnt = len(need)
        res = [-1,-1]
        reslen = float('inf')
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            while have == needcnt:
                if (right - left +1) < reslen:
                    res = [left,right]
                    reslen = right-left+1
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right+1] if reslen != float('inf') else ""