from pdf2image import convert_from_path
import os, shutil
try:
    os.makedirs('./TIFFs')
except FileExistsError:
    # directory already exists
    pass

listaarquivos = os.listdir()
for cadapdf in listaarquivos:
    if cadapdf[-4:].lower() == '.pdf':
        try:
            pages = convert_from_path(cadapdf)
            img_file = cadapdf.replace(".pdf", "")

            count = 0
            for page in pages:
                count += 1
                tiff_file = img_file + "_" + str(count).zfill(3) + ".tif"
                page.save(tiff_file), 'TIFF'
                shutil.move(tiff_file, './TIFFs')
        except:
            pass
