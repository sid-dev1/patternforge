class CheckerboardValidator:
    """
    Validates deterministic checkerboard
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - alternating pattern verification
        - inverse-state validation
        - corruption localization
        - transition-pattern analysis
    """

    validator_name = (
        "CHECKERBOARD_VALIDATOR"
    )

    supported_pattern = (
        "CHECKERBOARD"
    )

    BYTE_LIMIT = 0xFF

    def __init__(
        self,
        data: bytes,
        base_pattern: int
    ):
        """
        Initialize validator configuration.

        Args:
            data (bytes):
                Binary data to validate.

            base_pattern (int):
                Expected checkerboard base pattern.
        """

        if not isinstance(data, bytes):
            raise TypeError(
                "data must be of type bytes."
            )

        if len(data) == 0:
            raise ValueError(
                "data cannot be empty."
            )

        if not isinstance(base_pattern, int):
            raise TypeError(
                "base_pattern must be an integer."
            )

        if not (
            0 <= base_pattern <= self.BYTE_LIMIT
        ):
            raise ValueError(
                "base_pattern must be between "
                "0 and 255."
            )

        self.data = data
        self.base_pattern = base_pattern

        self.inverse_pattern = (
            ~self.base_pattern
        ) & self.BYTE_LIMIT

    def validate(self) -> dict:
        """
        Validate checkerboard binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        alternating_patterns = (
            self.base_pattern,
            self.inverse_pattern
        )

        for offset, observed_value in enumerate(
            self.data
        ):

            expected_value = (
                alternating_patterns[
                    offset % 2
                ]
            )

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
                "Checkerboard pattern "
                "validated successfully."
            )
        }