from abc import ABC, abstractmethod
from document import Document
from feature_visitor import FeatureVisitor

class AnalyzeFormatting(FeatureVisitor):
    def visit_text_file(self, text_file: Document):
        print("Analyze formatting for text file")

    def visit_spread_sheet(self, spread_sheet: Document):
        print("Analyze formatting for spread sheet")

    def visit_presentation_file(self, presentation_file: Document):
        print("Analyze formatting for presentation file")
