class TimeMap:

    def __init__(self):
        self.hs = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hs:
            self.hs[key] = []
        self.hs[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hs:
            return ""
        lst = self.hs[key]
        print(lst, timestamp)
        l, r = 0, len(lst) - 1
        while l < r - 1:
            m = (l + r) // 2
            print(l,r,m)
            if lst[m][0] == timestamp:
                return lst[m][1]
            elif lst[m][0] > timestamp:
                r = m
            else:
                l = m
        if lst[r][0] <= timestamp:
            return lst[r][1]
        if lst[l][0] <= timestamp:
            return lst[l][1]
        return ""

        
