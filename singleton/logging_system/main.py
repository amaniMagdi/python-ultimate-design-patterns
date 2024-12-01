from log_level import LogLevel
from logger import Logger

def main():
    # Get the singleton instance of Logger
    logger = Logger.get_instance()

    # Set the log level to DEBUG
    logger.set_log_level(LogLevel.DEBUG)

    # Test logging at various levels
    print("Testing with log level set to DEBUG:")
    logger.log_debug("This is a debug message.")  # Should log
    logger.log_info("This is an info message.")  # Should log
    logger.log_warn("This is a warning message.")  # Should log
    logger.log_error("This is an error message.")  # Should log

    # Set the log level to INFO
    logger.set_log_level(LogLevel.INFO)

    print("\nTesting with log level set to INFO:")
    logger.log_debug("This is a debug message.")  # Should NOT log
    logger.log_info("This is an info message.")  # Should log
    logger.log_warn("This is a warning message.")  # Should log
    logger.log_error("This is an error message.")  # Should log

    # Set the log level to WARN
    logger.set_log_level(LogLevel.WARN)

    print("\nTesting with log level set to WARN:")
    logger.log_debug("This is a debug message.")  # Should NOT log
    logger.log_info("This is an info message.")  # Should NOT log
    logger.log_warn("This is a warning message.")  # Should log
    logger.log_error("This is an error message.")  # Should log

    # Set the log level to ERROR
    logger.set_log_level(LogLevel.ERROR)

    print("\nTesting with log level set to ERROR:")
    logger.log_debug("This is a debug message.")  # Should NOT log
    logger.log_info("This is an info message.")  # Should NOT log
    logger.log_warn("This is a warning message.")  # Should NOT log
    logger.log_error("This is an error message.")  # Should log

    # Attempt to get a second instance (Should still be the same instance)
    second_logger = Logger.get_instance()
    print("\nBoth logger instances are the same:", logger is second_logger)

if __name__ == "__main__":
    main()
