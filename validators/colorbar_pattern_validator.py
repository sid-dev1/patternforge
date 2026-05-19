class ColorBarPatternValidator:
    """
    Validates deterministic RGB color bar
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - display payload verification
        - RGB channel validation
        - visual structure analysis
        - multimedia transport integrity
        - corruption localization
    """

    validator_name = (
        "COLORBAR_PATTERN_VALIDATOR"
    )

    supported_pattern = (
        "COLORBAR_PATTERN"
    )

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

    COLOR_WIDTH_BYTES = 3

    def __init__(self, data: bytes):
        """
        Initialize validator configuration.

        Args:
            data (bytes):
                Binary data to validate.
        """

        if not isinstance(data, bytes):
            raise TypeError(
                "data must be of type bytes."
            )

        if len(data) == 0:
            raise ValueError(
                "data cannot be empty."
            )

        self.data = data

    def validate(self) -> dict:
        """
        Validate RGB color bar binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        offset = 0
        color_index = 0

        while offset < len(self.data):

            expected_color = self.COLOR_BARS[
                color_index % len(
                    self.COLOR_BARS
                )
            ]

            remaining_bytes = (
                len(self.data) - offset
            )

            expected_chunk = expected_color[
                :remaining_bytes
            ]

            observed_chunk = self.data[
                offset :
                offset + self.COLOR_WIDTH_BYTES
            ]

            if observed_chunk != expected_chunk:

                mismatch_index = 0

                for index in range(
                    min(
                        len(observed_chunk),
                        len(expected_chunk)
                    )
                ):

                    if (
                        observed_chunk[index]
                        != expected_chunk[index]
                    ):

                        mismatch_index = index
                        break

                return {
                    "valid": False,
                    "mismatch_offset": (
                        offset + mismatch_index
                    ),
                    "expected_value": (
                        expected_chunk[
                            mismatch_index
                        ]
                    ),
                    "observed_value": (
                        observed_chunk[
                            mismatch_index
                        ]
                    )
                }

            offset += (
                self.COLOR_WIDTH_BYTES
            )

            color_index += 1

        return {
            "valid": True,
            "message": (
                "Color bar pattern validated "
                "successfully."
            )
        }