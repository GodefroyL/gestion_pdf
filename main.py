from tkinter import filedialog as fd

from pdf_docx import convertion_pdf_docx
from compression_pdf import compression_pdf, compression_pdf_

def main():
    oui = True
    while oui:
        print('Que voulez-vous faire ?\n1. Convertir un fichier PDF en DOCX (fichier word)\n2. Compresser un fichier PDF')
        choix = input('Entrez le numéro de votre choix : ')
        fichier = fd.askopenfilename(defaultextension='.pdf', filetypes=[('Fichiers PDF', '*.pdf')], title='Sélectionner un fichier PDF')
        try:
            match choix:
                case '1':
                    convertion_pdf_docx(fichier)
                case '2':
                    compression_pdf_(fichier)
            print('Traitement terminé. Votre fichier se trouve au même endroit que le fichier PDF d\'origine.')
            continuer = input('Voulez-vous traiter un autre fichier ? [oui/non]')
            if continuer != 'oui':
                oui = False
        except Exception as e:
            print(f'Erreur dans la conversion ou la compression de ce fichier. {str(e)}')
            continuer = input('Voulez-vous recommencer avec un autre fichier ? [oui/non]')
            if continuer != 'oui':
                oui = False
    print('Merci d\'avoir utilisé ce programme !')

if __name__ == '__main__':
    main()