class InverseIncrementalGenerator:
    """
    Generates deterministic inverse incremental
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - reverse sequence validation
        - complementary integrity analysis
        - decrement-based progression testing
        - transport corruption analysis

    Output:
        Raw binary byte stream.
    """

    pattern_name = "INVERSE_INCREMENTAL"
    deterministic = True
    pattern_type = "SEQUENTIAL"

    BYTE_LIMIT = 256

    def __init__(
        self,
        size_in_bytes: int,
        seed_value: int,
        decrement_value: int
    ):
        """
        Initialize inverse incremental generator
        configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern in bytes.

            seed_value (int):
                Starting byte value.

            decrement_value (int):
                Decrement step applied per byte.
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

        if not isinstance(decrement_value, int):
            raise TypeError(
                "decrement_value must be an integer."
            )

        if not (0 <= seed_value <= 255):
            raise ValueError(
                "seed_value must be between 0 and 255."
            )

        if not (0 <= decrement_value <= 255):
            raise ValueError(
                "decrement_value must be between 0 and 255."
            )

        self.size_in_bytes = size_in_bytes
        self.seed_value = seed_value
        self.decrement_value = decrement_value

    def generate(self) -> bytes:
        """
        Generate inverse incremental binary pattern.

        Returns:
            bytes:
                Inverse incremental byte stream.
        """

        generated_data = bytearray()

        current_value = self.seed_value

        for _ in range(self.size_in_bytes):

            generated_data.append(current_value)

            current_value = (
                current_value - self.decrement_value
            ) % self.BYTE_LIMIT

        return bytes(generated_data)