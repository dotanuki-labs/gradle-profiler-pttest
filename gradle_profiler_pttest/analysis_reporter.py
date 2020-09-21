# analysis_reporter.py

from rich.console import Console
from rich.table import Table


def report(analysis):
    benchmarks = format_benchmarks(analysis)
    results = format_results(analysis)
    conclusion = format_conclusion(analysis)

    console = Console()

    console.print("\n🔥 [bold cyan]Paired T-test analysis for Gradle Profiler Benchmarks[/bold cyan]\n")
    console.print(f"[bold magenta]- Baseline[/bold magenta] → {analysis.baseline.benchmark_file}")
    console.print(f"[bold magenta]- Modified[/bold magenta] → {analysis.modified.benchmark_file}")

    console.print("\n🔥 [bold cyan]Details for benchmarks[/bold cyan]\n")
    console.print(benchmarks)

    console.print("\n🔥 [bold cyan]Outcomes from hyphotesis testing (h0 versus h1, left-tailed)[/bold cyan]\n")
    console.print(results)

    console.print("\n🔥 [bold cyan]Conclusions[/bold cyan]")
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
    results.add_column("Metric")
    results.add_column("Assigned value", justify="right")

    details = analysis.details
    results.add_row("Significance", format(details.significance_level, '.3f'))
    results.add_row("p-value", f"{details.pvalue}")

    return results


def format_conclusion(analysis):
    improved = analysis.improvement_detected
    accepted_prefix = "\nThe [cyan]p-value[/cyan] is lower than [cyan]significance level[/cyan]."
    rejected_prefix = "\nThe [cyan]p-value[/cyan] is greater than [cyan]significance level[/cyan]."
    conclusion_posfix = "for improvements with modified build conditions.\n"

    if improved:
        conclusion = "\nTherefore [green]we have strong statistical evidence[/green]"
        return f"{accepted_prefix} {conclusion} {conclusion_posfix}"
    else:
        conclusion = "\nTherefore we are [red]lacking strong statistical evidence[/red]"
        return f"{rejected_prefix} {conclusion} {conclusion_posfix}"
