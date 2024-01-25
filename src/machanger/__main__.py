from .pipeline import Pipeline


def main() -> None:
    pipeline = Pipeline()

    pipeline.handle_arg_parsing()

    pipeline.handle_arg_validation()

    pipeline.handle_changing_mac()


if __name__ == "__main__":
    main()
