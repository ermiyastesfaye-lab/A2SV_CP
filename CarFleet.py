class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mtrx = [[p, s] for p, s in zip(position, speed)]
        stack = []
        mtrx = sorted(mtrx)[::-1]
        for p, s in mtrx:
            res = (target-p)/s
            stack.append(res)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
