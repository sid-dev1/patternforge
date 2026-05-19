class WalkingZerosValidator:
    """
    Validates deterministic walking-zeros
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - inverse bit-walk verification
        - lane integrity analysis
        - corruption localization
        - inverse transition validation
    """

    validator_name = "WALKING_ZEROS_VALIDATOR"
    supported_pattern = "WALKING_ZEROS"

    START_VALUE = 0xFE

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

    def validate(self) -> dict:
        """
        Validate walking-zeros binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        expected_value = self.START_VALUE

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
                ((expected_value << 1) | 0x01)
                & 0xFF
            )

            if expected_value == 0xFF:

                expected_value = (
                    self.START_VALUE
                )

        return {
            "valid": True,
            "message": (
                "Walking-zeros pattern "
                "validated successfully."
            )
        }