class WalkingZerosGenerator:
    """
    Generates deterministic walking-zeros binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - stuck-high fault detection
        - inverse lane validation
        - signal integrity analysis
        - hardware interface testing

    Output:
        Raw binary byte stream.
    """

    pattern_name = "WALKING_ZEROS"
    deterministic = True
    pattern_type = "SEQUENTIAL"

    START_VALUE = 0xFE
    MAX_BIT_POSITION = 8

    def __init__(self, size_in_bytes: int):
        """
        Initialize walking-zeros generator configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern in bytes.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError("size_in_bytes must be an integer.")

        if size_in_bytes <= 0:
            raise ValueError("size_in_bytes must be greater than zero.")

        self.size_in_bytes = size_in_bytes

    def generate(self) -> bytes:
        """
        Generate walking-zeros binary pattern.

        Returns:
            bytes:
                Walking-zeros byte stream.
        """

        generated_data = bytearray()

        current_value = self.START_VALUE

        for _ in range(self.size_in_bytes):

            generated_data.append(current_value)

            current_value = (
                ((current_value << 1) | 0x01) & 0xFF
            )

            if current_value == 0xFF:
                current_value = self.START_VALUE

        return bytes(generated_data)