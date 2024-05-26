import logging

# Configure logger
logger = logging.getLogger('System')
logger.setLevel(logging.DEBUG)  # Set to the lowest level to capture all messages

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('sys.log')

# Set logging level for each handler
console_handler.setLevel(logging.INFO)  # Log INFO and above to stdout
file_handler.setLevel(logging.DEBUG)    # Log DEBUG and above to file

# Create and set formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)