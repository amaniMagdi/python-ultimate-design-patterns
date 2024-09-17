from pdf_cv_report_generation import PdfCVReportGeneration
# Main function to run the app
def main():
    cv_file_path = "path/to/cv.pdf"
    
    # Create an instance of PdfCVReportGeneration
    report_generator = PdfCVReportGeneration()
    
    # Generate the CV report
    report = report_generator.generate_cv_report(cv_file_path)
    
    # Output the report result
    if report.is_passed():
        print("The report has passed.")
    else:
        print("The report has not passed.")

# Ensure the main function runs when this script is executed
if __name__ == "__main__":
    main()