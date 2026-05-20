from generators.prbs7 import PRBS7Generator
from file_io.binary_writer import BinaryWriter
from validators.prbs7_validator import PRBS7Validator
from file_io.binary_reader import BinaryReader

'''
generator = PRBS7Generator(
    size_in_bytes=1024,
    seed_value=0x5A
)

data = generator.generate()

writer = BinaryWriter(
    file_path="payloads/prbs7_payload.bin",
    mode="wb"
)

result = writer.write(data)

print(result)
'''

reader = BinaryReader(
    file_path="payloads/prbs7_payload.bin"
)

captured_data = reader.read()

validator = PRBS7Validator(
    data=captured_data,
    seed_value=0x5A
)

result = validator.validate()

print(result)