from text_editor_state import TextEditorState

class History:
    def __init__(self):
        self.__prev_states: TextEditorState = []

    def save_history_state(self, text_editor_state):
        self.__prev_states.append(text_editor_state)

    def undo(self):
        if self.__prev_states:
            return self.__prev_states.pop()
        else: 
            return None