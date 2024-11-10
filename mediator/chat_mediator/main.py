from chat_management import ChatManagement
from user import User

def main():
    # Create an instance of ChatManagement (ChatMediator)
    chat_mediator = ChatManagement()

    # Create User instances
    user1 = User("Alice", chat_mediator)
    user2 = User("Bob", chat_mediator)
    user3 = User("Charlie", chat_mediator)
    user4 = User("Dave", chat_mediator)

    # Register users to groups
    chat_mediator.register_user_to_group(user1, "Group1")
    chat_mediator.register_user_to_group(user2, "Group1")
    chat_mediator.register_user_to_group(user3, "Group2")
    chat_mediator.register_user_to_group(user4, "Group2")
    
    # Send a direct message from user1 to user2
    user1.send_direct_message("Hello, Bob!", user2)
    
    # Send a group message from user1 to "Group1"
    user1.send_group_message("Hi Group1 members!", "Group1")
    
    # Send a group message from user3 to "Group2"
    user3.send_group_message("Hello Group2!", "Group2")

# Run the main function to test
if __name__ == "__main__":
    main()
