"""learn logging 1/3"""
import logging


def main() -> None:
    """most basic usage:
    control on logging level only"""

    logging.basicConfig(level=logging.INFO)

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")


if __name__ == "__main__":
    main()
