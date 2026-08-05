class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed))
        stack = []

        for p,v in cars[::-1]:
            t = (target-p)/v
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)