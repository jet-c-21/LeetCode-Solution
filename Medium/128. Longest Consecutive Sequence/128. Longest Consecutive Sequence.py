from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in num_set:
                seq_len = 0
                while n + seq_len in num_set:
                    seq_len += 1

                longest = max(longest, seq_len)

        return longest
