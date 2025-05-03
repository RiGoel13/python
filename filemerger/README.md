# PDF Merger

This Python script allows you to merge multiple PDF files into one, providing an easy way to combine documents.

## Features

- Merge multiple PDF files into a single file.
- Custom file paths for each PDF to be merged.
- Output the merged PDF with a custom name.




## Installation
### Install Dependencies


```bash
pip install PyPDF2
```

1. Save the script as `pdf_merger.py`.

## How to Run

```bash
python pdf_merger.py
```

### Example Usage

```bash
Enter number of PDF files to merge: 3
Enter path for PDF file 1: file1.pdf
Enter path for PDF file 2: file2.pdf
Enter path for PDF file 3: file3.pdf
Enter output file name (e.g., merged.pdf): merged_output.pdf
```

### Example Output

The script will merge the PDF files specified and save them as `merged_output.pdf`.

##  How It Works

1. The script prompts you for the number of PDF files to merge.
2. For each file, it asks for the file path.
3. It uses `PyPDF2` to merge all the PDF files.
4. The merged file is saved under the custom name you provide.
