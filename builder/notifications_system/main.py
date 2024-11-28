from messenger_notification_builder import MessengerNotificationBuilder
from slack_notification_builder import SlackNotificationBuilder

def main():
    # Create a MessengerNotification using the builder pattern
    builder = MessengerNotificationBuilder()
    notification = (
        builder
        .set_content("Project deadline reminder!")
        .set_sender("Team Lead")
        .set_recipient("Development Team")
        .set_timestamp("2024-11-28T14:00:00Z")
        .set_attachments(["requirements.pdf", "timeline.xlsx"])
        .set_theme("urgent")
        .build()
    )

    # Display notification properties for messenger
    print("Messenger Notification Details:")
    print(f"Content: {notification.get_content()}")
    print(f"Sender: {notification.get_sender()}")
    print(f"Recipient: {notification.get_recipient()}")
    print(f"Timestamp: {notification.get_timestamp()}")
    print(f"Attachments: {notification.get_attachments()}")
    print(f"Theme: {notification.get_theme()}")


    # Create a builder instance for slack
    builder = SlackNotificationBuilder()

     # Use method chaining to set the values and build the SlackNotification
    slack_notification = (
        builder
        .set_content("System maintenance at midnight.")
        .set_sender("Admin")
        .set_recipient("All Users")
        .set_timestamp("2024-11-29T00:00:00Z")
        .set_markdown_language(True)
        .build()
    )

    # Print the details of the built SlackNotification
    print("Slack Notification Details:")
    print(f"Content: {slack_notification.get_content()}")
    print(f"Sender: {slack_notification.get_sender()}")
    print(f"Recipient: {slack_notification.get_recipient()}")
    print(f"Timestamp: {slack_notification.get_timestamp()}")
    print(f"Has Markdown Language: {slack_notification.has_markdown_language()}")

if __name__ == "__main__":
    main()
