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

    COLOR_NAMES = (
        "WHITE",
        "YELLOW",
        "CYAN",
        "GREEN",
        "MAGENTA",
        "RED",
        "BLUE",
        "BLACK"
    )

    RGB_CHANNEL_NAMES = (
        "RED_CHANNEL",
        "GREEN_CHANNEL",
        "BLUE_CHANNEL"
    )

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

    def validate(
        self,
        fail_fast: bool = True
    ) -> dict:
        """
        Validate RGB color bar binary pattern.

        Args:
            fail_fast (bool):
                Stop validation immediately on
                first mismatch.

                If False, collect all mismatches.

        Returns:
            dict:
                Structured validation result.
        """

        if not isinstance(fail_fast, bool):
            raise TypeError(
                "fail_fast must be of type bool."
            )

        mismatches = []

        offset = 0
        color_index = 0

        while offset < len(self.data):

            expected_color = self.COLOR_BARS[
                color_index % len(
                    self.COLOR_BARS
                )
            ]

            expected_color_name = (
                self.COLOR_NAMES[
                    color_index % len(
                        self.COLOR_NAMES
                    )
                ]
            )

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

            for index in range(
                min(
                    len(observed_chunk),
                    len(expected_chunk)
                )
            ):

                observed_value = (
                    observed_chunk[index]
                )

                expected_value = (
                    expected_chunk[index]
                )

                if observed_value != expected_value:

                    mismatch_entry = {
                        "mismatch_index": (
                            len(mismatches) + 1
                        ),

                        "offset": (
                            offset + index
                        ),

                        "color_index": (
                            color_index
                        ),

                        "color_name": (
                            expected_color_name
                        ),

                        "channel_name": (
                            self.RGB_CHANNEL_NAMES[
                                index
                            ]
                        ),

                        "expected_value": (
                            expected_value
                        ),

                        "observed_value": (
                            observed_value
                        )
                    }

                    mismatches.append(
                        mismatch_entry
                    )

                    if fail_fast:

                        return {
                            "valid": False,

                            "total_mismatches": 1,

                            "visual_integrity_lost": (
                                True
                            ),

                            "mismatches": (
                                mismatches
                            )
                        }

            offset += (
                self.COLOR_WIDTH_BYTES
            )

            color_index += 1

        if len(mismatches) > 0:

            return {
                "valid": False,

                "total_mismatches": (
                    len(mismatches)
                ),

                "visual_integrity_lost": True,

                "mismatches": mismatches
            }

        return {
            "valid": True,

            "total_mismatches": 0,

            "visual_integrity_lost": False,

            "message": (
                "Color bar pattern validated "
                "successfully."
            )
        }