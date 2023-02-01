class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        for c in s1:
            target[c] = target.get(c, 0) + 1

        for i in range(0, len(s2) - len(s1) + 1):
            curr_sub_str_dict = {}
            for j in s2[i:i + len(s1)]:
                curr_sub_str_dict[j] = curr_sub_str_dict.get(j, 0) + 1
            if curr_sub_str_dict == target:
                return True

        return False
