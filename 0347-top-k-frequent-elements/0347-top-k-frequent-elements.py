from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency (Hash Table / Counting)
        count = Counter(nums)

        # Step 2: Create buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Fill buckets
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Collect top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result