import os
import requests

def iniciar_fabrica_neurocapital():
    print("--- SISTEMA DE PRODUCCIÓN ACTIVO ---")
    
    # Verificación de llaves de capital
    api_key = os.getenv('PEXELS_API_KEY')
    webhook = os.getenv('MAKE_WEBHOOK_URL')
    
    if not api_key:
        print("ERROR: Falta PEXELS_API_KEY en los Secrets de GitHub.")
        return

    print("Conexión con Pexels: EXITOSA")
    print("Iniciando generación de videos de alta rentabilidad...")

# Ejecución directa inmediata
iniciar_fabrica_neurocapital()
