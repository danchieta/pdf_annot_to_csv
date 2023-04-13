# pdf_annot_to_csv
This simply scrapes the text annotations from a PDF file into a CSV file. The
columns of the CSV are the contents of the annotation, the type of annotation
(text, free text or caret), and the pagenumber.

The script depends on the PyPDF2 package, but you can probably run it in
[Google Colab](https://colab.research.google.com) and download your CSV file
from there.
