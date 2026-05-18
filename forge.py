from generators.all_zeros import AllZerosGenerator
from generators.all_ones import AllOnesGenerator
from generators.incremental import IncrementalGenerator
from generators.walking_ones import WalkingOnesGenerator
from generators.walking_zeros import WalkingZerosGenerator
from generators.prbs7 import PRBS7Generator
from generators.constant_pattern import ConstantPatternGenerator
from generators.random_pattern import RandomPatternGenerator
from generators.checkerboard import CheckerboardGenerator
from generators.burst_pattern import BurstPatternGenerator
from generators.walking_nibble import WalkingNibbleGenerator
from generators.walking_byte import WalkingByteGenerator
from generators.inverse_incremental import InverseIncrementalGenerator
from generators.colorbar_pattern import ColorBarPatternGenerator
from generators.ai_workload_pattern import AIWorkloadPatternGenerator


generator = AIWorkloadPatternGenerator(
    size_in_bytes=256,
    seed_value=1234
)

data = generator.generate()

print(" ".join(f"{byte:02X}" for byte in data[:128]))
