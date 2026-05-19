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

        if not isinstance(increment_value, int):
            raise TypeError(
                "increment_value must be an integer."
            )

        if not (0 <= seed_value <= 255):
            raise ValueError(
                "seed_value must be between 0 and 255."
            )

        if not (0 <= increment_value <= 255):
            raise ValueError(
                "increment_value must be between 0 and 255."
            )

        self.data = data
        self.seed_value = seed_value
        self.increment_value = increment_value

    def validate(self) -> dict:
        """
        Validate incremental binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        expected_value = self.seed_value

        for offset, observed_value in enumerate(
            self.data
        ):

            if observed_value != expected_value:

                return {
                    "valid": False,
                    "mismatch_offset": offset,
                    "expected_value": (
                        expected_value
                    ),
                    "observed_value": (
                        observed_value
                    )
                }

            expected_value = (
                expected_value
                + self.increment_value
            ) % self.BYTE_LIMIT

        return {
            "valid": True,
            "message": (
                "Incremental pattern validated "
                "successfully."
            )
        }