class InverseIncrementalValidator:
    """
    Validates deterministic inverse
    incremental binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - reverse arithmetic verification
        - decrement progression analysis
        - corruption localization
        - transport integrity validation
    """

    validator_name = (
        "INVERSE_INCREMENTAL_VALIDATOR"
    )

    supported_pattern = (
        "INVERSE_INCREMENTAL"
    )

    BYTE_LIMIT = 256

    def __init__(
        self,
        data: bytes,
        seed_value: int,
        decrement_value: int
    ):
        """
        Initialize validator configuration.

        Args:
            data (bytes):
                Binary data to validate.

            seed_value (int):
                Expected starting byte value.

            decrement_value (int):
                Expected decrement step.
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
            decrement_value,
            int
        ):
            raise TypeError(
                "decrement_value must be "
                "an integer."
            )

        if not (0 <= seed_value <= 255):
            raise ValueError(
                "seed_value must be between "
                "0 and 255."
            )

        if not (
            0 <= decrement_value <= 255
        ):
            raise ValueError(
                "decrement_value must be "
                "between 0 and 255."
            )

        self.data = data

        self.seed_value = seed_value

        self.decrement_value = (
            decrement_value
        )

    def validate(
        self,
        fail_fast: bool = True
    ) -> dict:
        """
        Validate inverse incremental
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

                        "decrement_sequence_lost": (
                            True
                        ),

                        "mismatches": (
                            mismatches
                        )
                    }

            expected_value = (
                expected_value
                - self.decrement_value
            ) % self.BYTE_LIMIT

        if len(mismatches) > 0:

            return {
                "valid": False,

                "total_mismatches": (
                    len(mismatches)
                ),

                "decrement_sequence_lost": True,

                "mismatches": mismatches
            }

        return {
            "valid": True,

            "total_mismatches": 0,

            "decrement_sequence_lost": False,

            "message": (
                "Inverse incremental pattern "
                "validated successfully."
            )
        }