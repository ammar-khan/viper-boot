#!/usr/bin/env python
"""Script for converting ``.coverage`` SQLite output into lint-style output.

The output is suitable for consumption using Darker.

See https://github.com/akaihola/darker

Example usage, pointing out modified code in a feature branch not covered by
the test suite::

    pip install pytest-cov darker
    curl -O $HOME/.local/bin/cov_to_lint.py \
      https://gist.githubusercontent.com/akaihola/2511fe7d2f29f219cb995649afd3d8d2/raw/
    cd $HOME/mypackage
    git checkout my-feature-branch
    pytest --cov=mypackage src
    ls coverage.xml
    darker --revision master --lint cov_to_lint.py src

"""
from typing import List
from typing import TextIO

from coverage import Coverage
from coverage.report import get_analysis_to_report
from coverage.report import render_report


class LintReporter:  # pylint: disable=too-few-public-methods
    """Linter reporter class."""

    @staticmethod
    def report(morfs: List[str], outfile: TextIO) -> None:
        """Report missing coverage while linting.

        Parameters:
            morfs (List[str]): morfs
            outfile (TextIO): output file
        """
        cov = Coverage(include="./***")
        cov.load()
        for file_reporters, analysis in get_analysis_to_report(cov, morfs):
            longest_location = 0
            shortest_indent = 16
            lines = []
            for linenum in sorted(analysis.missing):
                line = file_reporters.parser.lines[linenum - 1]
                lines.append((linenum, line))
                longest_location = max(
                    longest_location,
                    len(f"{file_reporters.filename}:{linenum}:")
                )
                indent = len(line) - len(line.lstrip())
                shortest_indent = min(shortest_indent, indent)
            prev_linenum = 0
            for linenum, line in lines:
                if linenum > prev_linenum + 1:
                    outfile.write("\n")
                prev_linenum = linenum
                location = f"{file_reporters.filename}:{linenum}:"
                outfile.write(
                    f"{location:{longest_location}} no coverage:"
                    f" {line[shortest_indent:]}\n"
                )


def main() -> None:
    """Render missing coverage report."""
    render_report("-", LintReporter, morfs=[])


if __name__ == "__main__":
    main()
