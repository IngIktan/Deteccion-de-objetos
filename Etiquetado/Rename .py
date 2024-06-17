import os

def rename_files_in_directory(directory_path, prefix):
    # Verificar si la ruta del directorio existe
    if not os.path.isdir(directory_path):
        print(f"La ruta {directory_path} no existe o no es un directorio.")
        return
    
    # Listar todos los archivos en el directorio
    files = os.listdir(directory_path)
    
    # Filtrar solo archivos (excluir directorios)
    files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
    
    # Ordenar los archivos para que se renombren de manera consistente
    files.sort()

    # Inicializar el contador
    counter = 1
    
    # Renombrar cada archivo
    for filename in files:
        # Generar el nuevo nombre de archivo
        new_name = f"{prefix}{counter}{os.path.splitext(filename)[1]}"
        
        # Obtener la ruta completa del archivo antiguo y nuevo
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_name)
        
        # Renombrar el archivo
        os.rename(old_file_path, new_file_path)
        
        # Incrementar el contador
        counter += 1
    
    print(f"Renombrados {counter-1} archivos en {directory_path}")

# Ejemplo de uso
directory_path = r'D:\Daniel Alejandro Flores Sepulveda\Ingenieria Escuela\Sexto\70- Vision Artificial\30- Tercero\Imagenes\Pet alreves volteado'
prefix = 'Plastico0 '
rename_files_in_directory(directory_path, prefix)
