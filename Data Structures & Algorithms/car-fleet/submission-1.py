class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed))
        stack = []

        for pos,spe in cars[::-1]:
            time = (target - pos)/spe

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)