# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:46:25 2023

@author: gmmatos
"""

import tabula
from tabula import read_pdf
from tabulate import tabulate
import io
import PyPDF2
from PIL import Image
import numpy as np
import PyPDF2
import re
import pandas as pd

# Open the PDF file
pdf_file = open('DGS_PNDCCV_V11.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pgno = pdf_reader.getNumPages()

lista=[]
# Loop through each page of the PDF
for page_num in range(pgno):
    page = pdf_reader.getPage(page_num)
    page_text = page.extractText()
    # Check if the page contains the text "Table of Contents"
    if re.search('TABELA',page_text):
        
        # Get the table on the same page as the text
        tables = tabula.read_pdf('DGS_PNDCCV_V11.pdf', pages=page_num+1, stream=True, multiple_tables=True)  # Print the table
        for table in tables:
            lista.append(table)
print('-------------------------------------------------------------')
df = pd.concat(lista)
df.to_excel(r'C:\Users\gonca\Test.xlsx')

# Close the PDF file
pdf_file.close()


