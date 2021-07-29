# app.py


from . import analysis_reporter
from . import benchmark_parser
from . import benchmarks_analyser
from . import cli_parser


def main(argv=None):
    baseline_csv, modified_csv = cli_parser.parse(argv)

    baseline = benchmark_parser.parse(baseline_csv)
    modified = benchmark_parser.parse(modified_csv)

    analysis = benchmarks_analyser.analyse(baseline, modified)
    analysis_reporter.report(analysis)
