# Data Processing Scripts

Scripts para limpieza, transformación y preparación de datos crudos.

## Scripts disponibles

- **clean_data.r**: Script principal de limpieza de datos
- **data_cleaning_initial.r**: Limpieza inicial y transformaciones básicas

## Requisitos

- R 3.6+
- Librerías R: tidyverse, dplyr, stringr

## Uso

```bash
Rscript processing/clean_data.r
Rscript processing/data_cleaning_initial.r
```

## Flujo

1. Lee datos crudos de `../data/raw/`
2. Aplica transformaciones y limpieza
3. Genera datos procesados en `../data/processed/`

## Datos generados

- `survey_data_2026.csv`: Encuesta limpia y procesada
- Otros archivos JSON procesados según corresponda
