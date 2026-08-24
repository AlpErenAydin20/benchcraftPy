# BenchCraft ⚡

A lightweight, precision Python decorator library for benchmarking execution time and tracking peak memory allocation.

## Features

- ⏱️ **Execution Time Tracking**: High-precision time measurements via `time.perf_counter()`.
- 🧠 **Memory Profiling**: Real-time peak memory usage tracking using `tracemalloc`.
- 📐 **Auto-formatting**: Human-readable memory unit conversion (`B`, `KB`, `MB`).
- 🛡️ **Exception Safe**: Guaranteed metrics delivery even if decorated functions raise runtime errors (`try...finally`).

## Installation

Install locally in editable mode for development:

```bash
pip install -e . 
```

## Quick Start

```python
import time
from benchcraft import BenchCraft

@BenchCraft(unit="ms")
def heavy_computation():
    data = [i for i in range(1000000)]
    time.sleep(0.05)
    return sum(data)

if __name__ == "__main__":
    heavy_computation()
```
## Output
```
[heavy_computation] Run Time: 85.124000 ms | Peak Memory: 38.15 MB
```