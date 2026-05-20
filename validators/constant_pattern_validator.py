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

    def validate(
        self,
        fail_fast: bool = True
    ) -> dict:
        """
        Validate repeating constant
        binary pattern.

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

        pattern_length = len(
            self.pattern
        )

        for offset, observed_value in enumerate(
            self.data
        ):

            expected_value = self.pattern[
                offset % pattern_length
            ]

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

                "mismatches": mismatches
            }

        return {
            "valid": True,

            "total_mismatches": 0,

            "message": (
                "Constant pattern validated "
                "successfully."
            )
        }