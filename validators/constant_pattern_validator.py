class ConstantPatternValidator:
    """
    Validates deterministic repeating
    constant binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - cyclic pattern verification
        - corruption localization
        - alignment validation
        - structural repetition analysis
    """

    validator_name = (
        "CONSTANT_PATTERN_VALIDATOR"
    )

    supported_pattern = (
        "CONSTANT_PATTERN"
    )

    def __init__(
        self,
        data: bytes,
        pattern: bytes
    ):
        """
        Initialize validator configuration.

        Args:
            data (bytes):
                Binary data to validate.

            pattern (bytes):
                Expected repeating byte sequence.
        """

        if not isinstance(data, bytes):
            raise TypeError(
                "data must be of type bytes."
            )

        if len(data) == 0:
            raise ValueError(
                "data cannot be empty."
            )

        if not isinstance(pattern, bytes):
            raise TypeError(
                "pattern must be of type bytes."
            )

        if len(pattern) == 0:
            raise ValueError(
                "pattern cannot be empty."
            )

        self.data = data
        self.pattern = pattern

    def validate(self) -> dict:
        """
        Validate repeating constant
        binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        pattern_length = len(self.pattern)

        for offset, observed_value in enumerate(
            self.data
        ):

            expected_value = self.pattern[
                offset % pattern_length
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
                "Constant pattern validated "
                "successfully."
            )
        }