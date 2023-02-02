class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''

        window, t_count = {}, {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l_idx = 0
        for r_idx in range(len(s)):
            c = s[r_idx]
            window[c] = window.get(c, 0) + 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                # update result
                if (r_idx - l_idx + 1) < res_len:
                    res = [l_idx, r_idx]
                    res_len = (r_idx - l_idx + 1)

                # pop from the left of window
                window[s[l_idx]] -= 1
                if s[l_idx] in t_count and window[s[l_idx]] < t_count[s[l_idx]]:
                    have -= 1
                l_idx += 1

        l_idx, r_idx = res
        return s[l_idx:r_idx + 1] if res_len != float('inf') else ''
