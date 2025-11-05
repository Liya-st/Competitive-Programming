from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}   # key -> value
        self.count = {}   # key -> frequency
        self.freq = defaultdict(list)  # freq -> list of keys
        self.lfu = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        oldfreq = self.count[key]
        self.freq[oldfreq].remove(key)
        if self.lfu == oldfreq and len(self.freq[oldfreq]) == 0:
            self.lfu += 1

        self.count[key] = oldfreq + 1
        self.freq[oldfreq + 1].append(key)

        return self.cache[key]
    

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.cache:
            oldfreq = self.count[key]
            self.freq[oldfreq].remove(key)
            if self.lfu == oldfreq and len(self.freq[oldfreq]) == 0:
                self.lfu += 1
            self.count[key] = oldfreq + 1
            self.freq[oldfreq + 1].append(key)
            self.cache[key] = value
            return

        if len(self.cache) == self.cap:
            evict_key = self.freq[self.lfu].pop(0)
            del self.cache[evict_key]
            del self.count[evict_key]
            if len(self.freq[self.lfu]) == 0:
                del self.freq[self.lfu]

        self.cache[key] = value
        self.count[key] = 1
        self.freq[1].append(key)
        self.lfu = 1
