class GPUMemoryPool:
    def __init__(self, size):
        self.size = size
        self.free_blocks = [(0, size)]  # (offset, size)
        self.allocated = {}

    def alloc(self, size):
        # Find a free block (buddy or best-fit)
        for i, (off, sz) in enumerate(self.free_blocks):
            if sz >= size:
                self.allocated[off] = size
                if sz == size:
                    self.free_blocks.pop(i)
                else:
                    self.free_blocks[i] = (off + size, sz - size)
                return off  # Return offset as handle
        raise MemoryError("Out of GPU memory")

    def free(self, offset):
        size = self.allocated.pop(offset)
        self.free_blocks.append((offset, size))
        self.free_blocks = self._coalesce(self.free_blocks)

    def _coalesce(self, blocks):
        # Merge adjacent free blocks
        blocks.sort()
        merged = []
        for off, sz in blocks:
            if merged and merged[-1][0] + merged[-1][1] == off:
                merged[-1] = (merged[-1][0], merged[-1][1] + sz)
            else:
                merged.append((off, sz))
        return merged

# Example usage
if __name__ == "__main__":
    pool = GPUMemoryPool(1024)
    h1 = pool.alloc(128)
    h2 = pool.alloc(256)
    print("Allocated blocks at:", h1, h2)
    pool.free(h1)
    pool.free(h2)
    print("Free blocks:", pool.free_blocks) 