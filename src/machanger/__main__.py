from .argparser import ArgParser
from .changer import change_mac


def main() -> None:
    # Create an ArgParser instance and add options
    parser = ArgParser()
    parser.add_options()

    # Parse command line arguments
    args = parser.parse_args()

    # Perform actions based on parsed arguments
    if args.interface:
        print(f"Changing MAC address for interface {args.interface}")


if __name__ == "__main__":
    main()
