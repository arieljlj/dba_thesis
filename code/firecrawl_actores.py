from firecrawl import FirecrawlApp
import json
from datetime import datetime
import os

# 1. Configura tu API Key como variable de entorno:
#    export FIRECRAWL_API_KEY="fc-tu-clave-aqui"
api_key = os.environ.get("FIRECRAWL_API_KEY")
if not api_key:
    raise EnvironmentError("La variable de entorno FIRECRAWL_API_KEY no está definida.")
app = FirecrawlApp(api_key=api_key)

# 2. Ejecutar el Agente Autónomo
print("Iniciando rastreo amplio de entrevistas y comunicados en Colombia...")
print("Esto puede tomar unos minutos dependiendo del volumen de datos. Por favor espera...")

resultado = app.extract(
    urls=[
        # Entidades Institucionales y Gobierno
        "https://www.innpulsacolombia.com/portfolio-category/noticias/",
        "https://www.mincit.gov.co/prensa/noticias/industria",
        "https://www.sena.edu.co/es-co/Noticias/Paginas/default.aspx",

        # Medios Económicos Nacionales (Secciones específicas)
        "https://www.portafolio.co/negocios/emprendimiento",
        "https://www.larepublica.co/empresas",
        "https://www.elcolombiano.com/negocios/emprendimiento",

        # Repositorios Académicos (Consultas pre-armadas sobre emprendimiento en Colombia)
        "https://search.scielo.org/?q=emprendimiento+politica+colombia",
        "https://www.redalyc.org/busquedaArticuloFiltros.oa?q=emprendimiento%20colombia"
    ],
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
    medio donde fue publicado, fecha, URL y fragmento exacto y relevante de la entrevista o comunicado.
    """
)

# 3. Guardar los resultados en la carpeta de datos crudos
ruta_destino = os.path.join("..", "data", "raw")
os.makedirs(ruta_destino, exist_ok=True)

fecha = datetime.now().strftime("%Y%m%d")
nombre_archivo = os.path.join(ruta_destino, f"entrevistas_actores_ampliado_{fecha}.json")

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "isoformat"):
            return obj.isoformat()
        return super().default(obj)

with open(nombre_archivo, "w", encoding="utf-8") as f:
    datos = resultado.model_dump() if hasattr(resultado, "model_dump") else vars(resultado)
    json.dump(datos, f, ensure_ascii=False, indent=2, cls=DatetimeEncoder)

print(f"✅ Corpus cualitativo guardado con éxito en: {nombre_archivo}")
