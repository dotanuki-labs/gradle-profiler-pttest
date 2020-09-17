# test_benchmark_parser.py

import os

from gradle_profiler_pttest import benchmark_parser
from gradle_profiler_pttest.gradle_benchmark import GradleBenchmark


FIXTURES_DIR = f"{os.getcwd()}/tests/fixtures"


def test_should_parse_single_task_gradle_benchmark():

    # Given
    csv = f"{FIXTURES_DIR}/benchmark-one-task.csv"

    # When
    parsed = benchmark_parser.parse(csv)

    # Then
    task = 'mobile:assembleDebug'
    builds = [34123, 36909, 36047, 39181, 33351]
    mean = '36435.26666666667'
    stddev = '3062.134233939895'
    expected = GradleBenchmark(task, builds, mean, stddev)

    assert parsed == expected
