import math

class MemoryBlock:
    def __init__(self, start, size):
        self.start = start  # Simulated address (offset)
        self.size = size

class MemoryPool:
    def __init__(self, pool_size, block_size, alignment):
        self.pool_size = pool_size
        self.block_size = block_size
        self.alignment = alignment
        self.memory = bytearray(pool_size)  # Simulated memory
        self.free_list = []
        # Precompute aligned block starts
        offset = 0
        while offset + block_size <= pool_size:
            aligned_offset = ((offset + alignment - 1) // alignment) * alignment
            if aligned_offset + block_size <= pool_size:
                self.free_list.append(MemoryBlock(aligned_offset, block_size))
            offset = aligned_offset + block_size

    def allocate(self):
        """Allocate a block from the pool, ensuring alignment."""
        if not self.free_list:
            raise MemoryError("Out of memory in pool")
        return self.free_list.pop()

    def free(self, block):
        """Return a block to the pool for reuse."""
        self.free_list.append(block)

# Example usage
if __name__ == "__main__":
    pool = MemoryPool(pool_size=1024, block_size=64, alignment=32)
    blocks = []
    for _ in range(5):
        block = pool.allocate()
        print(f"Allocated block at offset {block.start}, size {block.size}")
        blocks.append(block)
    pool.free(blocks[2])
    print("Freed one block.")
    block = pool.allocate()
    print(f"Re-allocated block at offset {block.start}, size {block.size}") 