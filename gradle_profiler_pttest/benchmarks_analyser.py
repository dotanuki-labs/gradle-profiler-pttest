# benchmarks_analyser.py

from pingouin import ttest

from .analysis_results import AnalysisResults
from .analysis_results import PairedTTestDetails


SIGNIFICANCE_LEVEL = 0.050


def analyse(baseline, modified):
    stats = ttest(baseline.builds, modified.builds, paired=True, tail='greater').round(3)
    tstatistic = stats.loc['T-test', 'T']
    pvalue = stats.loc['T-test', 'p-val']
    improvement_detected = pvalue < SIGNIFICANCE_LEVEL
    details = PairedTTestDetails(tstatistic, pvalue, SIGNIFICANCE_LEVEL)
    return AnalysisResults(baseline, modified, details, improvement_detected)
