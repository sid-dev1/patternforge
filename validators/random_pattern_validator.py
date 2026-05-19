import random


class RandomPatternValidator:
    """
    Validates deterministic pseudo-random
    binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - deterministic replay verification
        - corruption localization
        - PRNG sequence validation
        - entropy-stream integrity analysis
    """

    validator_name = (
        "RANDOM_PATTERN_VALIDATOR"
    )

    supported_pattern = (
        "RANDOM_PATTERN"
    )

    BYTE_LIMIT = 256

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
                Seed value used for deterministic
                pseudo-random generation.
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

        self.data = data
        self.seed_value = seed_value

    def validate(self) -> dict:
        """
        Validate deterministic pseudo-random
        binary pattern.

        Returns:
            dict:
                Structured validation result.
        """

        rng = random.Random(self.seed_value)

        for offset, observed_value in enumerate(
            self.data
        ):

            expected_value = rng.randint(
                0,
                self.BYTE_LIMIT - 1
            )

            if observed_value != expected_value:

                return {
                    "valid": False,
                    "mismatch_offset": (
                        offset
                    ),
                    "expected_value": (
                        expected_value
                    ),
                    "observed_value": (
                        observed_value
                    )
                }

        return {
            "valid": True,
            "message": (
                "Random pattern validated "
                "successfully."
            )
        }