# analysis_results.py

from dataclasses import dataclass

from .gradle_benchmark import GradleBenchmark


@dataclass
class PairedTTestDetails:
    t_statistic: float
    pvalue: float
    significance_level: float


@dataclass
class AnalysisResults:
    baseline: GradleBenchmark
    modified: GradleBenchmark
    details: PairedTTestDetails
    improvement_detected: bool
