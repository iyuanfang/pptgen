from win32com.client import gencache
import os


def ppt_to_pdf(inputFileName, outputFileName, formatType=32):
    p = gencache.EnsureDispatch("PowerPoint.Application")
    ppt = p.Presentations.Open(inputFileName)
    ppt.ExportAsFixedFormat(outputFileName, 2, PrintRange=None)


if __name__ == "__main__":
    ppt_to_pdf("gen/运营/运营.pptx", "运营.pdf")
