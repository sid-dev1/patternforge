class PRBS7Validator:
    """
    Validates deterministic PRBS7 binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - LFSR sequence verification
        - SERDES integrity analysis
        - corruption localization
        - feedback-state validation
        - pseudo-random sequence analysis
    """

    validator_name = "PRBS7_VALIDATOR"
    supported_pattern = "PRBS7"

    REGISTER_WIDTH = 7
    MAX_REGISTER_VALUE = 0x7F

    def __init__(
        self,
        data: bytes,
        seed_value: int
    ):
        """
        Initialize validator configuration.

        Args:
            data (bytes):
                Binary data to validate.

            seed_value (int):
                Initial non-zero LFSR seed value.
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

        if not (
            1 <= seed_value <= self.MAX_REGISTER_VALUE
        ):
            raise ValueError(
                "seed_value must be between 1 and 127."
            )

        self.data = data
        self.seed_value = seed_value

    def validate(self) -> dict:
        """
        Validate PRBS7 binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        lfsr = self.seed_value

        for byte_offset, observed_byte in enumerate(
            self.data
        ):

            expected_byte = 0

            for bit_position in range(8):

                output_bit = lfsr & 0x01

                expected_byte |= (
                    output_bit << bit_position
                )

                feedback_bit = (
                    ((lfsr >> 6) ^ (lfsr >> 5))
                    & 0x01
                )

                lfsr = (
                    (
                        (lfsr << 1)
                        | feedback_bit
                    )
                    & self.MAX_REGISTER_VALUE
                )

            if observed_byte != expected_byte:

                return {
                    "valid": False,
                    "mismatch_offset": (
                        byte_offset
                    ),
                    "expected_value": (
                        expected_byte
                    ),
                    "observed_value": (
                        observed_byte
                    )
                }

        return {
            "valid": True,
            "message": (
                "PRBS7 pattern validated "
                "successfully."
            )
        }