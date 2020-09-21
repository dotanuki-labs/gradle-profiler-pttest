# test_benchmarks_analyser.py

from gradle_profiler_pttest import benchmarks_analyser
from gradle_profiler_pttest.gradle_benchmark import GradleBenchmark


def test_should_detect_improvement_with_pttest():

    # Given
    task = 'mobile:assembleDebug'

    baseline_builds = [34123, 36909, 36047, 39181, 33351]
    baseline_mean = 35922.2
    baseline_stddev = 2316.1
    baseline = GradleBenchmark("baseline.csv", task, baseline_builds, baseline_mean, baseline_stddev)

    candidate_builds = [22123, 26909, 27047, 29181, 23351]
    candidate_mean = 25722.2
    candidate_stddev = 2902.7
    candidate = GradleBenchmark("modified.csv", task, candidate_builds, candidate_mean, candidate_stddev)

    # When
    results = benchmarks_analyser.analyse(baseline, candidate)

    # Then
    assert results.improvement_detected


def test_should_detect_no_improvements_with_pttest():

    # Given
    task = 'mobile:assembleDebug'

    baseline_builds = [34123, 36909, 36047, 39181, 33351]
    baseline_mean = 35922.2
    baseline_stddev = 2316.1
    baseline = GradleBenchmark("baseline.csv", task, baseline_builds, baseline_mean, baseline_stddev)

    candidate_builds = [34100, 37000, 36100, 39200, 33400]
    candidate_mean = 35960.0
    candidate_stddev = 2324.4
    candidate = GradleBenchmark("modified.csv", task, candidate_builds, candidate_mean, candidate_stddev)

    # When
    results = benchmarks_analyser.analyse(baseline, candidate)

    # Then
    assert not results.improvement_detected
