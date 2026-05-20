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

    def validate(
        self,
        fail_fast: bool = True
    ) -> dict:
        """
        Validate checkerboard binary pattern.

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

                mismatch_entry = {
                    "mismatch_index": (
                        len(mismatches) + 1
                    ),

                    "offset": offset,

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

                        "transition_integrity_lost": True,

                        "mismatches": (
                            mismatches
                        )
                    }

        if len(mismatches) > 0:

            return {
                "valid": False,

                "total_mismatches": (
                    len(mismatches)
                ),

                "transition_integrity_lost": True,

                "mismatches": mismatches
            }

        return {
            "valid": True,

            "total_mismatches": 0,

            "transition_integrity_lost": False,

            "message": (
                "Checkerboard pattern "
                "validated successfully."
            )
        }