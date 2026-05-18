class IncrementalGenerator:
    """
    Generates deterministic incremental binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - data integrity verification
        - ordering validation
        - alignment analysis
        - missing/duplicated byte detection
        - transport corruption analysis

    Output:
        Raw binary byte stream.
    """

    pattern_name = "INCREMENTAL"
    deterministic = True
    pattern_type = "SEQUENTIAL"

    BYTE_LIMIT = 256

    def __init__(
        self,
        size_in_bytes: int,
        seed_value: int,
        increment_value: int
    ):
        """
        Initialize incremental generator configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern in bytes.

            seed_value (int):
                Starting byte value.

            increment_value (int):
                Increment step applied per byte.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError("size_in_bytes must be an integer.")

        if size_in_bytes <= 0:
            raise ValueError("size_in_bytes must be greater than zero.")

        if not isinstance(seed_value, int):
            raise TypeError("seed_value must be an integer.")

        if not isinstance(increment_value, int):
            raise TypeError("increment_value must be an integer.")

        if not (0 <= seed_value <= 255):
            raise ValueError("seed_value must be between 0 and 255.")

        if not (0 <= increment_value <= 255):
            raise ValueError("increment_value must be between 0 and 255.")

        self.size_in_bytes = size_in_bytes
        self.seed_value = seed_value
        self.increment_value = increment_value

    def generate(self) -> bytes:
        """
        Generate incremental binary pattern.

        Returns:
            bytes:
                Incremental byte stream.
        """

        generated_data = bytearray()

        current_value = self.seed_value

        for _ in range(self.size_in_bytes):
            generated_data.append(current_value)

            current_value = (
                current_value + self.increment_value
            ) % self.BYTE_LIMIT

        return bytes(generated_data)