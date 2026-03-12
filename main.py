import os
import requests

def ejecutar_produccion_real():
    print("--- INICIANDO RENDERIZADO DE VIDEOS NEUROCAPITAL ---")
    
    # 1. Validación de Capital (API KEY)
    api_key = os.getenv('PEXELS_API_KEY')
    if not api_key:
        print("ERROR: Inyecte PEXELS_API_KEY en Secrets")
        return

    # 2. Búsqueda de metraje de alto valor
    print("Conectando con servidores de Pexels para obtener clips de lujo...")
    headers = {"Authorization": api_key}
    params = {"query": "luxury cars", "per_page": 1}
    
    res = requests.get("https://api.pexels.com/videos/search", headers=headers, params=params)
    
    if res.status_code == 200:
        video_url = res.json()['videos'][0]['url']
        print(f"ÉXITO: Material localizado. Iniciando descarga: {video_url}")
    else:
        print(f"ERROR DE CONEXIÓN: {res.status_code}")

# Inicio directo
ejecutar_produccion_real()
