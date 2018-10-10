import PyPDF2 
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure


import sys
# pdfFileObj = open('gpcan2017_Men_SP_Scores.pdf', 'rb', encoding= 'utf-8')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# # print(pdfReader.numPages) 
# pageObj = pdfReader.getPage(0) 
# obj = pageObj.getObject()
# pdfFileObj.close() 


def parse_layout(layout):
    """Function to recursively parse the layout tree."""
    for lt_obj in layout:
        print(lt_obj.__class__.__name__)
        print(lt_obj.bbox)
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            print(lt_obj.get_text())
        elif isinstance(lt_obj, LTFigure):
            parse_layout(lt_obj)  # Recursive


sys.stdout = open("gpcan_data", "w")
fp = open('gpcan2017_Men_SP_Scores.pdf', 'rb','utf-8')
for i in range(2):
    parser = PDFParser(fp)
    doc = PDFDocument(parser)

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
        layout = device.get_result()
        parse_layout(layout)
        break
    fp.close()
    sys.stdout = open("olymp_data", "w", 'utf-8')
    fp = open('OWG2018_LadiesSingleSkating_SP_Scores.pdf', 'rb', 'utf-8')

a = 0