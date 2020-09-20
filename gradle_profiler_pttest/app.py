# app.py

from . import analysis_reporter
from .analysis_results import AnalysisResults
from .analysis_results import PairedTTestDetails
from .gradle_benchmark import GradleBenchmark


def main(argv=None):
    test_report()


def test_report():
    task = 'mobile:assembleDebug'

    baseline_builds = [34123, 36909, 36047, 39181, 33351]
    baseline_mean = '35922.2'
    baseline_stddev = '2316.1'
    baseline = GradleBenchmark(task, baseline_builds, baseline_mean, baseline_stddev)

    candidate_builds = [22123, 26909, 27047, 29181, 23351]
    candidate_mean = '25722.2'
    candidate_stddev = '2902.7'
    candidate = GradleBenchmark(task, candidate_builds, candidate_mean, candidate_stddev)

    details = PairedTTestDetails(4.0, 0.01, 0.05)
    analysis = AnalysisResults(baseline, candidate, details, True)
    analysis_reporter.report(analysis)
