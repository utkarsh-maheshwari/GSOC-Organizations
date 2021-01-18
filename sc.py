import PyPDF2
import numpy as np
import pandas as pd

# pdffile = open("GSOC_Organizations.pdf")
read_pdf = PyPDF2.PdfFileReader("GSOC_Organizations.pdf")
inf = read_pdf.getDocumentInfo()
pages = read_pdf.getNumPages()
outlines = read_pdf.getOutlines()
a = []
b = []
for i in range(len(outlines)):
    a.append(outlines[i]['/Title'])

a = np.array(a)
# b = np.array(b)
for i in range(len(a)):

    if a[i] == 'afl++':
        save = i
        break
    if a[i][-2]==' ':
        b.append(a[i][-1])
    else:
        b.append(a[i][-2]+a[i][-1])
    # print(a[i])
    b[i] = int(b[i])
    a[i] = a[i][0:-2]

a = a[:save]

df = {'Org': a, '2020 Selections': b}
df = pd.DataFrame(df)
# df.insert(0,'Org',a)
print(df.describe())
with pd.ExcelWriter('GSOC Organizations.xlsx') as writer:
    df.to_excel(writer)

# print(a,b)

