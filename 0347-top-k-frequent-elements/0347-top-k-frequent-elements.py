class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)   # Step 1: frequency count
        
        # Step 2: get k most frequent elements
        return heapq.nlargest(k, count.keys(), key=count.get)