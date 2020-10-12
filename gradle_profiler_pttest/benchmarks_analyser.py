# benchmarks_analyser.py

import logging

from pingouin import ttest

from .analysis_results import AnalysisResults
from .analysis_results import PairedTTestDetails


SIGNIFICANCE_LEVEL = 0.050


def analyse(baseline, modified):
    try:
        stats = ttest(baseline.builds, modified.builds, paired=True, tail='greater').round(3)
        tstatistic = stats.loc['T-test', 'T']
        pvalue = stats.loc['T-test', 'p-val']
        improvement_detected = pvalue < SIGNIFICANCE_LEVEL
        details = PairedTTestDetails(tstatistic, pvalue, SIGNIFICANCE_LEVEL)
        return AnalysisResults(baseline, modified, details, improvement_detected)
    except:
        logging.exception("Error when runnig analyser")
        raise Exception('Failed when runnig analyser for benchmarks')
