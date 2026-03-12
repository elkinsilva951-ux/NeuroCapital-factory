import os
import requests
import random
from moviepy.editor import VideoFileClip, AudioFileClip

def ejecutar_produccion_elite():
    print("🔥 Iniciando Factoría NeuroCapital...")
    PEXELS_KEY = os.getenv('PEXELS_API_KEY')
    MAKE_URL = os.getenv('MAKE_WEBHOOK_URL')
    
    # 1. Búsqueda de Clips de Vídeo Reales (No imágenes)
    temas = ["tecnología futurista", "finanzas", "criptomonedas", "inteligencia artificial"]
    query = random.choice(temas)
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=10&orientation=portrait"
    headers = {"Authorization": PEXELS_KEY}
    
    response = requests.get(url, headers=headers).json()
    # Seleccionamos un vídeo al azar de los 10 mejores resultados para que cada vídeo sea diferente
    video_data = random.choice(response['videos'])
    video_link = video_data['video_files'][0]['link']
    
    print(f"🎬 Descargando clip profesional sobre: {query}")
    with open("clip_real.mp4", 'wb') as f:
        f.write(requests.get(video_link).content)

    # 2. Ensamblaje de 30 segundos (Calidad Profesional)
    video_final = VideoFileClip("clip_real.mp4").subclip(0, 30).resize(height=1920)
    video_final.write_videofile("neurocapital_pro.mp4", codec="libx264", audio=False, fps=24)

    # 3. Inyección al mercado vía Make.com
    print("🚀 Enviando vídeo dinámico a la red de distribución...")
    with open("neurocapital_pro.mp4", 'rb') as f:
        requests.post(MAKE_URL, files={'video': f}, data={'titulo': f'NeuroCapital - {query}'})

if _name_ == "_main_":
    ejecutar_produccion_elite()
