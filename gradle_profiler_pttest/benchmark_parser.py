# benchmark_parser.py

import csv

from .gradle_benchmark import GradleBenchmark


def parse(benchmark_file):
    with open(benchmark_file) as csv_file:

        data = csv.reader(csv_file, delimiter=',')

        builds = []
        task = ''
        mean = ''
        stddev = ''

        for row in data:
            description = row[0]
            value = row[1]

            if 'measured build' in description:
                builds.append(int(value))

            if 'mean' in description:
                mean = value

            if 'stddev' in description:
                stddev = value

            if 'tasks' in description:
                task = value

        if(values_ensured(builds, task, mean,stddev)):
            return GradleBenchmark(task, builds, mean, stddev)


def values_ensured(*values):
    for value in values:
        if not value:
            return False

    return True
