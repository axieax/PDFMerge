from os import listdir, path

from .constants import PDF_EXT


def validate_files(files):
    for file in files:
        if not path.isfile(file):
            raise FileNotFoundError(file)
        if not file.endswith(PDF_EXT):
            raise ValueError(f"{file} is not a PDF")


def guess_pdfs() -> list[str]:
    print("No filenames provided. Finding PDFs in current directory...")
    # guess from current directory
    base_names = sorted(x[: -len(PDF_EXT)] for x in listdir(".") if x.endswith(PDF_EXT))
    # reattach extension
    return [x + PDF_EXT for x in base_names]


def select_pdfs(cli_files: list[str]):
    print("\n=== Selecting PDFs ===")
    files = cli_files or guess_pdfs()
    validate_files(files)
    print(f"Selected files: {files}")
    return files
