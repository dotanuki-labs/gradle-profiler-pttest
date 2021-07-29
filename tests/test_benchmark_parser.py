# test_benchmark_parser.py

import os
import pytest

from gradle_profiler_pttest import benchmark_parser
from gradle_profiler_pttest.gradle_benchmark import GradleBenchmark


FIXTURES_DIR = f"{os.getcwd()}/tests/fixtures/old-csv-format/samples"


def test_should_parse_single_task_gradle_benchmark():

    # Given
    csv = f"{FIXTURES_DIR}/benchmark-one-task.csv"

    # When
    parsed = benchmark_parser.parse(csv)

    # Then
    builds = [34123, 36909, 36047, 39181, 33351]
    mean = 35922.2
    stddev = 2071.58
    expected = GradleBenchmark(csv, builds, mean, stddev)

    assert parsed == expected


def test_should_parse_multiple_tasks_gradle_benchmark():

    # Given
    csv = f"{FIXTURES_DIR}/benchmark-two-tasks.csv"

    # When
    parsed = benchmark_parser.parse(csv)

    # Then
    builds = [155132, 147981, 148263]
    mean = 150458.67
    stddev = 3306.55
    expected = GradleBenchmark(csv, builds, mean, stddev)

    assert parsed == expected


def test_should_handle_corrupted_benchmark():

    # Given
    csv = f"{FIXTURES_DIR}/benchmark-corrupted.csv"

    # When
    parsed = benchmark_parser.parse(csv)

    # Then
    assert parsed is None


def test_should_handle_error_when_opening_benchmark_file():
    with pytest.raises(Exception) as error:
        # Given
        csv = f"{FIXTURES_DIR}/missing.csv"

        # When
        benchmark_parser.parse(csv)

        # Then
        assert "Can't parse benchmarks inputs" in str(error.value)
