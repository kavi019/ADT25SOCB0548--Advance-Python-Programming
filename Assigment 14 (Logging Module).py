import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def perform_operation(value):
    logging.info(f"Operation started with value: {value}")
    if value < 0:
        logging.warning("Negative value received; results may vary.")
    elif value == 0:
        logging.error("Zero value received, cannot proceed further.")
        raise ValueError("Value cannot be zero")
    logging.info("Operation completed successfully.")


if __name__ == "__main__":
    print("--- Logging Demo ---")
    perform_operation(10)
    perform_operation(-5)
    try:
        perform_operation(0)
    except ValueError:
        logging.critical("Caught critical error from zero input.")
    print("Logs have been saved to 'app.log'. Check your explorer sidebar.")