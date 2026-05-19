from generators.ai_workload_pattern import (
    AIWorkloadPatternGenerator
)

from validators.ai_workload_pattern_validator import (
    AIWorkloadPatternValidator
)

generator = AIWorkloadPatternGenerator(
    size_in_bytes=256,
    seed_value=1234
)

data = generator.generate()

corrupted_data = bytearray(data)

corrupted_data[130] = 0xAA

validator = AIWorkloadPatternValidator(
    data=bytes(corrupted_data),
    seed_value=1234
)

result = validator.validate()

print(result)