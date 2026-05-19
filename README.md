# PatternForge

PatternForge is a Python-based validation pattern generation and verification framework designed for silicon validation, memory testing, transport integrity analysis, multimedia payload verification, and workload simulation.

The project focuses on:
- deterministic data pattern generation
- semantic validation infrastructure
- corruption localization
- workload-aware traffic modeling
- structured transport verification

PatternForge is built with a strong emphasis on:
- reproducibility
- deterministic behavior
- validation realism
- modular architecture
- infrastructure-oriented engineering

---

# Project Motivation

Silicon validation engineers frequently require:
- deterministic traffic generation
- repeatable stress patterns
- transport integrity verification
- workload simulation
- corruption analysis
- structured payload validation

PatternForge was built to provide reusable and extensible validation infrastructure for these workflows.

The goal is not merely to generate bytes, but to model:
- traffic behavior
- structured transitions
- workload semantics
- validation methodology

---

# Features

## Pattern Generators

### Static Patterns
- All Zeros
- All Ones
- Constant Pattern

### Arithmetic Patterns
- Incremental
- Inverse Incremental

### Bit-Transition Patterns
- Walking Ones
- Walking Zeros

### Structured Shift Patterns
- Walking Nibble
- Walking Byte

### Pseudo-Random Patterns
- PRBS7
- Random Pattern

### Structural Patterns
- Checkerboard
- Burst Pattern

### Multimedia Patterns
- RGB Color Bar Pattern

### Workload Patterns
- AI Workload Pattern

---

# Validation Infrastructure

Each generator has a corresponding semantic validator.

Validators are designed to:
- verify correctness
- detect corruption
- identify mismatch offsets
- preserve deterministic replay
- validate workload semantics

Validation is behavior-aware and not limited to blob comparison.

Examples:
- arithmetic progression validation
- LFSR feedback validation
- burst-structure verification
- RGB payload validation
- workload-phase verification

---

# Project Structure

```text
PatternForge/
│
├── generators/
│   ├── all_zeros.py
│   ├── all_ones.py
│   ├── incremental.py
│   ├── inverse_incremental.py
│   ├── walking_ones.py
│   ├── walking_zeros.py
│   ├── walking_nibble.py
│   ├── walking_byte.py
│   ├── prbs7.py
│   ├── random_pattern.py
│   ├── checkerboard.py
│   ├── burst_pattern.py
│   ├── colorbar_pattern.py
│   └── ai_workload_pattern.py
│
├── validators/
│   ├── all_zeros_validator.py
│   ├── all_ones_validator.py
│   ├── incremental_validator.py
│   ├── inverse_incremental_validator.py
│   ├── walking_ones_validator.py
│   ├── walking_zeros_validator.py
│   ├── walking_nibble_validator.py
│   ├── walking_byte_validator.py
│   ├── prbs7_validator.py
│   ├── random_pattern_validator.py
│   ├── checkerboard_validator.py
│   ├── burst_pattern_validator.py
│   ├── colorbar_pattern_validator.py
│   └── ai_workload_pattern_validator.py
│
└── README.md