class WalkingByteGenerator:
    """
    Generates deterministic walking-byte binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - byte-lane validation
        - DMA alignment testing
        - structured bus analysis
        - serializer/deserializer validation
        - byte-group movement analysis

    Output:
        Raw binary byte stream.
    """

    pattern_name = "WALKING_BYTE"
    deterministic = True
    pattern_type = "STRUCTURED_SHIFT"

    DOMAIN_WIDTH_BITS = 32
    BYTE_WIDTH_BITS = 8

    START_PATTERN = 0x000000FF

    def __init__(self, size_in_bytes: int):
        """
        Initialize walking-byte generator configuration.

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
        Generate walking-byte binary pattern.

        Returns:
            bytes:
                Walking-byte byte stream.
        """

        generated_data = bytearray()

        current_pattern = self.START_PATTERN

        while len(generated_data) < self.size_in_bytes:

            pattern_bytes = current_pattern.to_bytes(
                length=4,
                byteorder="big"
            )

            remaining_bytes = (
                self.size_in_bytes
                - len(generated_data)
            )

            generated_data.extend(
                pattern_bytes[:remaining_bytes]
            )

            current_pattern <<= self.BYTE_WIDTH_BITS

            if current_pattern >= (
                1 << self.DOMAIN_WIDTH_BITS
            ):
                current_pattern = self.START_PATTERN

        return bytes(generated_data)