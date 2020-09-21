# analysis_reporter.py

from rich.console import Console
from rich.table import Table


def report(analysis):
    benchmarks = format_benchmarks(analysis)
    results = format_results(analysis)
    conclusion = format_conclusion(analysis)

    console = Console()

    console.print("\n🔥 [bold cyan]Paired T-test for Gradle Profiler Benchmarks[/bold cyan]")
    console.print(f"\n [bold magenta]Baseline[/bold magenta] → {analysis.baseline.benchmark_file}")
    console.print(f"\n [bold magenta]Modified[/bold magenta] → {analysis.modified.benchmark_file}\n")

    console.print("\n🔥 [bold cyan]Details for benchmarks[/bold cyan]\n")
    console.print(benchmarks)

    console.print("\n🔥 [bold cyan]Outcomes from the left-tailed Paired T-test[/bold cyan]\n")
    console.print(results)
    console.print(conclusion)


def format_benchmarks(analysis):
    h0 = analysis.baseline
    h1 = analysis.modified

    benchmarks = Table(show_header=True, header_style="bold magenta")
    benchmarks.pad_edge = False
    benchmarks.add_column("Benchmark")
    benchmarks.add_column("Measured builds", justify="right")
    benchmarks.add_column("Mean", justify="right")
    benchmarks.add_column("Standard Deviation", justify="right")

    benchmarks.add_row("baseline (h0)", f"{len(h0.builds)}", format(h0.mean, '.2f'), format(h0.stddev, '.2f'))
    benchmarks.add_row("modified (h1)", f"{len(h1.builds)}", format(h1.mean, '.2f'), format(h1.stddev, '.2f'))

    return benchmarks


def format_results(analysis):
    results = Table(show_header=True, header_style="bold magenta")
    results.pad_edge = False
    results.add_column("Statistic Metric")
    results.add_column("Value")

    details = analysis.details
    results.add_row("Significance Level", f"{details.significance_level}")
    results.add_row("p-value", f"{details.pvalue}")

    return results


def format_conclusion(analysis):
    improved = analysis.improvement_detected
    accepted_prefix = "\n⚡️ [cyan]p-value[/cyan] is lower than [cyan]significance level[/cyan]\n"
    rejected_prefix = "\n⚡️ [cyan]p-value[/cyan] is greater than [cyan]significance level[/cyan]\n"
    conclusion_posfix = "for improvements with modified build conditions.\n"

    if improved:
        conclusion = "\nTherefore [green]we have strong statistical evidence[/green]"
        return f"{accepted_prefix} {conclusion} {conclusion_posfix}"
    else:
        conclusion = "\nTherefore we are [red]lacking strong statistical evidence[/red]"
        return f"{rejected_prefix} {conclusion} {conclusion_posfix}"
