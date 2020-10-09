# benchmark_parser.py

import csv
import numpy

from .gradle_benchmark import GradleBenchmark


def parse(benchmark_file):
    try:
        with open(benchmark_file) as csv_file:
            data = csv.reader(csv_file, delimiter=',')

            builds = []
            task = ''

            for row in data:
                description = row[0]
                value = row[1]

                if 'measured build' in description:
                    builds.append(int(value))

                if 'tasks' in description:
                    task = value

            if(builds and task):
                # We now have to calculate mean and stddev by our own since
                # Gradle Profiler does not report these metrics in the CSV anymore
                mean = round(numpy.mean(builds), 2)
                stddev = round(numpy.std(builds), 2)
                return GradleBenchmark(benchmark_file, task, builds, mean, stddev)

    except:
        raise Exception(f"Can't parse benchmarks inputs from {benchmark_file}")
