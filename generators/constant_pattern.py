class ConstantPatternGenerator:
    """
    Generates deterministic repeating constant binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - alignment verification
        - endian debugging
        - lane ordering analysis
        - corruption visibility
        - protocol signature testing

    Output:
        Raw binary byte stream.
    """

    pattern_name = "CONSTANT_PATTERN"
    deterministic = True
    pattern_type = "STATIC"

    def __init__(
        self,
        size_in_bytes: int,
        pattern: bytes
    ):
        """
        Initialize constant pattern generator configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern in bytes.

            pattern (bytes):
                Repeating byte sequence.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError("size_in_bytes must be an integer.")

        if size_in_bytes <= 0:
            raise ValueError(
                "size_in_bytes must be greater than zero."
            )

        if not isinstance(pattern, bytes):
            raise TypeError("pattern must be of type bytes.")

        if len(pattern) == 0:
            raise ValueError("pattern cannot be empty.")

        self.size_in_bytes = size_in_bytes
        self.pattern = pattern

    def generate(self) -> bytes:
        """
        Generate repeating constant binary pattern.

        Returns:
            bytes:
                Repeating constant byte stream.
        """

        generated_data = bytearray()

        pattern_length = len(self.pattern)

        for index in range(self.size_in_bytes):

            pattern_byte = self.pattern[
                index % pattern_length
            ]

            generated_data.append(pattern_byte)

        return bytes(generated_data)