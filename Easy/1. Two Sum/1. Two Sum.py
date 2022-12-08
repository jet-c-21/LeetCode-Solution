class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_idx_dict = dict()

        for i, n in enumerate(nums):
            diff = target - n
            if diff in n_idx_dict.keys():
                return [n_idx_dict[diff], i]
            n_idx_dict[n] = i
