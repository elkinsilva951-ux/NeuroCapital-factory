import os
import requests

def fabrica_neurocapital_activa():
    print("--- FÁBRICA NEUROCAPITAL: PRODUCCIÓN INICIADA ---")
    
    # 1. Validación de Conexión con Pexels
    api_key = os.getenv('PEXELS_API_KEY')
    if not api_key:
        print("ERROR: Inyecte su PEXELS_API_KEY en los Secrets de GitHub.")
        return

    # 2. Comando de Búsqueda de Contenido
    # El sistema buscará metraje de 'lujo' y 'motivación'
    query = "luxury motivation"
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=1"
    headers = {"Authorization": api_key}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(f"ÉXITO: Se ha localizado material para el Video #1.")
        print(f"URL de Producción: {data['videos'][0]['url']}")
    else:
        print(f"FALLO DE CONEXIÓN: Código {response.status_code}")

# Ejecución Directa Segura
fabrica_neurocapital_activa()
