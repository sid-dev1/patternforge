import random

class RandomPatternGenerator:
    """
    Generates deterministic pseudo-random binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - fuzz-style testing
        - entropy-rich data generation
        - workload variability simulation
        - cache behavior analysis
        - generic transport stress testing

    Output:
        Raw binary byte stream.
    """

    pattern_name = "RANDOM_PATTERN"
    deterministic = True
    pattern_type = "RANDOM"

    BYTE_LIMIT = 256

    def __init__(
        self,
        size_in_bytes: int,
        seed_value: int
    ):
        """
        Initialize random pattern generator configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern in bytes.

            seed_value (int):
                Seed value for deterministic pseudo-random generation.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError("size_in_bytes must be an integer.")

        if size_in_bytes <= 0:
            raise ValueError(
                "size_in_bytes must be greater than zero."
            )

        if not isinstance(seed_value, int):
            raise TypeError("seed_value must be an integer.")

        self.size_in_bytes = size_in_bytes
        self.seed_value = seed_value

    def generate(self) -> bytes:
        """
        Generate deterministic pseudo-random binary pattern.

        Returns:
            bytes:
                Pseudo-random byte stream.
        """

        generated_data = bytearray()

        rng = random.Random(self.seed_value)

        for _ in range(self.size_in_bytes):

            random_byte = rng.randint(
                0,
                self.BYTE_LIMIT - 1
            )

            generated_data.append(random_byte)

        return bytes(generated_data)