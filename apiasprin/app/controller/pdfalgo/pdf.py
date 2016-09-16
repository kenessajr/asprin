from pyPdf import PdfFileReader
from wand.image import Image
from asprin import Asprin
import os
import time

class Pdfalgo:

    def __init__(self, pdffile, filename):
        self.pdffile = pdffile
        self.filename = filename

    def loadPdf(self):
        start_time = time.time()
        pdf = PdfFileReader(open(self.pdffile, 'rb'))
        page_number = pdf.getNumPages()
        filesize = os.path.getsize(self.pdffile)
        filepath = os.path.abspath(self.pdffile)

        sumPdf = 0.0
        sumTonner = 0.0
        cPdf = 0
        mPdf = 0
        yPdf = 0
        kPdf = 0

        tmp = os.path.abspath('app/controller/pdfalgo/pdf/temp/tmp.jpg')
        for page in range(0, page_number):
            imageFile = self.pdffile + "[" + str(page) + "]"
            with Image(filename = imageFile) as img:
                img.save(filename=tmp)

            # Asprin Class
            asprin = Asprin(tmp)

            sum_t, sum, cmyk = asprin.tonnerPrice()

            # PDF summation price
            sumPdf += sum
            sumTonner += sum_t
            c,m,y,k = cmyk

            # CMYK Summation Price
            cPdf += c
            mPdf += m
            yPdf += y
            kPdf += k

        data = {
            'pagenumber':page_number,
            'filesize': filesize,
            'filename':self.filename,
            'filepath': filepath,
            'sumtonner':sumTonner,
            'sumPDF':sumPdf,
            'cPDF':cPdf,
            'mPDF':mPdf,
            'yPDF':yPdf,
            'kPDF':kPdf,
            'time': (time.time() - start_time)
        }

        return data



