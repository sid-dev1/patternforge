class WalkingNibbleGenerator:
    """
    Generates deterministic walking-nibble binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - nibble-lane validation
        - grouped transition analysis
        - partial bus stress testing
        - structured bit movement analysis

    Output:
        Raw binary byte stream.
    """

    pattern_name = "WALKING_NIBBLE"
    deterministic = True
    pattern_type = "STRUCTURED_SHIFT"

    DOMAIN_WIDTH_BITS = 16
    NIBBLE_WIDTH_BITS = 4

    START_PATTERN = 0x000F

    def __init__(self, size_in_bytes: int):
        """
        Initialize walking-nibble generator configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern in bytes.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError(
                "size_in_bytes must be an integer."
            )

        if size_in_bytes <= 0:
            raise ValueError(
                "size_in_bytes must be greater than zero."
            )

        self.size_in_bytes = size_in_bytes

    def generate(self) -> bytes:
        """
        Generate walking-nibble binary pattern.

        Returns:
            bytes:
                Walking-nibble byte stream.
        """

        generated_data = bytearray()

        current_pattern = self.START_PATTERN

        while len(generated_data) < self.size_in_bytes:

            pattern_bytes = current_pattern.to_bytes(
                length=2,
                byteorder="big"
            )

            remaining_bytes = (
                self.size_in_bytes
                - len(generated_data)
            )

            generated_data.extend(
                pattern_bytes[:remaining_bytes]
            )

            current_pattern <<= self.NIBBLE_WIDTH_BITS

            if current_pattern >= (
                1 << self.DOMAIN_WIDTH_BITS
            ):
                current_pattern = self.START_PATTERN

        return bytes(generated_data)