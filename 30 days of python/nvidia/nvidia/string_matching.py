import re
import difflib
from collections import deque, defaultdict

# KMP Algorithm
def kmp_search(text, pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    res = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            res.append(i - j + 1)
            j = lps[j-1]
    return res

# Boyer-Moore (bad character heuristic)
def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return []
    bad_char = {c: -1 for c in set(text)}
    for i, c in enumerate(pattern):
        bad_char[c] = i
    res = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            res.append(s)
            s += m - bad_char.get(text[s + m], -1) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return res

# Aho-Corasick (multi-pattern search)
class AhoCorasickNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []

class AhoCorasick:
    def __init__(self, patterns):
        self.root = AhoCorasickNode()
        for idx, pat in enumerate(patterns):
            node = self.root
            for c in pat:
                node = node.children.setdefault(c, AhoCorasickNode())
            node.output.append(idx)
        queue = deque()
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)
        while queue:
            rnode = queue.popleft()
            for c, unode in rnode.children.items():
                queue.append(unode)
                fnode = rnode.fail
                while fnode and c not in fnode.children:
                    fnode = fnode.fail
                unode.fail = fnode.children[c] if fnode and c in fnode.children else self.root
                unode.output += unode.fail.output if unode.fail else []
    def search(self, text):
        node = self.root
        results = []
        for i, c in enumerate(text):
            while node and c not in node.children:
                node = node.fail
            if not node:
                node = self.root
                continue
            node = node.children[c]
            for pat_idx in node.output:
                results.append((i, pat_idx))
        return results

# Regex search
def regex_search(text, pattern):
    return [m.start() for m in re.finditer(pattern, text)]

# Fuzzy search (approximate matching)
def fuzzy_search(text, pattern, max_dist=2):
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        window = text[i:i+len(pattern)]
        if difflib.SequenceMatcher(None, window, pattern).ratio() >= 1 - max_dist/len(pattern):
            matches.append(i)
    return matches

# Example usage
if __name__ == "__main__":
    log = "error at line 10: disk full. warning at line 20: cpu high. error at line 30: memory leak."
    print("KMP:", kmp_search(log, "error"))
    print("Boyer-Moore:", boyer_moore_search(log, "warning"))
    ac = AhoCorasick(["error", "warning", "disk"])
    print("Aho-Corasick:", ac.search(log))
    print("Regex:", regex_search(log, r"line \\d+"))
    print("Fuzzy:", fuzzy_search(log, "memry leak", max_dist=2)) 