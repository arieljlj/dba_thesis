from firecrawl import FirecrawlApp
import json
from datetime import datetime
import os

# 1. Configura tu API Key (Regístrate en firecrawl.dev para obtenerla gratis)
app = FirecrawlApp(api_key="REDACTED")

# 2. Ejecutar el Agente Autónomo
print("Iniciando rastreo de entrevistas a actores clave en Colombia...")
resultado = app.extract(
    urls=["*"], # El asterisco permite búsqueda autónoma en toda la web
    prompt="""
    Busca entrevistas, declaraciones y comunicados oficiales (2020–2025)
    de actores clave en política pública de emprendimiento en Colombia:
    
    ACTORES PRIORITARIOS:
    - Ministra/Ministro de MinCIT (Ministerio de Comercio, Industria y Turismo)
    - Gerente General de iNNpulsa Colombia
    - Director General del SENA
    - Directores de Unidades de Emprendimiento universitarias en Colombia
    - Líderes de Confecámaras y cámaras de comercio regionales
    - Investigadores académicos expertos en emprendimiento colombiano
    
    TEMAS DE INTERÉS:
    - Intención emprendedora y factores que la impulsan o frenan
    - Políticas públicas de fomento al emprendimiento (Ley 1014, Fondo Emprender, ALDEA)
    - Ecosistema emprendedor colombiano y contexto macroeconómico
    - Emprendimiento juvenil, femenino y en regiones
    
    Para cada resultado incluye: nombre del actor, cargo, institución,
    medio donde fue publicado, fecha, URL y fragmento exacto y relevante de la entrevista.
    """
)

# 3. Guardar los resultados en la carpeta de datos crudos
# Subimos un nivel desde 'code/' para llegar a 'data/raw/'
ruta_destino = os.path.join("..", "data", "raw")
os.makedirs(ruta_destino, exist_ok=True) # Crea la carpeta si no existe

fecha = datetime.now().strftime("%Y%m%d")
nombre_archivo = os.path.join(ruta_destino, f"entrevistas_actores_{fecha}.json")

with open(nombre_archivo, "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)

print(f"✅ Corpus cualitativo guardado con éxito en: {nombre_archivo}")