class WalkingByteValidator:
    """
    Validates deterministic walking-byte
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - byte-lane verification
        - structured shift validation
        - DMA alignment analysis
        - corruption localization
        - serializer integrity analysis
    """

    validator_name = (
        "WALKING_BYTE_VALIDATOR"
    )

    supported_pattern = (
        "WALKING_BYTE"
    )

    DOMAIN_WIDTH_BITS = 32
    BYTE_WIDTH_BITS = 8

    START_PATTERN = 0x000000FF

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
        Validate walking-byte binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        expected_pattern = (
            self.START_PATTERN
        )

        offset = 0

        while offset < len(self.data):

            expected_bytes = (
                expected_pattern.to_bytes(
                    length=4,
                    byteorder="big"
                )
            )

            remaining_bytes = (
                len(self.data) - offset
            )

            observed_chunk = self.data[
                offset : offset + 4
            ]

            expected_chunk = expected_bytes[
                :remaining_bytes
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

            expected_pattern <<= (
                self.BYTE_WIDTH_BITS
            )

            if expected_pattern >= (
                1 << self.DOMAIN_WIDTH_BITS
            ):
                expected_pattern = (
                    self.START_PATTERN
                )

            offset += 4

        return {
            "valid": True,
            "message": (
                "Walking-byte pattern "
                "validated successfully."
            )
        }