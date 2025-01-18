"""learn logging 3/3"""

import logging


def get_logger():
    """advanced usage:
    logger, formatter and handler:
        1) create formatter - formatter.datefmt
        2) create handler - handler.setFormatter(formatter)
        3) create logger - logger.setLevel; logger.addHandler(handler)
    """
    # Create logger with the name "my_logger"
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)  # Set log level

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    formatter.datefmt = "%Y-%m-%d %H:%M:%S"

    # Create handler, and set formatter on handler
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Create a file handler and set its level
    file_handler = logging.FileHandler("logging/opening_03.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def main():
    """main"""
    logger = get_logger()

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")


if __name__ == "__main__":
    main()
