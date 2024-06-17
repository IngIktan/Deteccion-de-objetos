import os
import cv2
import imgaug.augmenters as iaa
import numpy as np

# Directorio de imágenes de entrada y salida
input_dir = r'D:\Daniel Alejandro Flores Sepulveda\Ingenieria Escuela\Sexto\70- Vision Artificial\30- Tercero\Imagenes\Pet General'
output_dir = r'D:\Daniel Alejandro Flores Sepulveda\Ingenieria Escuela\Sexto\70- Vision Artificial\30- Tercero\Imagenes\Pet alreves volteado'

# Crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Definir las transformaciones de aumento
augmenters = iaa.Sequential([
    iaa.Fliplr(0.5),  # Voltear horizontalmente el 50% de las imágenes
    iaa.Affine(
        rotate=(-20, 20),  # Rotar entre -20 y 20 grados
        translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},  # Traducir en un 20%
        scale=(0.8, 1.2)  # Escalar entre el 80% y el 120%
    ),
    iaa.Multiply((0.8, 1.2)),  # Cambiar el brillo entre el 80% y el 120%
    iaa.AdditiveGaussianNoise(scale=(0, 0.05*255))  # Añadir ruido gaussiano
])

# Función para aumentar las imágenes
def augment_images(input_dir, output_dir, augmenters, num_augmented_images=5):
    file_counter = 1
    
    for filename in sorted(os.listdir(input_dir)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            img_path = os.path.join(input_dir, filename)
            # Leer la imagen, incluso las imágenes webp
            image = cv2.imread(img_path)
            if image is None:
                print(f"No se pudo leer la imagen: {filename}")
                continue
            
            # Guardar la imagen original con el nuevo nombre
            original_filename = f"{prefix}{file_counter}.jpg"
            original_path = os.path.join(output_dir, original_filename)
            cv2.imwrite(original_path, image)
            print(f"Guardado original: {original_path}")
            file_counter += 1

            # Guardar las imágenes aumentadas
            for i in range(num_augmented_images):
                augmented_image = augmenters(image=image)
                output_filename = f"{prefix}{file_counter}.jpg"
                output_path = os.path.join(output_dir, output_filename)
                cv2.imwrite(output_path, augmented_image)
                file_counter += 1
            print(f"Imagen {filename} aumentada {num_augmented_images} veces.")

# Prefijo para los nuevos nombres de archivo
prefix = 'PH'

# Aumentar las imágenes
augment_images(input_dir, output_dir, augmenters)
