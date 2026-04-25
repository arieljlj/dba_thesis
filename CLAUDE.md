# CLAUDE.MD — Tesis Doctoral DBA: Intención Emprendedora en Colombia

**Proyecto:** Factores determinantes de la intención emprendedora en estudiantes universitarios colombianos y el rol de las políticas públicas
**Universidad:** UIIX — Universidad de Investigación e Innovación de México
**Programa:** Doctorado en Administración de Empresas (DBA)
**Candidato:** Jorge Ariel Loaiza Loaiza
**Institución actual:** COTECNOVA — Cartago, Valle del Cauca, Colombia
**Directora/Director:** [Por confirmar]
**Rama:** main

---

## Principios de Trabajo

- **Plan primero** — Para tareas no triviales, planifica antes de ejecutar; guarda planes en `quality_reports/plans/`
- **Verifica después** — Confirma que el output es correcto al final de cada tarea
- **Word/Markdown es el formato** — La tesis se entrega en Word (UIIX); los borradores se trabajan en Markdown
- **APA 7ª edición** — Sistema de citación exclusivo para todo el documento
- **Umbral de calidad** — Nada va al comité con puntuación < 90; nada va al director con < 80
- **Pares trabajador-crítico** — Todo capítulo generado tiene un crítico asignado
- **Memoria automática** — Las correcciones y preferencias del investigador se guardan en `MEMORY.md`

---

## Referencia Rápida de Comandos

| Comando | Qué hace |
|---------|----------|
| `/discover literatura [tema]` | Búsqueda de literatura para marco teórico o estado del arte |
| `/discover datos` | Evaluación del dataset disponible (ALBA, entrevistas) |
| `/strategize metodologia` | Diseño o revisión de la estrategia metodológica |
| `/analyze datos` | Análisis estadístico del dataset de encuesta |
| `/write [capitulo]` | Redactar o revisar sección del capítulo |
| `/review [archivo]` | Revisión de calidad del capítulo (simula comité) |
| `/tools commit` | Crear commit git con mensaje estándar |

---

## Estructura de la Tesis (UIIX V4, Sep. 2025)

```
docs/
├── 00_portada_resumen_abstract/    # Título, resumen, abstract
├── 01_introduccion/                # Presentación general
├── 02_cap1_proyeccion_investigacion/  # Pregunta, objetivos, hipótesis
│   └── 01_capitulo_1.md            # ← EN DESARROLLO
├── 03_cap2_fundamentos_teoricos/   # Marco teórico, conceptual, contextual
├── 04_cap3_metodologia_resultados/ # Operacionalización, análisis, resultados
│   └── markdown_from_excel/        # Matrices de operacionalización
├── 05_cap4_propuesta_transformacion/  # Propuesta de política/modelo
├── 06_conclusiones/
├── 07_recomendaciones/
├── 08_bibliografia/
└── 09_anexos/
```

---

## Datos y Código Disponibles

```
data/
├── raw/
│   ├── interviews_actors_extended_20260331.json    # Entrevistas actores ecosistema
│   └── youtube_actors_entrepreneurship_20260401.json  # Datos YouTube
└── processed/
    └── survey_data_2026.csv   # Dataset ALBA 2026 — encuesta IE

code/
├── scraping/    # Scripts de recolección de datos (Python)
├── processing/  # Limpieza de datos (R)
├── analysis/    # Análisis (Python/R/Jupyter)
└── instruments/ # Cuestionarios PDF (ES/EN)
```

---

## Dependencias de Fases

| Capítulo | Requiere | Estado |
|----------|---------|--------|
| Cap. 1 — Proyección | Idea de investigación aprobada | 🔄 En desarrollo |
| Cap. 2 — Fundamentos | Estado del arte + definición de constructos | ⬜ Pendiente |
| Cap. 3 — Metodología | Cap. 1 aprobado + datos disponibles | ⬜ Pendiente |
| Cap. 3 — Resultados | Metodología aprobada + análisis ejecutado | ⬜ Pendiente |
| Cap. 4 — Propuesta | Resultados Cap. 3 aprobados | ⬜ Pendiente |
| Conclusiones | Todos los capítulos aprobados | ⬜ Pendiente |
| Defensa | Score global ≥ 95, todos los componentes ≥ 80 | ⬜ Terminal |

---

## Umbrales de Calidad

| Score | Puerta | Aplica a |
|-------|--------|----------|
| 65 | Borrador funcional | Continuar desarrollo |
| 80 | Director/Asesor | Enviar para revisión |
| 90 | Comité Doctoral | Presentar ante comité |
| 95 | Defensa | Versión final (bloquea por componente) |

Ver `.claude/rules/quality.md` para la fórmula de agregación ponderada.

---

## Formato del Documento (UIIX)

- **Tipo de letra:** Times New Roman 12 pt
- **Interlineado:** 1.5 (citas textuales: espacio simple)
- **Márgenes:** Izquierdo 4 cm, Superior/Inferior/Derecho 2.5 cm
- **Numeración:** Superior derecha
- **Citas:** APA 7ª edición — sistema autor-fecha
- **Extensión:** 120–200 páginas
- **Formato de entrega:** Word (.docx)

---

## Estado Actual del Proyecto

| Componente | Archivo | Estado | Descripción |
|-----------|---------|--------|-------------|
| Cap. 1 | `docs/02_cap1_proyeccion_investigacion/01_capitulo_1.md` | ✅ Completo | H₀/Ha reformuladas, operacionalización alineada |
| Cap. 2 | `docs/03_cap2_fundamentos_teoricos/02_capitulo_2.md` | ✅ Redactado (11,146 palabras) | Incluye sec. 2.6 marco cualitativo; pendiente writer-critic |
| Cap. 3 | `docs/04_cap3_metodologia_resultados/01_capitulo_3.md` | ✅ Revisiones completadas | Phase 1 strategist-critic: 88/100 (post-corrección temporal); Phase 2 writer-critic: 86/100 (post-INV-11). Listo para enmiendas Tier 1 antes de comité |
| Operacionalización | `docs/04_cap3_metodologia_resultados/markdown_from_excel/` | ✅ Completo | 3 matrices en Markdown |
| Dataset ALBA | `data/processed/survey_data_2026.csv` | ✅ Disponible | N=540 global, N=41 Colombia |
| Entrevistas | `data/raw/interviews_actors_extended_20260331.json` | ✅ Disponible | 38 videos + 24 documentos (~280K palabras) |
| Cap. 4 | `docs/05_cap4_propuesta_transformacion/01_capitulo_4.md` | ✅ Revisiones completadas | Phase 3 strategist-critic: 86/100; Phase 4 writer-critic: 87/100. Combinado: 86.5/100. Listo para enmiendas Tier 1 (linaje causal + APA referencias) antes de comité |
| Análisis | Cap. 3 Sección 3.3 | ✅ Especificado | 3 modelos regresión, sub-análisis Colombia, integración mixta |

---

## Convención de Commits

- `feat:` Nueva sección o contenido relevante
- `fix:` Corrección de contenido existente
- `data:` Actualización de datos
- `ref:` Ajuste bibliográfico
- `wip:` Trabajo en progreso (borrador)
- `infra:` Cambios en infraestructura `.claude/`

---

## Recuperación de Sesión

Después de compresión de contexto o nueva sesión:
1. Leer este `CLAUDE.md` + plan más reciente en `quality_reports/plans/`
2. Revisar `git log --oneline -10` y `MEMORY.md`
3. Enunciar: "Reanudando. Última tarea: [X]. Estado: [Y]."
