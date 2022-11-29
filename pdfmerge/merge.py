from os import path

from PyPDF2 import PdfMerger

from .constants import DEFAULT_OUTPUT_FILENAME


def get_output_filename(output_filename: str | None) -> str:
    while not output_filename:
        output_filename = (
            input(f"Enter output filename (default: {DEFAULT_OUTPUT_FILENAME}): ")
            or DEFAULT_OUTPUT_FILENAME
        )

        if path.exists(output_filename):
            response = (input("File exists. Overwrite? [y/N] ") or "n").lower()
            if response == "y":
                return output_filename
            output_filename = None

    return output_filename


def merge_pdfs(pdfs: list[str], cli_output_filename: str | None) -> None:
    print("\n=== Merging PDFs ===")

    output_filename = get_output_filename(cli_output_filename)

    print(f"Output filename: {output_filename}")

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_filename)
    merger.close()

    print(f"PDFMerge Success! Output saved to {path.abspath(output_filename)}")
