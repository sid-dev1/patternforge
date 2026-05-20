import random


class AIWorkloadPatternValidator:
    """
    Validates deterministic AI-inspired
    workload binary patterns.

    Purpose:
        Used for validation scenarios involving:
        - workload phase verification
        - sparse-region validation
        - tensor locality analysis
        - burst-transfer verification
        - deterministic entropy replay
        - corruption localization
    """

    validator_name = (
        "AI_WORKLOAD_PATTERN_VALIDATOR"
    )

    supported_pattern = (
        "AI_WORKLOAD_PATTERN"
    )

    SPARSE_REGION_SIZE = 64
    RANDOM_REGION_SIZE = 64
    TENSOR_REGION_SIZE = 64
    BURST_REGION_SIZE = 64

    TENSOR_PATTERN = (
        b'\xAA\xBB\xCC\xDD'
    )

    BURST_PATTERN = (
        b'\xFF\xFF\xFF\xFF'
        b'\x00\x00\x00\x00'
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
                pseudo-random workload regions.
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

    def validate(
        self,
        fail_fast: bool = True
    ) -> dict:
        """
        Validate AI-inspired workload
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

        rng = random.Random(
            self.seed_value
        )

        offset = 0

        while offset < len(self.data):

            workload_regions = (
                (
                    "SPARSE",
                    self._validate_sparse_region
                ),
                (
                    "RANDOM",
                    lambda current_offset:
                    self._validate_random_region(
                        current_offset,
                        rng
                    )
                ),
                (
                    "TENSOR",
                    self._validate_tensor_region
                ),
                (
                    "BURST",
                    self._validate_burst_region
                )
            )

            for (
                region_name,
                validator_function
            ) in workload_regions:

                if offset >= len(self.data):
                    break

                validation_result = (
                    validator_function(
                        offset
                    )
                )

                if validation_result is not None:

                    validation_result[
                        "mismatch_index"
                    ] = (
                        len(mismatches) + 1
                    )

                    validation_result[
                        "region_name"
                    ] = region_name

                    mismatches.append(
                        validation_result
                    )

                    if fail_fast:

                        return {
                            "valid": False,

                            "total_mismatches": 1,

                            "workload_integrity_lost": (
                                True
                            ),

                            "mismatches": (
                                mismatches
                            )
                        }

                offset += (
                    self._get_region_size(
                        region_name,
                        offset
                    )
                )

        if len(mismatches) > 0:

            return {
                "valid": False,

                "total_mismatches": (
                    len(mismatches)
                ),

                "workload_integrity_lost": True,

                "mismatches": mismatches
            }

        return {
            "valid": True,

            "total_mismatches": 0,

            "workload_integrity_lost": False,

            "message": (
                "AI workload pattern validated "
                "successfully."
            )
        }

    def _validate_sparse_region(
        self,
        offset: int
    ):

        region_size = min(
            self.SPARSE_REGION_SIZE,
            len(self.data) - offset
        )

        for index in range(region_size):

            observed_value = self.data[
                offset + index
            ]

            expected_value = 0x00

            if observed_value != expected_value:

                return {
                    "offset": (
                        offset + index
                    ),

                    "expected_value": (
                        expected_value
                    ),

                    "observed_value": (
                        observed_value
                    )
                }

        return None

    def _validate_random_region(
        self,
        offset: int,
        rng: random.Random
    ):

        region_size = min(
            self.RANDOM_REGION_SIZE,
            len(self.data) - offset
        )

        for index in range(region_size):

            observed_value = self.data[
                offset + index
            ]

            expected_value = rng.randint(
                0,
                self.BYTE_LIMIT - 1
            )

            if observed_value != expected_value:

                return {
                    "offset": (
                        offset + index
                    ),

                    "expected_value": (
                        expected_value
                    ),

                    "observed_value": (
                        observed_value
                    )
                }

        return None

    def _validate_tensor_region(
        self,
        offset: int
    ):

        region_size = min(
            self.TENSOR_REGION_SIZE,
            len(self.data) - offset
        )

        pattern_length = len(
            self.TENSOR_PATTERN
        )

        for index in range(region_size):

            observed_value = self.data[
                offset + index
            ]

            expected_value = (
                self.TENSOR_PATTERN[
                    index % pattern_length
                ]
            )

            if observed_value != expected_value:

                return {
                    "offset": (
                        offset + index
                    ),

                    "expected_value": (
                        expected_value
                    ),

                    "observed_value": (
                        observed_value
                    )
                }

        return None

    def _validate_burst_region(
        self,
        offset: int
    ):

        region_size = min(
            self.BURST_REGION_SIZE,
            len(self.data) - offset
        )

        pattern_length = len(
            self.BURST_PATTERN
        )

        for index in range(region_size):

            observed_value = self.data[
                offset + index
            ]

            expected_value = (
                self.BURST_PATTERN[
                    index % pattern_length
                ]
            )

            if observed_value != expected_value:

                return {
                    "offset": (
                        offset + index
                    ),

                    "expected_value": (
                        expected_value
                    ),

                    "observed_value": (
                        observed_value
                    )
                }

        return None

    def _get_region_size(
        self,
        region_name: str,
        offset: int
    ) -> int:
        """
        Determine effective region size.

        Args:
            region_name (str):
                Workload region type.

            offset (int):
                Current workload offset.

        Returns:
            int:
                Effective region size.
        """

        region_sizes = {
            "SPARSE":
                self.SPARSE_REGION_SIZE,

            "RANDOM":
                self.RANDOM_REGION_SIZE,

            "TENSOR":
                self.TENSOR_REGION_SIZE,

            "BURST":
                self.BURST_REGION_SIZE
        }

        return min(
            region_sizes[region_name],
            len(self.data) - offset
        )