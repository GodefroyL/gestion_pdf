import os
import pypdf

def compression_pdf(fichier):
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
        
        print(f'tail du fichier original : {os.path.getsize(fichier) / 1024:.2f} KB')
        print(f'tail du fichier compressé : {os.path.getsize(f"{fichier}_compressé.pdf") / 1024:.2f} KB')
    except Exception as e:
        raise Exception(f"Impossible de compresser le PDF : {str(e)}")
