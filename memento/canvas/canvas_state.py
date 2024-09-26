class CanvasState:
    def __init__(self, content, color, border):
        self.__content = content
        self.__color = color
        self.__border = border

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
