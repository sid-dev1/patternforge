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

    def validate(
        self,
        fail_fast: bool = True
    ) -> dict:
        """
        Validate walking-byte binary pattern.

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

                        "lane_index": (
                            index
                        ),

                        "group_index": (
                            offset // 4
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

                            "lane_integrity_lost": (
                                True
                            ),

                            "mismatches": (
                                mismatches
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

        if len(mismatches) > 0:

            return {
                "valid": False,

                "total_mismatches": (
                    len(mismatches)
                ),

                "lane_integrity_lost": True,

                "mismatches": mismatches
            }

        return {
            "valid": True,

            "total_mismatches": 0,

            "lane_integrity_lost": False,

            "message": (
                "Walking-byte pattern "
                "validated successfully."
            )
        }