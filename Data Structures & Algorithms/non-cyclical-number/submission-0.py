class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:

            if n in seen:
                return False
            seen.add(n)
            summ = 0
            while n >0:
                d = n%10
                n = n//10
                summ += d*d
            n = summ
        return True