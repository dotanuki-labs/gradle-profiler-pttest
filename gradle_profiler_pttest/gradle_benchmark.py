# gradle_benchmark.py

from dataclasses import dataclass
from typing import List


@dataclass
class GradleBenchmark:
    gradle_task:str
    builds: List[int]
    mean: str
    stddev: str
