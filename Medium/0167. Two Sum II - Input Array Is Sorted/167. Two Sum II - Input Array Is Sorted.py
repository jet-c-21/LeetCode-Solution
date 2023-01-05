from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while (numbers[l] + numbers[r]) != target:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1

        return [l + 1, r + 1]
