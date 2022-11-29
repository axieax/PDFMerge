from argparse import ArgumentParser
from typing import cast

from pdfmerge import Args, main

# TODO: vim interface to manipulate files

if __name__ == "__main__":
    # CLI args
    parser = ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("-o", "--output", help="output filename")
    args = parser.parse_args()
    args = cast(Args, args)
    print(args)

    main(args)
