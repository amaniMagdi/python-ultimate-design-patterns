from text_file import TextFile
from presentation_file import PresentationFile
from spread_sheet import SpreadSheet
from counting_words import CountingWords
from analyze_formatting import AnalyzeFormatting

def main():
    documnets_list= [TextFile(), 
                    PresentationFile(),
                    SpreadSheet()]

    for document in documnets_list:
        document.accept(CountingWords())
        document.accept(AnalyzeFormatting())

if __name__ == "__main__":
    main()
