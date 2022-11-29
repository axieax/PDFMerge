from dataclasses import dataclass

from .merge import merge_pdfs
from .select import select_pdfs
from .sort import sort_pdfs


@dataclass
class Args:
    files: list[str]
    output: str | None


def main(cli_args: Args):
    print(
        r"""
  _____  _____  ______ __  __
 |  __ \|  __ \|  ____|  \/  |
 | |__) | |  | | |__  | \  / | ___ _ __ __ _  ___
 |  ___/| |  | |  __| | |\/| |/ _ \ '__/ _` |/ _ \
 | |    | |__| | |    | |  | |  __/ | | (_| |  __/
 |_|    |_____/|_|    |_|  |_|\___|_|  \__, |\___|
                                        __/ |
                                       |___/
          """
    )
    pdfs = select_pdfs(cli_args.files)
    pdfs = sort_pdfs(pdfs)
    merge_pdfs(pdfs, cli_args.output)
