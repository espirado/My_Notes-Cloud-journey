import hashlib
import bisect
from typing import Any, Dict, List

class ConsistentHashRing:
    def __init__(self, replicas: int = 100):
        self.replicas = replicas  # Default virtual nodes per weight=1
        self.ring: List[tuple[int, str]] = []  # Sorted list of (hash, vnode_id)
        self.vnode_map: Dict[str, str] = {}    # vnode_id -> physical node
        self.node_weights: Dict[str, int] = {} # node_id -> weight

    def _hash(self, key: Any) -> int:
        return int(hashlib.md5(str(key).encode()).hexdigest(), 16)

    def add_node(self, node_id: str, weight: int = 1):
        self.node_weights[node_id] = weight
        for i in range(self.replicas * weight):
            vnode_id = f"{node_id}-vnode-{i}"
            h = self._hash(vnode_id)
            bisect.insort(self.ring, (h, vnode_id))
            self.vnode_map[vnode_id] = node_id

    def remove_node(self, node_id: str):
        self.node_weights.pop(node_id, None)
        to_remove = [v for v in self.vnode_map if self.vnode_map[v] == node_id]
        for vnode_id in to_remove:
            h = self._hash(vnode_id)
            idx = bisect.bisect_left(self.ring, (h, vnode_id))
            if idx < len(self.ring) and self.ring[idx][1] == vnode_id:
                self.ring.pop(idx)
            self.vnode_map.pop(vnode_id)

    def get_node(self, key: Any) -> str:
        if not self.ring:
            raise Exception("No nodes in the ring")
        h = self._hash(key)
        idx = bisect.bisect(self.ring, (h, ""))
        if idx == len(self.ring):
            idx = 0
        vnode_id = self.ring[idx][1]
        return self.vnode_map[vnode_id]

    def rebalance(self):
        # In this design, rebalancing is automatic on add/remove
        pass

# Example usage for interview prep
def _example():
    ring = ConsistentHashRing()
    ring.add_node("A", weight=2)
    ring.add_node("B", weight=1)
    ring.add_node("C", weight=3)

    print("Key 'my_key_1' maps to node:", ring.get_node("my_key_1"))
    print("Key 'my_key_2' maps to node:", ring.get_node("my_key_2"))

    ring.remove_node("B")  # B fails
    print("After removing B:")
    print("Key 'my_key_1' maps to node:", ring.get_node("my_key_1"))
    print("Key 'my_key_2' maps to node:", ring.get_node("my_key_2"))

if __name__ == "__main__":
    _example() 