class TimeMap:

    def __init__(self):
        self.hashmap = dict()
        self.timestamp_key = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hashmap.get(key):
            self.hashmap[key][timestamp] = value
        else:
            self.hashmap[key] = {timestamp: value}

        if self.timestamp_key.get(key):
            self.timestamp_key[key].append(timestamp)
        else:
            self.timestamp_key[key] = [ timestamp, ]

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        times = self.timestamp_key.get(key)
        times.sort()

        low, high = 0, len(times) - 1

        while low <= high:
            mid = (low + high) // 2

            if times[mid] > timestamp:
                high = mid - 1
            else:
                low = mid + 1

        if high < 0:
            return ""

        answer = self.hashmap[key][times[high]]
        return answer

        
        
        
