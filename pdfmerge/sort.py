from os import path

from .constants import PDF_EXT


def sort_by_number(pdfs: list[str], base_filenames: list[str]) -> list[str]:
    response = input("Detected all pdfs are numbered. Sort by number? [y/N] ") or "n"
    if response.lower() == "n":
        return pdfs

    direction = input("Sort ascending or descending? [A/d] ") or "a"
    descending = direction.lower() == "d"

    return [
        str(x) + PDF_EXT for x in sorted(map(int, base_filenames), reverse=descending)
    ]


def sort_by_name(pdfs: list[str]) -> list[str]:
    base_filenames = [pdf[: -len(PDF_EXT)] for pdf in pdfs]
    if all(map(str.isdigit, base_filenames)):
        return sort_by_number(pdfs, base_filenames)
    return sorted(pdfs)


def sort_by_date(pdfs: list[str]) -> list[str]:
    return sorted(pdfs, key=path.getmtime)


no_sort = lambda x: x

SORT_LOOKUP = {
    "n": (sort_by_name, "name"),
    "d": (sort_by_date, "date"),
    "x": (no_sort, "don't sort"),
}


def sort_pdfs(pdfs: list[str]) -> list[str]:
    print("\n=== Sorting PDFs ===")
    key = input(
        "Sort by:\n"
        + "\n".join(f"  {k}: {v[1]}" for k, v in SORT_LOOKUP.items())
        + "\n"
    )

    sorter, ref = SORT_LOOKUP.get(key, SORT_LOOKUP["x"])
    if sorter == no_sort:
        return pdfs

    print(f"Sorting by: {ref}")
    pdfs = sorter(pdfs)
    print(f"Sorted files: {pdfs}")
    return pdfs
