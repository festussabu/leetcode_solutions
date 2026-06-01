class TimeMap:

    def __init__(self):
        self.h_s = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.h_s:
            self.h_s[key] = []
        self.h_s[key].append((timestamp, value))
        # return ""

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h_s:
            return ""
        arr = self.h_s[key]
        l = 0
        r = len(arr) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1))
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))         
print(timeMap.set("foo", "bar2", 4)) 
print(timeMap.get("foo", 4))         
print(timeMap.get("foo", 5))         
