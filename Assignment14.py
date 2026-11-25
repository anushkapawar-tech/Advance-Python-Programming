import logging

# Configure logging
logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Different logging levels
logging.debug("This is a debug message")
logging.info("Application started successfully")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("This is a critical error")

# Demonstrate logging in a function
def divide(a, b):
    logging.info("Division operation started")

    try:
        result = a / b
        logging.info("Division completed successfully")
        return result

    except ZeroDivisionError:
        logging.exception("Cannot divide by zero")
        return None


# Perform operations
print("Result:", divide(10, 2))
print("Result:", divide(10, 0))

print("Check application.log for log messages.")
