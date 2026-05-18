import random


class AIWorkloadPatternGenerator:
    """
    Generates deterministic AI-inspired workload
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - AI-style traffic simulation
        - sparse workload behavior
        - burst-transfer modeling
        - tensor locality emulation
        - mixed entropy traffic analysis

    Output:
        Raw binary byte stream.
    """

    pattern_name = "AI_WORKLOAD_PATTERN"
    deterministic = True
    pattern_type = "WORKLOAD"

    SPARSE_REGION_SIZE = 64
    RANDOM_REGION_SIZE = 64
    TENSOR_REGION_SIZE = 64
    BURST_REGION_SIZE = 64

    TENSOR_PATTERN = (
        b'\xAA\xBB\xCC\xDD'
    )

    BURST_PATTERN = (
        b'\xFF\xFF\xFF\xFF'
        b'\x00\x00\x00\x00'
    )

    BYTE_LIMIT = 256

    def __init__(
        self,
        size_in_bytes: int,
        seed_value: int
    ):
        """
        Initialize AI workload pattern generator
        configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern
                in bytes.

            seed_value (int):
                Seed value for deterministic
                pseudo-random workload regions.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError(
                "size_in_bytes must be an integer."
            )

        if size_in_bytes <= 0:
            raise ValueError(
                "size_in_bytes must be greater than zero."
            )

        if not isinstance(seed_value, int):
            raise TypeError(
                "seed_value must be an integer."
            )

        self.size_in_bytes = size_in_bytes
        self.seed_value = seed_value

    def _generate_sparse_region(self) -> bytearray:
        """
        Generate sparse zero-filled region.

        Returns:
            bytearray:
                Sparse region data.
        """

        return bytearray(
            b'\x00' * self.SPARSE_REGION_SIZE
        )

    def _generate_random_region(
        self,
        rng: random.Random
    ) -> bytearray:
        """
        Generate pseudo-random entropy region.

        Args:
            rng (random.Random):
                Deterministic random generator.

        Returns:
            bytearray:
                Random workload region.
        """

        region = bytearray()

        for _ in range(self.RANDOM_REGION_SIZE):

            region.append(
                rng.randint(
                    0,
                    self.BYTE_LIMIT - 1
                )
            )

        return region

    def _generate_tensor_region(self) -> bytearray:
        """
        Generate repeated tensor-style region.

        Returns:
            bytearray:
                Tensor locality region.
        """

        region = bytearray()

        pattern_length = len(
            self.TENSOR_PATTERN
        )

        for index in range(
            self.TENSOR_REGION_SIZE
        ):

            region.append(
                self.TENSOR_PATTERN[
                    index % pattern_length
                ]
            )

        return region

    def _generate_burst_region(self) -> bytearray:
        """
        Generate burst-transfer style region.

        Returns:
            bytearray:
                Burst-style traffic region.
        """

        region = bytearray()

        pattern_length = len(
            self.BURST_PATTERN
        )

        for index in range(
            self.BURST_REGION_SIZE
        ):

            region.append(
                self.BURST_PATTERN[
                    index % pattern_length
                ]
            )

        return region

    def generate(self) -> bytes:
        """
        Generate deterministic AI-inspired
        workload binary pattern.

        Returns:
            bytes:
                AI workload byte stream.
        """

        generated_data = bytearray()

        rng = random.Random(self.seed_value)

        while len(generated_data) < self.size_in_bytes:

            workload_regions = (
                self._generate_sparse_region(),
                self._generate_random_region(rng),
                self._generate_tensor_region(),
                self._generate_burst_region()
            )

            for region in workload_regions:

                remaining_bytes = (
                    self.size_in_bytes
                    - len(generated_data)
                )

                if remaining_bytes <= 0:
                    break

                generated_data.extend(
                    region[:remaining_bytes]
                )

        return bytes(generated_data)