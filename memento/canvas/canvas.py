from canvas_state import CanvasState

class Canvas:
    def __init__(self):
        self.__content = ""
        self.__color = ""
        self.__border = ""

    def get_content(self):
        return self.__content
        
    def set_content(self, content):
        self.__content = content
    
    def get_color(self):
        return self.__color
        
    def set_color(self, color):
        self.__color = color
    
    def get_border(self):
        return self.__border
        
    def set_border(self, border):
        self.__border = border

    def save(self):
        return CanvasState(self.__content, self.__color, self.__border)
    
    def restore(self, canvas_state: CanvasState):
        self.__content = canvas_state.get_content()
        self.__color = canvas_state.get_color()
        self.__border = canvas_state.get_border()

    