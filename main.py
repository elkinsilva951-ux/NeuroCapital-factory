import os

def produccion():
    print("--- FÁBRICA NEUROCAPITAL: STATUS OPERATIVO ---")
    key = os.getenv('PEXELS_API_KEY')
    if not key:
        print("ERROR: LLAVE NO DETECTADA")
        return
    print("SISTEMA CONECTADO. LISTO PARA ESCALAR.")

produccion()
