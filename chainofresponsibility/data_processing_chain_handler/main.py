from data import Data
from validation_checks_handler import ValidationChecksHandler
from formatting_checks_handler import FormattingChecksHandler
from data_size_checks_handler import DataSizeChecksHandler
from data_processor import DataProcessor

def main():
    data = Data(True, True, True)
    validation_checks_handler = ValidationChecksHandler()
    formatting_checks_handler = FormattingChecksHandler()
    data_size_checks_handler = DataSizeChecksHandler()
    # Set up the chain of responsibility
    validation_checks_handler.set_next(formatting_checks_handler).set_next(data_size_checks_handler)
    data_processor = DataProcessor(validation_checks_handler)
    response = data_processor.process_data(data)
    print(f"Response: {response.get_result()}, Success: {response.is_succeeded()}")
if __name__ == "__main__":
    main()