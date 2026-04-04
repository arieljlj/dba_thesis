# Web Scraping Scripts

Scripts para recopilación de datos de fuentes en línea.

## Scripts disponibles

- **scrape_youtube_actors_apify.py**: Extrae datos de videos de actores de YouTube usando Apify
- **scrape_actors_firecrawl.py**: Extrae información de actores usando FireCrawl

## Requisitos

- Python 3.8+
- Librerías: requests, json
- APIs: Apify, FireCrawl

## Uso

```bash
python scraping/scrape_youtube_actors_apify.py
python scraping/scrape_actors_firecrawl.py
```

## Salida

Los datos obtenidos se guardan en `../data/raw/` en formato JSON.
