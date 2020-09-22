# cli_parser.py

import argparse


HELP_PREFIX = 'Path to the CSV file generated by Gradle Profiler'


def parse(args):
    parser = argparse.ArgumentParser(
        prog='gradle-profiler-pttest',
        description='Paired T-test for Gradle Profiler benchmakrs'
    )

    parser.add_argument(
        '-b',
        '--baseline',
        action='store',
        required=True,
        help=f"{HELP_PREFIX}, benchmarking the status quo"
    )

    parser.add_argument(
        '-m',
        '--modified',
        action='store',
        required=True,
        help=f"{HELP_PREFIX}, benchmarking the modifications applied"
    )

    try:
        parsed = parser.parse_args(args)
        return [parsed.baseline, parsed.modified]
    except:
        message = "Could not recoginze program arguments. Run with --help to learn more"
        raise Exception(message)
