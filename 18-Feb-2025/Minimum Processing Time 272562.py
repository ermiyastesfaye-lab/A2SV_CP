# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        n = len(tasks)
        jump = n//len(processorTime)
        res, ind, ans = 0 ,0, 0
        for w in range(n):
            tasks[w] += processorTime[ind]
            res = max(res, tasks[w])
            if not (w+1)%jump:
                ind += 1
                ans = max(res, ans)
                res = 0
        return ans


        # for right in range(idx):
        #     processorTime[]

        

        