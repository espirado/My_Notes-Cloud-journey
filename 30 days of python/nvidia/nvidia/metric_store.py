import time
from collections import defaultdict

class MetricStore:
    def __init__(self, num_partitions=8):
        self.num_partitions = num_partitions
        self.partitions = [defaultdict(list) for _ in range(num_partitions)]
        self.downsampled = [defaultdict(list) for _ in range(num_partitions)]
        self.retention_seconds = 3600  # 1 hour raw retention

    def _partition(self, labels):
        # Simple hash of sorted label items
        return hash(frozenset(labels.items())) % self.num_partitions

    def write(self, timestamp, value, labels):
        p = self._partition(labels)
        self.partitions[p][frozenset(labels.items())].append((timestamp, value))

    def query(self, labels, start, end, downsample=False):
        p = self._partition(labels)
        key = frozenset(labels.items())
        data = self.downsampled[p][key] if downsample else self.partitions[p][key]
        return [(t, v) for t, v in data if start <= t <= end]

    def downsample(self, interval=60):
        # Aggregate to 1-min intervals
        for p in range(self.num_partitions):
            for key, points in self.partitions[p].items():
                buckets = defaultdict(list)
                for t, v in points:
                    bucket = int(t // interval) * interval
                    buckets[bucket].append(v)
                self.downsampled[p][key] = [(b, sum(vals)/len(vals)) for b, vals in buckets.items()]

    def enforce_retention(self):
        now = time.time()
        for p in range(self.num_partitions):
            for key in list(self.partitions[p].keys()):
                self.partitions[p][key] = [(t, v) for t, v in self.partitions[p][key] if t >= now - self.retention_seconds]

# Example usage
if __name__ == "__main__":
    store = MetricStore()
    now = time.time()
    for i in range(100):
        store.write(now + i, i, {"host": "a", "region": "us"})
    store.downsample()
    print(store.query({"host": "a", "region": "us"}, now, now + 100, downsample=True)) 