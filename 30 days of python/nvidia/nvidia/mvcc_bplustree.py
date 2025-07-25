import threading
from typing import Any, List, Optional, Dict, Tuple

class LeafEntry:
    def __init__(self, key: Any, value: Any, created_version: int, deleted_version: Optional[int] = None):
        self.key = key
        self.value = value
        self.created_version = created_version
        self.deleted_version = deleted_version

class LeafNode:
    def __init__(self, entries: List[LeafEntry], next_leaf: Optional['LeafNode'] = None):
        self.entries = entries  # List[LeafEntry]
        self.next_leaf = next_leaf

class InternalNode:
    def __init__(self, keys: List[Any], children: List[Any]):
        self.keys = keys  # List of keys
        self.children = children  # List of child nodes

class MVCCBPlusTree:
    def __init__(self):
        self.root_versions: Dict[int, Any] = {}  # version -> root node
        self.current_version = 0
        self.lock = threading.Lock()  # For atomic version increment

    def _next_version(self) -> int:
        with self.lock:
            self.current_version += 1
            return self.current_version

    def insert(self, key: Any, value: Any):
        version = self._next_version()
        # Copy-on-write insert (simplified: single leaf node, no splits)
        prev_root = self.root_versions.get(self.current_version - 1)
        new_root = self._insert(prev_root, key, value, version)
        self.root_versions[version] = new_root
        return version

    def _insert(self, node: Optional[LeafNode], key: Any, value: Any, version: int) -> LeafNode:
        if node is None:
            entry = LeafEntry(key, value, version)
            return LeafNode([entry])
        # Copy node and add new entry
        new_entries = node.entries.copy()
        new_entries.append(LeafEntry(key, value, version))
        return LeafNode(new_entries, node.next_leaf)

    def range_query(self, start_key: Any, end_key: Any, version: int) -> List[Tuple[Any, Any]]:
        node = self.root_versions.get(version)
        result = []
        while node:
            for entry in node.entries:
                if start_key <= entry.key <= end_key:
                    if entry.created_version <= version and (entry.deleted_version is None or version < entry.deleted_version):
                        result.append((entry.key, entry.value))
            node = node.next_leaf
        return result

    def snapshot(self, version: int) -> Optional[Any]:
        return self.root_versions.get(version)

# Example usage for interview prep
def _example():
    tree = MVCCBPlusTree()
    v1 = tree.insert(1, 'a')
    v2 = tree.insert(2, 'b')
    v3 = tree.insert(3, 'c')
    print('Version 2:', tree.range_query(1, 3, 2))  # Should print [(1, 'a'), (2, 'b')]
    print('Version 3:', tree.range_query(1, 3, 3))  # Should print [(1, 'a'), (2, 'b'), (3, 'c')]

if __name__ == "__main__":
    _example() 