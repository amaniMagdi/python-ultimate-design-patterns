from json_message_formatter import JsonMessageFormatter
from plain_message_formatter import PlainMessageFormatter
from xml_message_formatter import XMLMessageFormatter

def main():
    message_formatters = [
        JsonMessageFormatter(),
        PlainMessageFormatter(),
        XMLMessageFormatter()
    ]
    test_message = "Hello, World!"
    for message_formatter in message_formatters:
        formatted_message = message_formatter.format_message(test_message)
        print(f"Formatter type: {message_formatter.get_type()}")
        print(f"Formatted message: {formatted_message}")
        print()


if __name__ == "__main__":
    main()