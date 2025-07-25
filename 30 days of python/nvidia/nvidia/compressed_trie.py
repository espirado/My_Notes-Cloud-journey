class PatriciaTrieNode:
    def __init__(self, label=""):
        self.label = label
        self.children = {}  # key: first char of child label, value: PatriciaTrieNode
        self.is_word = False

class PatriciaTrie:
    def __init__(self):
        self.root = PatriciaTrieNode()

    def insert(self, word):
        node = self.root
        i = 0
        while i < len(word):
            c = word[i]
            if c in node.children:
                child = node.children[c]
                label = child.label
                j = 0
                while j < len(label) and i + j < len(word) and word[i + j] == label[j]:
                    j += 1
                if j == len(label):
                    node = child
                    i += j
                else:
                    existing_child = PatriciaTrieNode(label[j:])
                    existing_child.children = child.children
                    existing_child.is_word = child.is_word

                    new_child = PatriciaTrieNode(word[i + j:])
                    new_child.is_word = True

                    child.label = label[:j]
                    child.children = {}
                    if existing_child.label:
                        child.children[existing_child.label[0]] = existing_child
                    if new_child.label:
                        child.children[new_child.label[0]] = new_child
                    child.is_word = child.is_word if j == len(label) and i + j == len(word) else False
                    return
            else:
                new_child = PatriciaTrieNode(word[i:])
                new_child.is_word = True
                node.children[c] = new_child
                return
        node.is_word = True

    def search(self, word):
        node = self.root
        i = 0
        while i < len(word):
            c = word[i]
            if c not in node.children:
                return False
            child = node.children[c]
            label = child.label
            if word[i:i+len(label)] != label:
                return False
            node = child
            i += len(label)
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        i = 0
        while i < len(prefix):
            c = prefix[i]
            if c not in node.children:
                return False
            child = node.children[c]
            label = child.label
            if prefix[i:i+len(label)] != label:
                return False
            node = child
            i += len(label)
        return True

    def autocomplete(self, prefix):
        node = self.root
        i = 0
        while i < len(prefix):
            c = prefix[i]
            if c not in node.children:
                return []
            child = node.children[c]
            label = child.label
            if prefix[i:i+len(label)] != label:
                return []
            node = child
            i += len(label)
        results = []
        def dfs(n, path):
            if n.is_word:
                results.append(prefix + path)
            for child in n.children.values():
                dfs(child, path + child.label)
        dfs(node, "")
        return results

if __name__ == "__main__":
    trie = PatriciaTrie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apex")
    trie.insert("bat")
    trie.insert("bath")
    trie.insert("banana")
    print(trie.search("apple"))      # True
    print(trie.search("appl"))       # False
    print(trie.starts_with("app"))   # True
    print(trie.autocomplete("ba"))   # ['bat', 'bath', 'banana'] 