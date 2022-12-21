import zipfile
import shutil

# mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

# mi_zip.write('textob.txt')
# mi_zip.write('txtoa.txt')

# mi_zip.close()

# zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')

# zip_abierto.extractall()

# carpeta_origen = 'C:\\Users\\Ian\\Documents\\Ejercicios Python\\Curso-Python-Udemy\\Dia-9'
# archivo_destino = 'Todo_comprimido'
# shutil.make_archive(archivo_destino,'zip',carpeta_origen)

shutil.unpack_archive('Proyecto+Dia+9.zip','Extraccion-Proyecto','zip')