from typing import List


class Solution:
    def find_warmer_day_idx(self, curr_temp, start_find_idx, temp_ls):
        for i in range(start_find_idx, len(temp_ls)):
            if temp_ls[i] > curr_temp:
                return i
        return None

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            warmer_idx = self.find_warmer_day_idx(curr_temp, i + 1, temperatures)
            if warmer_idx:
                res.append(warmer_idx - i)
            else:
                res.append(0)
        return res


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
