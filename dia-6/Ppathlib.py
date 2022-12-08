from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/Ian/Documents/Ejercicios Python/Curso-Python-Udemy/Dia-6/Prueba.txt')

rutaWi = PureWindowsPath(carpeta)

# if not carpeta.exists():
#     print('No')
# else:
#     print('si')

print(rutaWi)
