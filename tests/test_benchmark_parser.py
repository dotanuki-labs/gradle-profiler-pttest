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
    mean = 36435.26
    stddev = 3062.13
    expected = GradleBenchmark(csv, task, builds, mean, stddev)

    assert parsed == expected


def test_should_parse_multiple_tasks_gradle_benchmark():

    # Given
    csv = f"{FIXTURES_DIR}/benchmark-two-tasks.csv"

    # When
    parsed = benchmark_parser.parse(csv)

    # Then
    task = 'app:assembleDebug'
    builds = [155132, 147981, 148263]
    mean = 151303.3
    stddev = 4436.15
    expected = GradleBenchmark(csv, task, builds, mean, stddev)

    assert parsed == expected


def test_should_handle_corrupted_benchmark():

    # Given
    csv = f"{FIXTURES_DIR}/benchmark-corrupted.csv"

    # When
    parsed = benchmark_parser.parse(csv)

    # Then
    assert parsed is None
