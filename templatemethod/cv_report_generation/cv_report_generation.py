from abc import ABC, abstractmethod
from generated_report import GeneratedReport

class CVReportGeneration(ABC):
    def generate_cv_report(self, cv_file_path: str):
        file = self.__read_file(cv_file_path)
        extracted_data = self._extract_data(file)
        analyzed_data = self.__analyze_data(extracted_data)
        return self.__generate_report_of(analyzed_data)

    @abstractmethod
    def _extract_data(self, file):
        pass

    def __read_file(self, file_path):
        print(f"reading file from: {file_path}")
        return None

    def __analyze_data(self, data):
        print("analyzing data...")
        return None

    def __generate_report_of(self, analyzed_data):
        print("generating report...")
        return GeneratedReport(True)