from abc import ABC, abstractmethod

class FeatureVisitor(ABC):
    @abstractmethod
    def visit_text_file(self, text_file):
        pass

    @abstractmethod
    def visit_spread_sheet(self, spread_sheet):
        pass

    @abstractmethod
    def visit_presentation_file(self, presentation_file):
        pass
