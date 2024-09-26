class TextEditorState:
    def __init__(self, content):
        self.__content = content

    def get_content(self):
        return self.__content
        
    def set_content(self, content):
        self.__content = content
