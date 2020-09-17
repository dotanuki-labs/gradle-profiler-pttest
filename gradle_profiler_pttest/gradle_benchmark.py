# gradle_benchmark.py

from dataclasses import dataclass
from typing import List


@dataclass
class GradleBenchmark:
    gradle_task:str
    measured_builds: List[int]
    mean: str
    standard_deviation: str
