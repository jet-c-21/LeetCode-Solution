class TimeMap:

    def __init__(self):
        self.store = {}  # key : list of (val, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        val = self.store.get(key, [])
        # binary search

        l_idx, r_idx = 0, len(val) - 1
        while r_idx >= l_idx:
            m_idx = (l_idx + r_idx) // 2
            if val[m_idx][1] < timestamp:
                res = val[m_idx][0]
                l_idx = m_idx + 1

            elif val[m_idx][1] == timestamp:
                res = val[m_idx][0]
                break

            else:
                r_idx = m_idx - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
