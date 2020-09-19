import glob
import time
import os
try:
    import PyPDF2
except Exception as e:
    inp = input("PyPDF2 module not found!!Do you want to install it? [y/n]: ")
    if(inp == 'y' or inp == 'Y'):
        os.system('pip install PyPDF2')
        print("Module Insatlled!!")
        time.sleep(0.5)
    else:
        print("Goodbye...")
        time.sleep(1)
        exit()


def splitPDFS(pdfFile, Filename):
    Filename = "../OUTPUT/{}_Page_No_".format(Filename)
    pdfFileObj = PyPDF2.PdfFileReader(open(pdfFile, "rb"))
    for i in range(pdfFileObj.numPages):
        newSplitPage = PyPDF2.PdfFileWriter()
        newSplitPage.addPage(pdfFileObj.getPage(i))
        pdfOutPutFile = open(Filename+str(i+1)+".pdf", "wb")
        newSplitPage.write(pdfOutPutFile)
        pdfOutPutFile.close()
    return"DONE!!!"


if __name__ == "__main__":
    PdfArray = glob.glob("../DROP/*pdf")
    print(len(PdfArray), "Files found")
    PdfDict = {chr(a+97): b for a, b in enumerate(PdfArray)}
    for i, j in PdfDict.items():
        print(i, ":", j.split("\\")[1])
    inp = input("Select the file you want to split:")
    while(PdfDict.get(inp) == None):
        inp = input("Please select a valid file you want to split:")
    print(splitPDFS(PdfDict[inp], PdfDict[inp].split(
        "\\")[1]), "\nFiles are in \'OUTPUT\' folder")
    time.sleep(1)
    print("Goodbye..")
    time.sleep(2)
