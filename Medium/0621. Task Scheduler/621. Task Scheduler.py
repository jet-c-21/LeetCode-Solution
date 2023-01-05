import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        min_heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(min_heap)

        time = 0
        queue = []

        while min_heap or queue:
            time += 1

            if min_heap:
                count = 1 + heapq.heappop(min_heap)
                if count:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(min_heap, queue.pop(0)[0])

        return time


if __name__ == '__main__':
    tasks = ['A', 'A', 'A', 'B', 'B', 'C', 'C']

    ans = Solution().leastInterval(tasks, 1)
    print(ans)
