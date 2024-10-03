from document import Document
from feature_visitor import FeatureVisitor

class SpreadSheet(Document):
    def accept(self, feature_visitor: FeatureVisitor):
        feature_visitor.visit_spread_sheet(self)
