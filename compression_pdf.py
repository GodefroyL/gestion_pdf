import fitz
import os
import pypdf

def compression_pdf_(fichier):
    try:
        reader = pypdf.PdfReader(fichier)
        writer = pypdf.PdfWriter()
        writer.compress_identical_objects()
        for page in reader.pages:
            writer.add_page(page)
        for page in writer.pages:
            for img in page.images:
                try:img.replace(img.image, quality=70)
                except Exception: continue
            page.compress_content_streams()
        with open(f'{fichier}_compressé.pdf', 'wb') as fichier_sortie:
            writer.write(fichier_sortie)
    except Exception as e:
        raise Exception(f"Impossible de compresser le PDF : {str(e)}")


def compression_pdf(fichier: str, zoom_x: float=0.5, zoom_y: float=0.5):
    """
    Compresser un fichier PDF en réduisant son contenu
    :param fichier: Chemin du fichier PDF d'entrée
    :param zoom_x: Facteur d'échelle horizontal (0-1)
    :param zoom_y: Facteur d'échelle vertical (0-1)
    """
    try:
    # Taille du fichier avant compression
        taille_originale = os.path.getsize(fichier)
    # Ouverture du PDF
        document = fitz.open(fichier)
        
    # Création du nouveau PDF
        nouveau_document = fitz.open()
        
    # Itération page par page
        for num_page in range(len(document)):
            page = document.load_page(num_page)
        # Créer une matrice de transformation pour la mise à l'échelle
            matrice = fitz.Matrix(zoom_x, zoom_y)
            # Obtenir le pixmap (image redimensionnée) de la page
            pix = page.get_pixmap(matrix=matrice, alpha=False, dpi=72)
            # Convertir en JPEG avec les paramètres de qualité
            octets_img = pix.pil_tobytes(format="JPEG", quality=70)
            # Créer une nouvelle page dans le document de sortie
            nouvelle_page = nouveau_document.new_page(width=pix.width, height=pix.height)
            # Insérer l'image JPEG au lieu du pixmap brut
            nouvelle_page.insert_image(nouvelle_page.rect, stream=octets_img)
        
        # Enregistrer le PDF compressé
        nouveau_document.save(f'{fichier}_compressé.pdf')
        nouveau_document.close()
        document.close()
        
        print(f"PDF compressé enregistré dans {fichier}_compressé.pdf")
        print(f"Taille originale : {taille_originale/1024:.2f} Ko")
        print(f"Taille compressée : {os.path.getsize(f'{fichier}_compressé.pdf')/1024:.2f} Ko")
        
    except Exception as e:
        raise Exception(f"Impossible de compresser le PDF : {str(e)}")