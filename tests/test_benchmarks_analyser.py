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

    modified_builds = [22123, 26909, 27047, 29181, 23351]
    modified_mean = 25722.2
    modified_stddev = 2902.7
    modified = GradleBenchmark("modified.csv", task, modified_builds, modified_mean, modified_stddev)

    # When
    results = benchmarks_analyser.analyse(baseline, modified)

    # Then
    assert results.improvement_detected


def test_should_detect_no_improvements_with_pttest():

    # Given
    task = 'mobile:assembleDebug'

    baseline_builds = [34123, 36909, 36047, 39181, 33351]
    baseline_mean = 35922.2
    baseline_stddev = 2316.1
    baseline = GradleBenchmark("baseline.csv", task, baseline_builds, baseline_mean, baseline_stddev)

    modified_builds = [34100, 37000, 36100, 39200, 33400]
    modified_mean = 35960.0
    modified_stddev = 2324.4
    modified = GradleBenchmark("modified.csv", task, modified_builds, modified_mean, modified_stddev)

    # When
    results = benchmarks_analyser.analyse(baseline, modified)

    # Then
    assert not results.improvement_detected
