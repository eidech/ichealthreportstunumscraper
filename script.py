######################################################
### IC Health Screening Missing Report Scraper #######
### Written by Christopher Eide, Technology ##########
### Integration Specialist, Trumbull Public Schools ##
### Initial Code Deposit: 30 Apr, 2024 ###############
### Direct inquiries to ceide@trumbullps.org #########
######################################################

from PyPDF2 import PdfReader
import re, csv

def main():
    # holder for list of student numbers
    studentnumbers = []

    # load up the pdf assumed to be "report.pdf" in the same directory
    # as the script
    pdf = PdfReader(open('report.pdf', 'rb'))

    # go through page by page and extract student numbers; add them to list
    for page in pdf.pages:
        pagetext = page.extract_text()
        pagelines = pagetext.splitlines()
        for line in pagelines:
            if re.search("[0-9]{8}|[0-9]{7}", line):
                studentnumber = re.search("[0-9]{8}|[0-9]{7}", line).group()
                if studentnumber:
                    studentnumbers.append(studentnumber)
    
    # write to csv file
    with open ('output.csv', mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # write the header
        writer.writerow(['student_studentNumber'])

        # write the student numbers
        for studentnumber in studentnumbers:
            writer.writerow([studentnumber])
            


if __name__ == "__main__":
    main()