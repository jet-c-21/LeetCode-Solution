from typing import List


class Solution:
    def merge(self, l_ls: list, r_ls: list) -> list:
        res = []
        l_idx, r_idx = 0, 0
        while l_idx < len(l_ls) and r_idx < len(r_ls):
            if l_ls[l_idx] < r_ls[r_idx]:
                res.append(l_ls[l_idx])
                l_idx += 1
            else:
                res.append(r_ls[r_idx])
                r_idx += 1

        # add remaining
        res += l_ls[l_idx:]
        res += r_ls[r_idx:]

        return res

    def merge_sort(self, ls) -> list:
        if len(ls) < 2:
            return ls

        mid_idx = len(ls) // 2

        l_ls = self.merge_sort(ls[:mid_idx])
        r_ls = self.merge_sort(ls[mid_idx:])

        return self.merge(l_ls, r_ls)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = self.merge_sort(nums)

        # three_sum = a + b + c
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  # skip same value
                continue

            b_idx = i + 1
            c_idx = len(nums) - 1

            while b_idx < c_idx:
                three_sum = a + nums[b_idx] + nums[c_idx]
                if three_sum < 0:
                    b_idx += 1
                elif three_sum > 0:
                    c_idx -= 1
                else:
                    res.append([a, nums[b_idx], nums[c_idx]])
                    # [-2, -2, 0, 0, 2, 2]
                    b_idx += 1
                    while nums[b_idx] == nums[b_idx - 1] and b_idx < c_idx:
                        b_idx += 1

        return res
