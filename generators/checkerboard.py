class CheckerboardGenerator:
    """
    Generates deterministic checkerboard binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - transition stress testing
        - signal integrity analysis
        - coupling analysis
        - memory interface validation
        - alternating bit-pattern stress

    Output:
        Raw binary byte stream.
    """

    pattern_name = "CHECKERBOARD"
    deterministic = True
    pattern_type = "TRANSITION_STRESS"

    BYTE_LIMIT = 0xFF

    def __init__(
        self,
        size_in_bytes: int,
        base_pattern: int
    ):
        """
        Initialize checkerboard generator configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern in bytes.

            base_pattern (int):
                Base byte pattern used to generate
                alternating inverse sequence.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError("size_in_bytes must be an integer.")

        if size_in_bytes <= 0:
            raise ValueError(
                "size_in_bytes must be greater than zero."
            )

        if not isinstance(base_pattern, int):
            raise TypeError("base_pattern must be an integer.")

        if not (0 <= base_pattern <= self.BYTE_LIMIT):
            raise ValueError(
                "base_pattern must be between 0 and 255."
            )

        self.size_in_bytes = size_in_bytes
        self.base_pattern = base_pattern

        self.inverse_pattern = (
            ~self.base_pattern
        ) & self.BYTE_LIMIT

    def generate(self) -> bytes:
        """
        Generate checkerboard binary pattern.

        Returns:
            bytes:
                Alternating checkerboard byte stream.
        """

        generated_data = bytearray()

        alternating_patterns = (
            self.base_pattern,
            self.inverse_pattern
        )

        for index in range(self.size_in_bytes):

            pattern_byte = alternating_patterns[
                index % 2
            ]

            generated_data.append(pattern_byte)

        return bytes(generated_data)