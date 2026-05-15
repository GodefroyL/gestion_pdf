from pdf2docx import Converter # type: ignore

def convertion_pdf_docx(fichier: str) -> None:
    """
    Fonction pour convertir des fichiers pdf en docx

    #### Paramètre d'entrée:
        fichier: fichier à convertir
    """
    fichier_docx = fichier.replace('.pdf', '.docx')
    cv = Converter(fichier)
    cv.convert(fichier_docx)
    cv.close()
    return None

if __name__=='__main__':
    pass
        