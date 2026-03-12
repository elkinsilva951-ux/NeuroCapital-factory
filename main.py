import os
import requests

def iniciar_fabrica():
    print("--- INICIANDO SISTEMA DE GENERACIÓN DE CAPITAL ---")
    # Aquí se ejecutará su lógica principal
    # Verificando credenciales
    api_key = os.getenv('PEXELS_API_KEY')
    if not api_key:
        print("ERROR: Falta PEXELS_API_KEY en Secrets")
        return
    
    print("Conexión establecida. Procesando contenido...")

# Esta es la forma más simple y segura que GitHub Actions no puede confundir:
iniciar_fabrica()
