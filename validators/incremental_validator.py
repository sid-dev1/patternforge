class IncrementalValidator:
    """
    Validates deterministic incremental
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - arithmetic progression verification
        - integrity validation
        - ordering analysis
        - corruption localization
    """

    validator_name = "INCREMENTAL_VALIDATOR"
    supported_pattern = "INCREMENTAL"

    BYTE_LIMIT = 256

    def __init__(
        self,
        data: bytes,
        seed_value: int,
        increment_value: int
    ):
        """
        Initialize validator configuration.

        Args:
            data (bytes):
                Binary data to validate.

            seed_value (int):
                Expected starting byte value.

            increment_value (int):
                Expected arithmetic increment.
        """

        if not isinstance(data, bytes):
            raise TypeError(
                "data must be of type bytes."
            )

        if len(data) == 0:
            raise ValueError(
                "data cannot be empty."
            )

        if not isinstance(seed_value, int):
            raise TypeError(
                "seed_value must be an integer."
            )

        if not isinstance(
            increment_value,
            int
        ):
            raise TypeError(
                "increment_value must be "
                "an integer."
            )

        if not (0 <= seed_value <= 255):
            raise ValueError(
                "seed_value must be between "
                "0 and 255."
            )

        if not (
            0 <= increment_value <= 255
        ):
            raise ValueError(
                "increment_value must be "
                "between 0 and 255."
            )

        self.data = data

        self.seed_value = seed_value

        self.increment_value = (
            increment_value
        )

    def validate(
        self,
        fail_fast: bool = True
    ) -> dict:
        """
        Validate incremental binary pattern.

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

        expected_value = (
            self.seed_value
        )

        for offset, observed_value in enumerate(
            self.data
        ):

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

            expected_value = (
                expected_value
                + self.increment_value
            ) % self.BYTE_LIMIT

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
                "Incremental pattern "
                "validated successfully."
            )
        }