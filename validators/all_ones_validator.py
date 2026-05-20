class AllOnesValidator:
    """
    Validates deterministic all-ones binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - integrity verification
        - corruption detection
        - transport validation
        - mismatch localization
    """

    validator_name = "ALL_ONES_VALIDATOR"
    supported_pattern = "ALL_ONES"

    EXPECTED_VALUE = 0xFF

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
        Validate all-ones binary pattern.

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

        for offset, observed_value in enumerate(
            self.data
        ):

            expected_value = (
                self.EXPECTED_VALUE
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
                "All bytes validated "
                "successfully."
            )
        }