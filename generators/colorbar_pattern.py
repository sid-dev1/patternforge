class ColorBarPatternGenerator:
    """
    Generates deterministic RGB color bar
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - display pipeline validation
        - multimedia transport testing
        - RGB channel verification
        - visual payload generation
        - streaming integrity analysis

    Output:
        Raw RGB888 binary byte stream.
    """

    pattern_name = "COLORBAR_PATTERN"
    deterministic = True
    pattern_type = "VISUAL"

    COLOR_BARS = (
        b'\xFF\xFF\xFF',  # White
        b'\xFF\xFF\x00',  # Yellow
        b'\x00\xFF\xFF',  # Cyan
        b'\x00\xFF\x00',  # Green
        b'\xFF\x00\xFF',  # Magenta
        b'\xFF\x00\x00',  # Red
        b'\x00\x00\xFF',  # Blue
        b'\x00\x00\x00'   # Black
    )

    def __init__(self, size_in_bytes: int):
        """
        Initialize color bar pattern generator
        configuration.

        Args:
            size_in_bytes (int):
                Total size of generated pattern
                in bytes.
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
        Generate RGB color bar binary pattern.

        Returns:
            bytes:
                RGB888 color bar byte stream.
        """

        generated_data = bytearray()

        color_index = 0

        while len(generated_data) < self.size_in_bytes:

            current_color = self.COLOR_BARS[
                color_index % len(self.COLOR_BARS)
            ]

            remaining_bytes = (
                self.size_in_bytes
                - len(generated_data)
            )

            generated_data.extend(
                current_color[:remaining_bytes]
            )

            color_index += 1

        return bytes(generated_data)