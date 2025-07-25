import bisect
import hashlib

class BloomFilter:
    def __init__(self, size=1024, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bits = [0] * size

    def _hashes(self, key):
        return [int(hashlib.md5((str(key)+str(i)).encode()).hexdigest(), 16) % self.size for i in range(self.hash_count)]

    def add(self, key):
        for h in self._hashes(key):
            self.bits[h] = 1

    def __contains__(self, key):
        return all(self.bits[h] for h in self._hashes(key))

class SSTable:
    def __init__(self, items):
        self.items = sorted(items)  # list of (key, value)
        self.bloom = BloomFilter()
        for k, _ in self.items:
            self.bloom.add(k)

    def get(self, key):
        if key not in self.bloom:
            return None
        i = bisect.bisect_left(self.items, (key, None))
        if i < len(self.items) and self.items[i][0] == key:
            return self.items[i][1]
        return None

    def range_query(self, start, end):
        i = bisect.bisect_left(self.items, (start, None))
        j = bisect.bisect_right(self.items, (end, None))
        return self.items[i:j]

class LSMTree:
    def __init__(self, memtable_limit=5):
        self.memtable = {}
        self.sstables = []
        self.memtable_limit = memtable_limit

    def put(self, key, value):
        self.memtable[key] = value
        if len(self.memtable) >= self.memtable_limit:
            self.flush()

    def get(self, key):
        if key in self.memtable:
            return self.memtable[key]
        for sstable in self.sstables:
            v = sstable.get(key)
            if v is not None:
                return v
        return None

    def flush(self):
        if self.memtable:
            self.sstables.insert(0, SSTable(list(self.memtable.items())))
            self.memtable = {}
            if len(self.sstables) > 3:  # simple compaction trigger
                self.compact()

    def compact(self):
        # Merge the two oldest SSTables
        if len(self.sstables) < 2:
            return
        s1 = self.sstables.pop()
        s2 = self.sstables.pop()
        merged = {}
        for k, v in s1.items + s2.items:
            merged[k] = v
        self.sstables.append(SSTable(list(merged.items())))

    def range_query(self, start, end):
        result = []
        # Check memtable
        for k, v in self.memtable.items():
            if start <= k <= end:
                result.append((k, v))
        # Merge results from SSTables
        for sstable in self.sstables:
            result.extend(sstable.range_query(start, end))
        # Remove duplicates (keep latest)
        result.sort()
        dedup = {}
        for k, v in result:
            dedup[k] = v
        return sorted(dedup.items())

# Example usage
if __name__ == "__main__":
    lsm = LSMTree(memtable_limit=3)
    lsm.put('a', 1)
    lsm.put('b', 2)
    lsm.put('c', 3)
    lsm.put('d', 4)  # triggers flush
    lsm.put('e', 5)
    print(lsm.get('a'))  # 1
    print(lsm.range_query('b', 'e'))  # [('b', 2), ('c', 3), ('d', 4), ('e', 5)] 