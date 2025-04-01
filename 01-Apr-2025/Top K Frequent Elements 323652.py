# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for val, freq in cnt.items():
            bucket[freq].append(val)
        return list(chain(*bucket[::-1]))[:k]      

        



        