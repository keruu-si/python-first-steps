import os 
import shutil

CATEGORIAS = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mov', '.mov', '.mkv', 'webm'],
    'Musica': ['.mp3', '.wav', '.aac', '.flac'],
    'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Codigo': ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css', '.json'],
    'Otros': []
}

def get_categorias(archivo)
    """Determina la categoria de una archivo segun su extension"""
    extension = os.path.