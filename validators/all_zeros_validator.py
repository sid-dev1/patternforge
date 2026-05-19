class AllZerosValidator:
    """
    Validates deterministic all-zero binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - integrity verification
        - corruption detection
        - transport validation
        - mismatch localization
    """

    validator_name = "ALL_ZEROS_VALIDATOR"
    supported_pattern = "ALL_ZEROS"

    def __init__(self, data: bytes):
        """
        Initialize validator configuration.

        Args:
            data (bytes):
                Binary data to validate.
        """

        if not isinstance(data, bytes):
            raise TypeError("data must be of type bytes.")

        if len(data) == 0:
            raise ValueError("data cannot be empty.")

        self.data = data

    def validate(self) -> dict:
        """
        Validate all-zero binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        for offset, value in enumerate(self.data):

            if value != 0x00:

                return {
                    "valid": False,
                    "mismatch_offset": offset,
                    "expected_value": 0x00,
                    "observed_value": value
                }

        return {
            "valid": True,
            "message": "All bytes validated successfully."
        }