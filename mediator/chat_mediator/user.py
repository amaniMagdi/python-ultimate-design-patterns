class User:
    def __init__(self, name, chat_mediator):
        self._name = name
        self._chat_mediator = chat_mediator


    def send_direct_message(self, message, to_user):
        self._chat_mediator.send_direct_message(message, to_user, self)

    def receive_direct_message(self, message, from_user):
        print(f"{self._name} is receiving message: {message} from user: {from_user.get_name()}")

    def send_group_message(self, message, group_name): 
        self._chat_mediator.send_group_message(message, self, group_name)
    
    def receive_group_message(self, message, from_user, group_name):
        print(f"{self._name} is receiving message: {message} from group: {group_name} from user: {from_user.get_name()}")

    def get_name(self):
        return self._name
    

