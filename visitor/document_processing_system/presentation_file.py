from document import Document
from feature_visitor import FeatureVisitor

class PresentationFile(Document):
    def accept(self, feature_visitor: FeatureVisitor):
        feature_visitor.visit_presentation_file(self)
