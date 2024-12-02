from copy import deepcopy
from abc import ABC, abstractmethod

class MarketingMaterial(ABC):
    def __init__(self, layout, content, color):
        self.__layout = layout
        self.__content = content
        self.__color = color

    @property
    def layout(self):
        return self.__layout
    
    @layout.setter
    def layout(self, layout):
        self.__layout = layout

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    def print_material(self):
        print("Marketing Material Configuration:")
        print(f"Layout: {self.__layout}")
        print(f"Content: {self.__content}")
        print(f"Color: {self.__color}")
        print("Printing now ...")

    # Abstract method to be implemented by subclasses
    @abstractmethod
    def clone_marketing_material(self):
        pass

    # Clone method that leverages deepcopy
    def clone(self):
        # Creates a deep copy of the current object
        cloned_object = deepcopy(self)
        # Now we call the abstract method to clone the specific material
        return cloned_object.clone_marketing_material()