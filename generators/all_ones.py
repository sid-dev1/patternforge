class AllOnesGenerator:
    """
    Generates deterministic all-ones binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - stuck-at faults
        - high-state stress testing
        - power and thermal behavior analysis
        - transport integrity validation

    Output:
        Raw binary byte stream.
    """

    pattern_name = "ALL_ONES"
    deterministic = True
    pattern_type = "STATIC"

    def __init__(self, size_in_bytes: int):
        """
        Initialize generator configuration.

        Args:
            size_in_bytes (int):
                Total size of pattern to generate in bytes.
        """

        if not isinstance(size_in_bytes, int):
            raise TypeError("size_in_bytes must be an integer.")

        if size_in_bytes <= 0:
            raise ValueError("size_in_bytes must be greater than zero.")

        self.size_in_bytes = size_in_bytes

    def generate(self) -> bytes:
        """
        Generate all-ones binary pattern.

        Returns:
            bytes:
                One-filled binary data.
        """

        return bytes([0xFF] * self.size_in_bytes)