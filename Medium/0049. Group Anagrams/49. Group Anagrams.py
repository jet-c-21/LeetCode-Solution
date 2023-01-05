from typing import List


class Solution:
    def get_char_tuple(self, word: str) -> tuple:
        temp = [0] * 26
        for c in word:
            c_idx = ord(c) - ord('a')
            temp[c_idx] += 1
        return tuple(temp)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ct_dict = {}
        for word in strs:
            ct = self.get_char_tuple(word)
            if ct not in ct_dict.keys():
                ct_dict[ct] = [word]
            else:
                ct_dict[ct].append(word)

        return list(ct_dict.values())
