import logging


def get_logger():
    # Create logger
    logger = logging.getLogger("arjancodes")

    # Create handler
    handler = logging.StreamHandler()

    # Create formatter
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    formatter.datefmt = "%Y-%m-%d %H:%M:%S"

    # Set formatter on handler
    handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(handler)

    # Set log level
    logger.setLevel(logging.INFO)

    return logger


def main():
    logger = get_logger()

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")


if __name__ == "__main__":
    main()
