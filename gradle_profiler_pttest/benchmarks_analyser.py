# benchmarks_analyser.py

from pingouin import ttest

from .analysis_results import AnalysisResults
from .analysis_results import PairedTTestDetails


SIGNIFICANCE_LEVEL = 0.05


def analyse(baseline, candidate):
    stats = ttest(baseline.builds, candidate.builds, paired=True, tail='greater').round(3)
    tstatistic = stats.loc['T-test', 'T']
    pvalue = stats.loc['T-test', 'p-val']
    improvement_detected = pvalue < SIGNIFICANCE_LEVEL
    details = PairedTTestDetails(tstatistic, pvalue, SIGNIFICANCE_LEVEL)
    return AnalysisResults(baseline, candidate, details, improvement_detected)
