import PyPDF2 as pd

# Ask user how many files to merge
n = int(input("Enter number of PDF files to merge: "))

# Take file paths from user
pdffiles = []
for i in range(n):
    path = input(f"Enter path for PDF file {i+1}: ")
    pdffiles.append(path)

# Merge the files
merger = pd.PdfMerger()
for filename in pdffiles:
    pdfile = open(filename, 'rb')
    pdfreader = pd.PdfReader(pdfile)
    merger.append(pdfreader)
    pdfile.close()

# Output merged PDF
output = input("Enter output file name (e.g., merged.pdf): ")
merger.write(output)
merger.close()
print("")