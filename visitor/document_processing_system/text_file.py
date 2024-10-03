from document import Document
from feature_visitor import FeatureVisitor

class TextFile(Document):
    def accept(self, feature_visitor: FeatureVisitor):
        feature_visitor.visit_text_file(self)
