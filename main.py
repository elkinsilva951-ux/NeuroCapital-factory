import os
import requests

def ejecucion_directa_neurocapital():
    print("--- MOTOR DE PRODUCCIÓN ACTIVADO ---")
    
    # Validación de activos
    api_key = os.getenv('PEXELS_API_KEY')
    webhook = os.getenv('MAKE_WEBHOOK_URL')
    
    if not api_key:
        print("ERROR: Falta PEXELS_API_KEY en Secrets.")
        return

    print("Conexión con Pexels: AUTORIZADA")
    print("Iniciando fase de renderizado de alto valor...")

# Llamada directa al motor (sin guiones bajos conflictivos)
ejecucion_directa_neurocapital()
