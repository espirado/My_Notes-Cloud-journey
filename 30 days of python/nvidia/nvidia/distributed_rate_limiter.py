import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, config):
        """
        config: dict mapping (region, tier) -> (max_tokens, refill_rate_per_sec)
        Example: {('US', 'premium'): (10, 10), ('EU', 'free'): (5, 5)}
        """
        self.config = config
        self.buckets = defaultdict(lambda: {'tokens': 0, 'last': 0})

    def allow(self, user_id, region, tier):
        key = (user_id, region, tier)
        now = time.time()
        max_tokens, refill_rate = self.config[(region, tier)]
        bucket = self.buckets[key]
        # Refill tokens based on elapsed time
        elapsed = now - bucket['last']
        bucket['tokens'] = min(max_tokens, bucket['tokens'] + elapsed * refill_rate)
        bucket['last'] = now
        if bucket['tokens'] >= 1:
            bucket['tokens'] -= 1
            return True
        return False

# Example usage
if __name__ == "__main__":
    config = {
        ('US', 'premium'): (10, 10),  # 10 req/sec
        ('EU', 'free'): (5, 5),       # 5 req/sec
    }
    limiter = RateLimiter(config)
    for _ in range(12):
        print("US premium:", limiter.allow('user1', 'US', 'premium'))
    time.sleep(1)
    print("After 1 second refill:", limiter.allow('user1', 'US', 'premium'))
    for _ in range(7):
        print("EU free:", limiter.allow('user2', 'EU', 'free')) 