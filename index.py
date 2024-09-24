import PyPDF2
import os

merger = PyPDF2.PdfMerger()

listar_arquivos = os.listdir("arquivos")
listar_arquivos.sort()
print(listar_arquivos)

for arquivo in listar_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

merger.write("PDF Final.pdf")
