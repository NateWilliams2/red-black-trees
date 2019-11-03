import math

TAP_BITS = [5, 3, 2, 0]
DEFAULT_SEED = 211


class lfsr:
    #constructor assigns default seed if none is provided
    def __init__(self, seed = DEFAULT_SEED):
        self.seed = seed % 256

    # gets next lfsr value from seed
    def nextValue(self):
        xor_bit = 0  # bit to store result of xor operations
        for bit in TAP_BITS:
         xor_bit ^= ((self.seed >> bit) & 1)
        self.seed = (self.seed >> 1) | (xor_bit << 7)
        return self.seed
