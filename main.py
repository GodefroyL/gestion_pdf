from tkinter import filedialog as fd

from pdf_docx import convertion_pdf_docx
from compression_pdf import compression_pdf, compression_pdf

def main():
    oui = True
    while oui:
        print('Que voulez-vous faire ?\n1. Convertir un fichier PDF en DOCX (fichier word)\n2. Compresser un fichier PDF\n3. Quitter le programme')
        choix = input('Entrez le numéro de votre choix : ')
        try:
            match choix:
                case '1':
                    fichier = fd.askopenfilename(defaultextension='.pdf', filetypes=[('Fichiers PDF', '*.pdf')], title='Sélectionner un fichier PDF')
                    convertion_pdf_docx(fichier)
                case '2':
                    fichier = fd.askopenfilename(defaultextension='.pdf', filetypes=[('Fichiers PDF', '*.pdf')], title='Sélectionner un fichier PDF')
                    compression_pdf(fichier)
                case '3':
                    oui = False
                    continue
                case _:
                    print('Choix invalide. Veuillez entrer un numéro valide.')
                    continue
            print('Traitement terminé. Votre fichier se trouve au même endroit que le fichier PDF d\'origine.')
        except Exception as e:
            print(f'Erreur dans la conversion ou la compression de ce fichier. {str(e)}')
            continuer = input('Voulez-vous recommencer avec un autre fichier ? [oui/non]')
            if continuer != 'oui':
                oui = False
    print('Merci d\'avoir utilisé ce programme !')

if __name__ == '__main__':
    main()