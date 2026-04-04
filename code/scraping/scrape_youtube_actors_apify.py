"""
apify_youtube_actores.py
Captura videos de YouTube sobre entrevistas a actores clave en
política de emprendimiento en Colombia usando Apify, y extrae
campos estructurados con Claude (Anthropic).

Campos extraídos por video:
  - nombre_actor       : nombre de la persona entrevistada / que habla
  - cargo_actor        : posición o cargo (ej. Ministro de Comercio)
  - institucion        : organización a la que pertenece
  - fecha_publicacion  : fecha del video en YouTube
  - url_video          : enlace directo al video
  - fragmentos_clave   : lista de citas textuales relevantes para la investigación
  - titulo             : título del video
  - canal              : canal de YouTube
  - descripcion        : descripción del video
  - subtitulos         : texto completo de subtítulos (si están disponibles)

Requisitos:
    pip install apify-client anthropic

Variables de entorno:
    APIFY_API_TOKEN   — token de Apify (console.apify.com/account/integrations)
    ANTHROPIC_API_KEY — (opcional) si no está definida, la extracción se hace
                        con heurísticas simples sobre título y descripción

Uso:
    export APIFY_API_TOKEN="apify_api_xxxxx"
    export ANTHROPIC_API_KEY="sk-ant-xxxxx"   # opcional pero recomendado
    python3 apify_youtube_actores.py
"""

import json
import os
import re
import time
from datetime import datetime
from typing import Optional

from apify_client import ApifyClient

# ── Configuración ─────────────────────────────────────────────────────────────

APIFY_TOKEN = os.environ.get("APIFY_API_TOKEN")
if not APIFY_TOKEN:
    raise EnvironmentError(
        "APIFY_API_TOKEN no está definida.\n"
        "Ejecuta: export APIFY_API_TOKEN='apify_api_xxxxx'"
    )

ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY")

ACTOR_ID = "streamers/youtube-scraper"

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "raw")

# ── Términos de búsqueda ───────────────────────────────────────────────────────

SEARCH_QUERIES = [
    # Institucionales
    "entrevista MinCIT emprendimiento Colombia",
    "Ministerio de Comercio emprendimiento política pública Colombia",
    "iNNpulsa Colombia entrevista director",
    "SENA emprendimiento Fondo Emprender entrevista director",
    "Confecámaras emprendimiento Colombia entrevista",
    # Programas y leyes
    "Ley 1014 fomento emprendimiento Colombia entrevista",
    "programa ALDEA emprendimiento Colombia iNNpulsa",
    "ecosistema emprendedor Colombia política pública entrevista",
    # Académicos e investigadores
    "investigador emprendimiento Colombia intención emprendedora entrevista",
    "emprendimiento juvenil Colombia política pública entrevista",
    "emprendimiento femenino Colombia política entrevista",
    # Regiones
    "emprendimiento regional Colombia cámara de comercio entrevista",
    # Contexto
    "emprendimiento Colombia 2022 2023 2024 entrevista actores",
]

MAX_RESULTS_PER_QUERY = 15

# ── Extracción con Claude ──────────────────────────────────────────────────────

EXTRACTION_PROMPT = """Analiza el siguiente video de YouTube sobre emprendimiento en Colombia.
Extrae ÚNICAMENTE la información que esté explícitamente presente en el texto.
Si algún campo no está disponible, escribe null.

TÍTULO: {title}
CANAL: {channel}
DESCRIPCIÓN: {description}
SUBTÍTULOS (fragmento): {subtitles}

Responde SOLO con JSON válido con esta estructura exacta:
{{
  "nombre_actor": "Nombre completo de la persona entrevistada o que habla",
  "cargo_actor": "Cargo o posición (ej. Ministro de Comercio, Director SENA)",
  "institucion": "Organización o entidad (ej. MinCIT, iNNpulsa, SENA, Universidad)",
  "temas_abordados": ["tema1", "tema2"],
  "fragmentos_clave": [
    "Cita textual o paráfrasis relevante para política de emprendimiento 1",
    "Cita textual o paráfrasis relevante 2",
    "Cita textual o paráfrasis relevante 3"
  ],
  "relevancia_investigacion": "alta|media|baja",
  "justificacion_relevancia": "Una oración explicando por qué es relevante para la investigación"
}}"""


def extract_with_claude(title: str, channel: str, description: str, subtitles: str) -> dict:
    """Usa Claude para extraer campos estructurados del video."""
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

        sub_fragment = (subtitles or "")[:4000]  # máx tokens razonables
        desc_fragment = (description or "")[:1500]

        prompt = EXTRACTION_PROMPT.format(
            title=title or "",
            channel=channel or "",
            description=desc_fragment,
            subtitles=sub_fragment,
        )

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",  # rápido y económico
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )

        raw = message.content[0].text.strip()
        # Limpiar posible markdown ```json ... ```
        raw = re.sub(r"^```json\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        return json.loads(raw)

    except Exception as exc:
        print(f"      ⚠ Claude extraction error: {exc}")
        return _heuristic_extraction(title, channel, description)


def _heuristic_extraction(title: str, channel: str, description: str) -> dict:
    """Extracción basada en palabras clave cuando Claude no está disponible."""
    institutions = {
        "innpulsa": "iNNpulsa Colombia",
        "mincit": "Ministerio de Comercio, Industria y Turismo",
        "sena": "SENA",
        "confecámaras": "Confecámaras",
        "cámara de comercio": "Cámara de Comercio",
        "universidad": "Universidad",
    }
    text_lower = f"{title} {description}".lower()
    found_inst = next(
        (v for k, v in institutions.items() if k in text_lower), None
    )

    return {
        "nombre_actor": None,
        "cargo_actor": None,
        "institucion": found_inst,
        "temas_abordados": [],
        "fragmentos_clave": [],
        "relevancia_investigacion": "media",
        "justificacion_relevancia": "Extracción heurística (Claude no disponible)",
    }


# ── Subtítulos ─────────────────────────────────────────────────────────────────

def get_subtitles_text(video: dict) -> str:
    """Intenta obtener texto de subtítulos desde el objeto devuelto por Apify."""
    # El actor puede devolver subtítulos en distintas claves según versión
    for key in ("subtitles", "captions", "transcript", "subtitlesText"):
        value = video.get(key)
        if not value:
            continue
        if isinstance(value, str):
            return value
        if isinstance(value, list):
            # lista de segmentos {"text": "...", "start": ...}
            return " ".join(
                seg.get("text", "") for seg in value if isinstance(seg, dict)
            )
    return ""


# ── YouTube Scraper ────────────────────────────────────────────────────────────

def run_youtube_scraper(client: ApifyClient, query: str) -> list[dict]:
    print(f"  Buscando: «{query}» …")
    try:
        run = client.actor(ACTOR_ID).call(
            run_input={
                "searchQueries": [query],
                "maxResults": MAX_RESULTS_PER_QUERY,
                "maxResultsShorts": 0,
                "maxResultStreams": 0,
                "downloadSubtitles": True,
                "subtitlesLanguage": "es",
                "preferAutoGeneratedSubtitles": True,
                "subtitlesFormat": "srt",
                "sortingOrder": "relevance",
            }
        )
        items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
        print(f"    → {len(items)} videos")
        return items
    except Exception as exc:
        print(f"    ⚠ Error en scraper: {exc}")
        return []


def deduplicate(videos: list[dict]) -> list[dict]:
    seen: set[str] = set()
    unique: list[dict] = []
    for v in videos:
        vid = v.get("id") or v.get("videoId") or v.get("url", "")
        if vid and vid not in seen:
            seen.add(vid)
            unique.append(v)
    return unique


# ── Construcción del registro final ───────────────────────────────────────────

def build_record(video: dict, query: str, extracted: dict) -> dict:
    """Combina metadatos de YouTube con la extracción estructurada."""
    url = (
        video.get("url")
        or video.get("videoUrl")
        or f"https://www.youtube.com/watch?v={video.get('id', '')}"
    )
    pub_date = (
        video.get("date")
        or video.get("publishedAt")
        or video.get("uploadDate")
    )

    return {
        # ── Campos del investigador ──
        "nombre_actor": extracted.get("nombre_actor"),
        "cargo_actor": extracted.get("cargo_actor"),
        "institucion": extracted.get("institucion"),
        "fecha_publicacion": pub_date,
        "url_video": url,
        "fragmentos_clave": extracted.get("fragmentos_clave", []),
        "temas_abordados": extracted.get("temas_abordados", []),
        "relevancia_investigacion": extracted.get("relevancia_investigacion"),
        "justificacion_relevancia": extracted.get("justificacion_relevancia"),
        # ── Metadatos del video ──
        "titulo": video.get("title"),
        "canal": video.get("channelName") or video.get("channel"),
        "descripcion": video.get("description"),
        "duracion_seg": video.get("duration"),
        "vistas": video.get("viewCount"),
        "likes": video.get("likeCount"),
        "subtitulos_disponibles": bool(get_subtitles_text(video)),
        # ── Trazabilidad ──
        "_query_origen": query,
        "_capturado_en": datetime.utcnow().isoformat() + "Z",
        "_video_id": video.get("id") or video.get("videoId"),
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    use_claude = bool(ANTHROPIC_KEY)

    print("=" * 65)
    print("  Captura YouTube — Actores en Política de Emprendimiento CO")
    print(f"  Actor Apify : {ACTOR_ID}")
    print(f"  Extracción  : {'Claude (Anthropic)' if use_claude else 'Heurística (sin ANTHROPIC_API_KEY)'}")
    print(f"  Términos    : {len(SEARCH_QUERIES)}")
    print("=" * 65)

    apify = ApifyClient(APIFY_TOKEN)
    all_raw: list[tuple[dict, str]] = []  # (video_raw, query)

    for query in SEARCH_QUERIES:
        items = run_youtube_scraper(apify, query)
        all_raw.extend((v, query) for v in items)
        time.sleep(1)  # pausa cortés entre runs

    unique_raw = deduplicate([v for v, _ in all_raw])
    print(f"\nVideos únicos: {len(unique_raw)} (de {len(all_raw)} capturas totales)")

    # Reconstruir mapa query por video_id para trazabilidad
    query_map: dict[str, str] = {}
    for v, q in all_raw:
        vid = v.get("id") or v.get("videoId") or v.get("url", "")
        if vid not in query_map:
            query_map[vid] = q

    print("\nExtrayendo campos estructurados…")
    records: list[dict] = []

    for i, video in enumerate(unique_raw, 1):
        vid = video.get("id") or video.get("videoId") or video.get("url", "")
        origin_query = query_map.get(vid, "")
        subtitles = get_subtitles_text(video)

        print(f"  [{i}/{len(unique_raw)}] {video.get('title', '')[:70]}")

        if use_claude:
            extracted = extract_with_claude(
                title=video.get("title", ""),
                channel=video.get("channelName") or video.get("channel", ""),
                description=video.get("description", ""),
                subtitles=subtitles,
            )
        else:
            extracted = _heuristic_extraction(
                title=video.get("title", ""),
                channel=video.get("channelName") or video.get("channel", ""),
                description=video.get("description", ""),
            )

        records.append(build_record(video, origin_query, extracted))
        time.sleep(0.3)  # evitar rate-limit de Claude

    # ── Guardar ──────────────────────────────────────────────────────────────
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fecha = datetime.now().strftime("%Y%m%d_%H%M")
    output_path = os.path.join(
        OUTPUT_DIR, f"youtube_actores_emprendimiento_{fecha}.json"
    )

    output = {
        "metadata": {
            "fuente": "Apify / YouTube Scraper",
            "actor_apify": ACTOR_ID,
            "extraccion_nlp": "Claude claude-haiku-4-5" if use_claude else "heuristica",
            "capturado_en": datetime.utcnow().isoformat() + "Z",
            "total_videos": len(records),
            "terminos_busqueda": SEARCH_QUERIES,
        },
        "videos": records,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Resumen
    con_actor = sum(1 for r in records if r.get("nombre_actor"))
    alta_relevancia = sum(1 for r in records if r.get("relevancia_investigacion") == "alta")
    print(f"\n{'=' * 65}")
    print(f"✅ Guardado en: {output_path}")
    print(f"   Total videos   : {len(records)}")
    print(f"   Con actor ID   : {con_actor}")
    print(f"   Alta relevancia: {alta_relevancia}")
    print(f"{'=' * 65}")


if __name__ == "__main__":
    main()
