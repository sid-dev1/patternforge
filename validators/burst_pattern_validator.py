class BurstPatternValidator:
    """
    Validates deterministic burst-style
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - burst-transfer verification
        - DMA-style traffic analysis
        - grouped structure validation
        - corruption localization
        - burst-boundary analysis
    """

    validator_name = (
        "BURST_PATTERN_VALIDATOR"
    )

    supported_pattern = (
        "BURST_PATTERN"
    )

    def __init__(
        self,
        data: bytes,
        pattern_a: bytes,
        pattern_b: bytes,
        burst_length_in_bytes: int
    ):
        """
        Initialize validator configuration.

        Args:
            data (bytes):
                Binary data to validate.

            pattern_a (bytes):
                Expected first burst pattern.

            pattern_b (bytes):
                Expected second burst pattern.

            burst_length_in_bytes (int):
                Expected burst size.
        """

        if not isinstance(data, bytes):
            raise TypeError(
                "data must be of type bytes."
            )

        if len(data) == 0:
            raise ValueError(
                "data cannot be empty."
            )

        if not isinstance(pattern_a, bytes):
            raise TypeError(
                "pattern_a must be of type bytes."
            )

        if len(pattern_a) == 0:
            raise ValueError(
                "pattern_a cannot be empty."
            )

        if not isinstance(pattern_b, bytes):
            raise TypeError(
                "pattern_b must be of type bytes."
            )

        if len(pattern_b) == 0:
            raise ValueError(
                "pattern_b cannot be empty."
            )

        if not isinstance(
            burst_length_in_bytes,
            int
        ):
            raise TypeError(
                "burst_length_in_bytes "
                "must be an integer."
            )

        if burst_length_in_bytes <= 0:
            raise ValueError(
                "burst_length_in_bytes "
                "must be greater than zero."
            )

        self.data = data
        self.pattern_a = pattern_a
        self.pattern_b = pattern_b

        self.burst_length_in_bytes = (
            burst_length_in_bytes
        )

    def validate(self) -> dict:
        """
        Validate burst binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        burst_patterns = (
            self.pattern_a,
            self.pattern_b
        )

        for offset, observed_value in enumerate(
            self.data
        ):

            burst_index = (
                offset
                // self.burst_length_in_bytes
            )

            current_pattern = burst_patterns[
                burst_index % 2
            ]

            pattern_index = (
                offset
                % self.burst_length_in_bytes
            ) % len(current_pattern)

            expected_value = current_pattern[
                pattern_index
            ]

            if observed_value != expected_value:

                return {
                    "valid": False,
                    "mismatch_offset": (
                        offset
                    ),
                    "expected_value": (
                        expected_value
                    ),
                    "observed_value": (
                        observed_value
                    )
                }

        return {
            "valid": True,
            "message": (
                "Burst pattern validated "
                "successfully."
            )
        }