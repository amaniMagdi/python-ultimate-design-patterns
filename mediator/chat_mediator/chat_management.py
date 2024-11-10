from chat_mediator import ChatMediator
class ChatManagement(ChatMediator):
    def __init__(self):
        self._groups = {}

    def send_direct_message(self, message, to_user, from_user):
        print(f"{from_user.get_name()} is sending a direct message {message}to {to_user.get_name()}")
        to_user.receive_direct_message(message, from_user)

    def send_group_message(self, message, from_user, to_group):
        print(f"{from_user.get_name()} is sending message: {message} to group: {to_group}")
        users = self._groups.get(to_group, [])
        for user in users:
            user.receive_group_message(message, from_user, to_group)
    
    def register_user_to_group(self, user, group_name):
        if group_name not in self._groups:
            self._groups[group_name] = []
        self._groups[group_name].append(user)