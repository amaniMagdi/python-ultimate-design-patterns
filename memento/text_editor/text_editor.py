from text_editor_state import TextEditorState

class TextEditor:
    def __init__(self):
        self.__content = ""

    def get_content(self):
        return self.__content
        
    def set_content(self, content):
        self.__content = content

    def save(self):
        return TextEditorState(self.__content)
    
    def restore(self, text_editor_state: TextEditorState):
        self.__content = text_editor_state.get_content()