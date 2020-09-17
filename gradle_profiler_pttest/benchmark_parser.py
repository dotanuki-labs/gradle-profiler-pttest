# benchmark_parser.py

import csv

from .gradle_benchmark import GradleBenchmark

DESCRIPTIONS = 0
VALUES = 1


def parse(benchmark_file):
    with open(benchmark_file) as csv_file:

        data = csv.reader(csv_file, delimiter=',')

        builds = []
        task = ''
        mean = 0.0
        stddev = 0.0

        for row in data:
            if 'measured build' in row[DESCRIPTIONS]:
                builds.append(int(row[VALUES]))

            if 'mean' in row[DESCRIPTIONS]:
                mean = row[VALUES]

            if 'stddev' in row[DESCRIPTIONS]:
                stddev = row[VALUES]

            if 'tasks' in row[DESCRIPTIONS]:
                task = row[VALUES]

        return GradleBenchmark(task, builds, mean, stddev)
