# gradle_benchmark.py

from dataclasses import dataclass
from typing import List


@dataclass
class GradleBenchmark:
    benchmark_file: str
    builds: List[int]
    mean: float
    stddev: float
