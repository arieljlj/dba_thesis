# Análisis y Mejoras de Estructura del Repositorio - Tesis DBA

## 📋 Estado Actual

Tu repositorio tiene una **estructura base sólida** pero con **problemas de duplicación y organización**:

```
dba_thesis/
├── code/                    (Scripts de análisis y scraping)
├── data/                    (Datos raw)
├── docs/                    (Contenido de tesis)
└── README.md
```

---

## 🚨 Problemas Identificados

### 1. **DUPLICACIÓN CRÍTICA en `/docs`**
- **Carpetas numeradas**: `00_portada...`, `01_introduccion...`, `02_cap1...`, etc.
- **Carpeta `capitulos/`**: Contiene carpetas duplicadas (`cap1...`, `cap2...`, etc.)
- **Resultado**: Confusión sobre cuál es la estructura oficial

### 2. **Archivos en `code/` sin organización**
- Scripts sueltos: `code 1.R`, `analisis_encuesta_2026.ipynb`, `analisis_macroeconomico.py`
- Scripts de scraping: `apify_youtube_actores.py`, `firecrawl_actores.py`
- Scripts de limpieza: `limpiar_datos.R`
- **Falta**: Carpetas temáticas (scraping, processing, analysis)

### 3. **Organización de datos incompleta**
- Todo en `data/raw/` o raíz de data
- **Falta**: Carpetas para datos procesados, outputs, intermediate

### 4. **Archivos sueltos en docs**
- `index.html`, `styles.css`, `estructura_tesis_completa.md`
- No tienen relación clara con capítulos

### 5. **Nómina de archivos inconsistente**
- `code 1.R` (con espacio)
- `datos_encuesta_2026.csv` vs `youtube_actores_emprendimiento_claude_20260401.json`
- Falta estandarización en nombres

### 6. **Archivos de sistema en versionado**
- `.DS_Store` (macOS)
- `.claude/` con settings
- Deberían estar en `.gitignore`

---

## ✅ Estructura Recomendada

```
dba_thesis/
│
├── 📁 docs/                          # Contenido de tesis
│   ├── 00_portada_resumen_abstract/
│   ├── 01_introduccion/
│   ├── 02_cap1_proyeccion_investigacion/
│   ├── 03_cap2_fundamentos_teoricos/
│   ├── 04_cap3_metodologia_resultados/
│   ├── 05_cap4_propuesta_transformacion/
│   ├── 06_conclusiones/
│   ├── 07_recomendaciones/
│   ├── 08_bibliografia/
│   ├── 09_anexos/
│   ├── assets/                       # Recursos: CSS, HTML, imágenes
│   │   ├── styles.css
│   │   ├── index.html
│   │   └── images/
│   └── estructura_tesis_completa.md
│
├── 📁 code/
│   ├── 📁 scraping/                 # Scripts de recopilación de datos
│   │   ├── apify_youtube_actores.py
│   │   ├── firecrawl_actores.py
│   │   └── README.md
│   ├── 📁 processing/               # Limpieza y preparación
│   │   ├── clean_survey_data.py
│   │   ├── clean_macroeconomic_data.py
│   │   ├── clean_interview_data.py
│   │   └── README.md
│   ├── 📁 analysis/                 # Análisis y estadísticas
│   │   ├── survey_analysis_2026.ipynb
│   │   ├── macroeconomic_analysis.py
│   │   └── README.md
│   ├── 📁 utils/                    # Funciones auxiliares
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── config.py
│   ├── 📁 instruments/              # Cuestionarios e instrumentos
│   │   ├── questionnaire_en.pdf
│   │   ├── questionnaire_es.pdf
│   │   └── README.md
│   ├── DATA_SOURCES.md
│   └── README.md
│
├── 📁 data/
│   ├── 📁 raw/                      # Datos sin procesar
│   │   ├── interviews_actors_20260331.json
│   │   └── youtube_actors_entrepreneurship_20260401.json
│   ├── 📁 processed/                # Datos limpios y procesados
│   │   ├── survey_2026_processed.csv
│   │   ├── macroeconomic_processed.csv
│   │   └── interviews_processed.json
│   ├── 📁 outputs/                  # Resultados de análisis
│   │   ├── figures/
│   │   ├── tables/
│   │   └── statistics/
│   └── README.md
│
├── README.md                         # Overview general
├── .gitignore                        # Actualizado
└── .git/
```

---

## 🎯 Acciones Específicas Recomendadas

### Prioridad ALTA

| Acción | Descripción |
|--------|------------|
| **1. Eliminar `docs/capitulos`** | Duplicado de estructura con nombres sin numerar |
| **2. Reorganizar `code/`** | Crear subcarpetas por funcionalidad (scraping, processing, analysis) |
| **3. Renombrar instrumentos** | Mover a `code/instruments/` y estandarizar nombres |
| **4. Organizar `data/`** | Crear `processed/` y `outputs/` |
| **5. Actualizar `.gitignore`** | Agregar `.DS_Store` y `.claude/` |

### Prioridad MEDIA

| Acción | Descripción |
|--------|------------|
| **6. Crear `docs/assets/`** | Mover `styles.css` e `index.html` |
| **7. Renombrar archivos** | Estandarizar nomenclatura (snake_case, sin espacios) |
| **8. Documentación** | Actualizar README en cada carpeta principal |

### Prioridad BAJA

| Acción | Descripción |
|--------|------------|
| **9. Cleanup** | Remover `.DS_Store` |
| **10. Configurar** | Revisar `.claude/settings.local.json` |

---

## 💡 Prompts Optimizados para Claude Code

### **PROMPT 1: Limpieza y Reorganización Completa** (Recomendado)

```
Reorganiza la estructura de mi tesis doctoral según estos cambios:

1. ELIMINAR:
   - La carpeta 'docs/capitulos/' completa (es duplicada)

2. MOVER archivos:
   - 'docs/styles.css' → 'docs/assets/styles.css'
   - 'docs/index.html' → 'docs/assets/index.html'

3. REORGANIZAR 'code/':
   - Crear: code/scraping/, code/processing/, code/analysis/, code/utils/, code/instruments/
   - Mover scripts de scraping: apify_youtube_actores.py, firecrawl_actores.py → code/scraping/
   - Mover scripts de limpieza: limpiar_datos.R, "code 1.R" → code/processing/ (renombrar sin espacios)
   - Mover análisis: analisis_encuesta_2026.ipynb, analisis_macroeconomico.py → code/analysis/
   - Mover instrumentos: code/instrumentos/* → code/instruments/ (renombrar a questionnaire_es.pdf, questionnaire_en.pdf)

4. REORGANIZAR 'data/':
   - Crear: data/processed/, data/outputs/, data/outputs/figures/, data/outputs/tables/
   - Renombrar archivos en raw/ con snake_case estándar:
     * 'entrevistas_actores_ampliado_20260331.json' → 'interviews_actors_20260331.json'
     * 'youtube_actores_emprendimiento_claude_20260401.json' → 'youtube_actors_entrepreneurship_20260401.json'

5. ACTUALIZAR archivos:
   - Actualizar .gitignore para excluir: .DS_Store, .claude/, *.pyc, __pycache__/

6. CREAR documentación:
   - Crear README.md en: code/scraping/, code/processing/, code/analysis/, code/instruments/
   - Cada README debe explicar el propósito de la carpeta y cómo usar los scripts

7. USAR git:
   - Crear un commit describiendo estos cambios de reorganización
```

---

### **PROMPT 2: Solo Estructuras (sin mover archivos)**

```
Reorganiza la estructura de carpetas de mi tesis doctoral:

1. En 'code/', crear estas subcarpetas:
   - code/scraping/
   - code/processing/
   - code/analysis/
   - code/utils/
   - code/instruments/

2. En 'data/', crear:
   - data/processed/
   - data/outputs/figures/
   - data/outputs/tables/
   - data/outputs/statistics/

3. En 'docs/', crear:
   - docs/assets/

4. Crear archivos README.md en:
   - code/scraping/README.md
   - code/processing/README.md
   - code/analysis/README.md
   - code/instruments/README.md

Luego, sugiere un plan de cómo migrar los archivos existentes a estas nuevas carpetas.
```

---

### **PROMPT 3: Migración Gradual (por fases)**

```
Quiero reorganizar mi tesis doctoral en fases para evitar cambios masivos. Sugiere:

FASE 1 - Esta semana:
- Eliminar docs/capitulos/ (verificar que no haya contenido único)
- Crear estructura de carpetas básica (scraping/, processing/, analysis/)

FASE 2 - Próxima semana:
- Mover y renombrar archivos en code/
- Actualizar imports en Jupyter notebooks y scripts Python

FASE 3 - Semana siguiente:
- Reorganizar data/ (raw, processed, outputs)
- Crear documentación en cada carpeta

Para cada fase, proporciona:
1. Lista exacta de cambios
2. Comandos git para trackear los cambios
3. Qué revisar/verificar después de cada cambio
```

---

### **PROMPT 4: Solo Nombres (renombramiento)**

```
Estandariza los nombres de archivos en mi repositorio de tesis a snake_case:

Cambios específicos:
- 'code 1.R' → 'data_cleaning.r'
- 'analisis_encuesta_2026.ipynb' → 'survey_analysis_2026.ipynb'
- 'analisis_macroeconomico.py' → 'macroeconomic_analysis.py'
- 'apify_youtube_actores.py' → 'scrape_youtube_actors.py'
- 'firecrawl_actores.py' → 'scrape_actors_firecrawl.py'
- 'limpiar_datos.R' → 'clean_data.r'

Actualiza también referencias a estos archivos en:
- README.md (global y en code/)
- .gitignore
- Cualquier script que importe estos archivos
```

---

## 📊 Comparativa: Antes vs Después

| Aspecto | ANTES | DESPUÉS |
|---------|-------|---------|
| Carpetas en docs | 11 + capitulos duplicado | 9 + assets |
| Organización code | Scripts sueltos | Por funcionalidad |
| Carpetas data | raw | raw + processed + outputs |
| Claridad de propósito | Confusa | Clara por categoría |
| Facilidad mantenimiento | Baja | Alta |

---

## 🚀 Siguiente Pasos

1. **Elige un prompt** (recomiendo PROMPT 1 para cambio completo)
2. **Abre Claude Code**
3. **Copia el prompt** en la sesión
4. **Revisa los cambios** antes de confirmar
5. **Verifica integridad** de scripts y notebooks
6. **Actualiza documentación** en README principal

¿Necesitas que ejecute alguno de estos prompts ahora?
