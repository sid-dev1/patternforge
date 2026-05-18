class BurstPatternGenerator:
    """
    Generates deterministic burst-style binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - DMA burst simulation
        - cacheline behavior analysis
        - burst-transfer validation
        - FIFO stress testing
        - grouped traffic simulation

    Output:
        Raw binary byte stream.
    """

    pattern_name = "BURST_PATTERN"
    deterministic = True
    pattern_type = "BURST"

    def __init__(
        self,
        size_in_bytes: int,
        pattern_a: bytes,
        pattern_b: bytes,
        burst_length_in_bytes: int
    ):
        """
        Initialize burst pattern generator configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern in bytes.

            pattern_a (bytes):
                First burst pattern sequence.

            pattern_b (bytes):
                Second burst pattern sequence.

            burst_length_in_bytes (int):
                Burst size for each alternating pattern block.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError(
                "size_in_bytes must be an integer."
            )

        if size_in_bytes <= 0:
            raise ValueError(
                "size_in_bytes must be greater than zero."
            )

        if not isinstance(pattern_a, bytes):
            raise TypeError(
                "pattern_a must be of type bytes."
            )

        if len(pattern_a) == 0:
            raise ValueError(
                "pattern_a cannot be empty."
            )

        if not isinstance(pattern_b, bytes):
            raise TypeError(
                "pattern_b must be of type bytes."
            )

        if len(pattern_b) == 0:
            raise ValueError(
                "pattern_b cannot be empty."
            )

        if not isinstance(
            burst_length_in_bytes,
            int
        ):
            raise TypeError(
                "burst_length_in_bytes must be an integer."
            )

        if burst_length_in_bytes <= 0:
            raise ValueError(
                "burst_length_in_bytes must be greater than zero."
            )

        self.size_in_bytes = size_in_bytes
        self.pattern_a = pattern_a
        self.pattern_b = pattern_b
        self.burst_length_in_bytes = (
            burst_length_in_bytes
        )

    def _generate_burst_block(
        self,
        pattern: bytes
    ) -> bytearray:
        """
        Generate a single burst block using
        repeating pattern bytes.

        Args:
            pattern (bytes):
                Pattern used for burst generation.

        Returns:
            bytearray:
                Generated burst block.
        """

        burst_block = bytearray()

        pattern_length = len(pattern)

        for index in range(
            self.burst_length_in_bytes
        ):

            pattern_byte = pattern[
                index % pattern_length
            ]

            burst_block.append(pattern_byte)

        return burst_block

    def generate(self) -> bytes:
        """
        Generate deterministic burst binary pattern.

        Returns:
            bytes:
                Burst-pattern byte stream.
        """

        generated_data = bytearray()

        burst_patterns = (
            self.pattern_a,
            self.pattern_b
        )

        burst_index = 0

        while len(generated_data) < self.size_in_bytes:

            current_pattern = burst_patterns[
                burst_index % 2
            ]

            burst_block = self._generate_burst_block(
                current_pattern
            )

            remaining_bytes = (
                self.size_in_bytes
                - len(generated_data)
            )

            generated_data.extend(
                burst_block[:remaining_bytes]
            )

            burst_index += 1

        return bytes(generated_data)