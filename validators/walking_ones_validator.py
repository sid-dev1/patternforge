class WalkingOnesValidator:
    """
    Validates deterministic walking-ones
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - bit-walk verification
        - lane integrity analysis
        - corruption localization
        - bit-position transition validation
    """

    validator_name = "WALKING_ONES_VALIDATOR"
    supported_pattern = "WALKING_ONES"

    START_VALUE = 0x01
    MAX_BIT_POSITION = 8

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
        Validate walking-ones binary pattern.

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

            expected_value <<= 1

            if expected_value >= (
                1 << self.MAX_BIT_POSITION
            ):
                expected_value = (
                    self.START_VALUE
                )

        return {
            "valid": True,
            "message": (
                "Walking-ones pattern "
                "validated successfully."
            )
        }