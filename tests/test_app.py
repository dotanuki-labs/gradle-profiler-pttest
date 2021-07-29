# test_app.py

import os
import pytest

from gradle_profiler_pttest import app

FIXTURES_DIR = f"{os.getcwd()}/tests/fixtures"


def test_should_reject_improvements_given_benchmarks(capsys):

    # Given
    baseline = f"{FIXTURES_DIR}/old-csv-format/sdksearch/jdk8/benchmark.csv"
    modified = f"{FIXTURES_DIR}/old-csv-format/sdksearch/jdk11/benchmark.csv"

    # When
    argv = ["-b", baseline, "-m", modified]
    app.main(argv)

    # Then
    captured = capsys.readouterr()
    assert "p-value is greater than significance level" in captured.out
    assert "we are lacking strong statistical evidence for improvements" in captured.out


def test_should_accept_improvements_given_benchmarks_in_the_old_format(capsys):

    # Given
    baseline = f"{FIXTURES_DIR}/old-csv-format/iosched/outdated-agp/benchmark.csv"
    modified = f"{FIXTURES_DIR}/old-csv-format/iosched/updated-agp/benchmark.csv"

    # When
    argv = ["-b", baseline, "-m", modified]
    app.main(argv)

    # Then
    captured = capsys.readouterr()
    assert "p-value is smaller than significance level" in captured.out
    assert "we have strong statistical evidence for improvements" in captured.out


def test_should_accept_improvements_given_benchmarks_in_the_new_format(capsys):

    # Given
    baseline = f"{FIXTURES_DIR}/new-csv-format/h0/benchmark.csv"
    modified = f"{FIXTURES_DIR}/new-csv-format/h1/benchmark.csv"

    # When
    argv = ["-b", baseline, "-m", modified]
    app.main(argv)

    # Then
    captured = capsys.readouterr()
    assert "p-value is smaller than significance level" in captured.out
    assert "we have strong statistical evidence for improvements" in captured.out


def test_should_report_execution_errors(caplog):

    with pytest.raises(Exception):

        # Given
        baseline = f"{FIXTURES_DIR}/old-csv-format/iosched/outdated-agp/benchmark.csv"
        modified = f"{FIXTURES_DIR}/old-csv-format/iosched/new-agp/benchmark.csv"  # does not exist

        # When
        argv = ["-b", baseline, "-m", modified]
        app.main(argv)

        # Then
        assert "Error when parsing benchmark" in caplog.text
        assert "Could not complete analysis" in caplog.text
