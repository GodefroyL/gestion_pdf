from pdf2docx import Converter

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
    from tkinter import filedialog as fd
    oui = True
    while oui:
        fichier = fd.askopenfilename(defaultextension='.pdf', filetypes=[('Fichiers PDF', '*.pdf')], title='Sélectionner un fichier PDF')
        try:
            convertion_pdf_docx(fichier)
            print('Conversion terminée. Votre fichier se trouve au même endroit que le fichier PDF d\'origine.')
            continuer = input('Voulez-vous convertir un autre fichier ? [oui/non]')
            if continuer != 'oui':
                oui = False
        except Exception as e:
            print('Erreur dans la conversion de ce fichier. Le fichier peut être corrompu ou protégé, ou bien le format n\'est pas supporté....')
            continuer = input('Voulez-vous recommencer avec un autre fichier ? [oui/non]')
            if continuer != 'oui':
                oui = False
        