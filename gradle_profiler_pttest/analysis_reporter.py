# analysis_reporter.py

from rich.console import Console
from rich.table import Table


def report(analysis):
    benchmarks = format_benchmarks(analysis)
    results = format_results(analysis)
    conclusion = format_conclusion(analysis)

    console = Console()
    console.print("\n🔥 [bold cyan]Provided Samples[/bold cyan]")
    console.print("\n [bold]Baseline builds[/bold] → ~/Desktop/benchmarks/test01/benchmark.csv")
    console.print("\n [bold]Modified builds[/bold] → ~/Desktop/benchmarks/test02/benchmark.csv\n")

    console.print("\n🔥 [bold cyan]Details for benchmarks[/bold cyan]\n")
    console.print(benchmarks)
    console.print("\n🔥 [bold cyan]Outcomes from the left-tailed Paired T-test[/bold cyan]\n")
    console.print(results)
    console.print(conclusion)


def format_benchmarks(analysis):
    h0 = analysis.baseline
    h1 = analysis.candidate

    benchmarks = Table(show_header=True, header_style="bold magenta")
    benchmarks.pad_edge = False
    benchmarks.add_column(analysis.baseline.gradle_task)
    benchmarks.add_column("Measured builds", justify="right")
    benchmarks.add_column("Mean", justify="right")
    benchmarks.add_column("Standard Deviation", justify="right")

    benchmarks.add_row("baseline (h0)", f"{len(h0.builds)}", h0.mean, h0.stddev)
    benchmarks.add_row("modified (h1)", f"{len(h1.builds)}", h1.mean, h1.stddev)

    return benchmarks


def format_results(analysis):
    results = Table(show_header=True, header_style="bold magenta")
    results.pad_edge = False
    results.add_column("Statistic Metric")
    results.add_column("Value")

    details = analysis.details
    results.add_row("t-stastistic", f"{details.t_statistic}")
    results.add_row("significance level", f"{details.significance_level}")
    results.add_row("p-value", f"{details.pvalue}")

    return results


def format_conclusion(analysis):
    improved = analysis.improvement_detected
    accepted_prefix = "\n🔥 [cyan]p-value[/cyan] is lower than [cyan]significance level[/cyan]\n"
    rejected_prefix = "\n🔥 [cyan]p-value[/cyan] is greater than [cyan]significance level[/cyan]\n"
    conclusion_posfix = "for improvements with modified build conditions.\n"

    if improved:
        conclusion = "\nTherefore [green]we have strong statistical evidence[/green]"
        return f"{accepted_prefix} {conclusion} {conclusion_posfix}"
    else:
        conclusion = "\nTherefore we are [red]lacking strong statistical evidence[/red]"
        return f"{rejected_prefix} {conclusion} {conclusion_posfix}"
