from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()  # index
        l_idx = r_idx = 0
        # O(n) O(n)
        while r_idx < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r_idx]:
                q.pop()
            q.append(r_idx)

            # remove left val from a window
            if l_idx > q[0]:
                q.popleft()

            if (r_idx + 1) >= k:
                res.append(nums[q[0]])
                l_idx += 1

            r_idx += 1

        return res


if __name__ == '__main__':
    nnn = [1, 3, -1, -3, 5, 3, 6, 7]
    kkk = 3
    print(Solution().maxSlidingWindow(nnn, kkk))
