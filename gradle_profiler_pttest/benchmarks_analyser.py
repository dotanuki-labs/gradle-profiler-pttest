# benchmarks_analyser.py

from pingouin import ttest

from .analysis_results import AnalysisResults
from .analysis_results import PairedTTestDetails


SIGNIFICANCE_LEVEL = 0.05


def analyse(baseline, candidate):
    stats = ttest(baseline.measured_builds, candidate.measured_builds, paired=True, tail='greater').round(3)
    tstatistic = stats.loc['T-test', 'T']
    pvalue = stats.loc['T-test', 'p-val']
    print(stats)
    improvement_detected = pvalue < SIGNIFICANCE_LEVEL
    details = PairedTTestDetails(tstatistic, pvalue, SIGNIFICANCE_LEVEL)
    return AnalysisResults(baseline, candidate, details, improvement_detected)
