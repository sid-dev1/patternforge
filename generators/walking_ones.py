class WalkingOnesGenerator:
    """
    Generates deterministic walking-ones binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - bit-line isolation
        - stuck-low fault detection
        - lane integrity validation
        - signal integrity analysis
        - hardware interface testing

    Output:
        Raw binary byte stream.
    """

    pattern_name = "WALKING_ONES"
    deterministic = True
    pattern_type = "SEQUENTIAL"

    START_VALUE = 0x01
    MAX_BIT_POSITION = 8

    def __init__(self, size_in_bytes: int):
        """
        Initialize walking-ones generator configuration.

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
        Generate walking-ones binary pattern.

        Returns:
            bytes:
                Walking-ones byte stream.
        """

        generated_data = bytearray()

        current_value = self.START_VALUE

        for _ in range(self.size_in_bytes):

            generated_data.append(current_value)

            current_value <<= 1

            if current_value >= (1 << self.MAX_BIT_POSITION):
                current_value = self.START_VALUE

        return bytes(generated_data)