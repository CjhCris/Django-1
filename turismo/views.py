from django.shortcuts import render
from PIL import Image
import os

def index(request):
    # Obtener la ruta del directorio actual del proyecto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Ruta de la imagen original
    ruta_imagen_original = os.path.join(base_dir, 'turismo', 'static', 'turismo', 'imagen', 'images.jpeg')

    # Abre la imagen
    imagen_original = Image.open(ruta_imagen_original)

    # Redimensiona la imagen a un tamaño específico (por ejemplo, 1000x150 píxeles)
    nuevo_tamano = (2000, 800)
    imagen_redimensionada = imagen_original.resize(nuevo_tamano)

    # Ruta para guardar la imagen redimensionada
    ruta_imagen_redimensionada = os.path.join(base_dir, 'turismo', 'static', 'turismo', 'imagen', 'images_redimensionada.jpeg')

    # Guarda la imagen redimensionada
    imagen_redimensionada.save(ruta_imagen_redimensionada)

    print("Imagen redimensionada guardada en:", ruta_imagen_redimensionada)

    # Paso la ruta de la imagen redimensionada al contexto
    context = {'imagen_redimensionada_path': '/static/turismo/imagen/images_redimensionada.jpeg'}
    
    return render(request, 'turismo/index.html', context)
