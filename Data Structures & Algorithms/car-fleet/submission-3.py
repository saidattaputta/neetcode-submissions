class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        cars = sorted(zip(position,speed))

        for p,vel in cars[::-1]:
            dist = target - p
            time = dist/vel

            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)