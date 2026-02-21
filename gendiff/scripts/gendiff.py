import argparse  # NOSONAR

from gendiff import generate_diff


def main():  # NOSONAR
    parser = argparse.ArgumentParser(  # NOSONAR
        prog="gendiff",
        usage="gendiff [-h] [-f FORMAT] first_file second_file",
        description="Compares two configuration files and shows a difference.",
    )

    parser.add_argument(  # NOSONAR
        "-f",
        "--format",
        dest="format",
        metavar="FORMAT",
        default="stylish",
        choices=["stylish", "plain", "json"],
        help="set format of output (default: stylish)",
    )  # NOSONAR

    parser.add_argument("first_file")  # NOSONAR
    parser.add_argument("second_file")  # NOSONAR

    args = parser.parse_args()  # NOSONAR

    diff = generate_diff(  # NOSONAR
        args.first_file, args.second_file, args.format # NOSONAR
    )  # NOSONAR
    print(diff)  # NOSONAR


if __name__ == "__main__":  # NOSONAR
    main()  # NOSONAR
