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
    └── datos_encuesta_2025.csv   # Dataset ALBA 2025 — encuesta IE (nombre real del archivo)

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
| Cap. 1 — Proyección | Idea de investigación aprobada | ✅ Completo |
| Cap. 2 — Fundamentos | Estado del arte + definición de constructos | ✅ Completo (90/100) |
| Cap. 3 — Metodología y Resultados | Análisis Fase C ejecutado | ✅ Completo (~88/100, pendiente revisión formal) |
| Cap. 4 — Propuesta | Resultados Cap. 3 | ✅ Enmiendas A–F (83/100, pendiente Tier 2) |
| Conclusiones | Todos los capítulos redactados | ⚠️ Pendiente revisión alineación Fase C |
| Recomendaciones | Conclusiones aprobadas | ⚠️ Pendiente revisión alineación Fase C |
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

> **Última sesión:** 2026-04-27 — Fase C completada. Todos los capítulos alineados con datos reales. Ver `SESSION_REPORT.md` para detalle.

| Componente | Archivo | Estado | Score | Descripción |
|-----------|---------|--------|-------|-------------|
| Portada / Resumen / Abstract | `docs/00_portada_resumen_abstract/` | ✅ Actualizado | — | Estadísticos reales: R²=0.537, EA β_std=0.665, FK/FL ns, EA×U-D ns, brecha ~45pp |
| Cap. 1 | `docs/02_cap1_proyeccion_investigacion/01_capitulo_1.md` | ✅ Actualizado | — | Nota H2 corregida: moderación no confirmada cuantitativamente; sostenida cualitativamente |
| Cap. 2 | `docs/03_cap2_fundamentos_teoricos/02_capitulo_2.md` | ✅ Completo | 90/100 | 11,146 palabras. Aprobado para director. |
| Cap. 3 | `docs/04_cap3_metodologia_resultados/01_capitulo_3.md` | ✅ Fase C completa | ~88/100* | Fases A+B+C ejecutadas. VIF declarado. Pendiente writer-critic formal post-Fase C. |
| Cap. 4 | `docs/05_cap4_propuesta_transformacion/01_capitulo_4.md` | ✅ Enmiendas A–F | 83/100 | Sección 4.1 corregida. Apto director (≥80). Para comité necesita Tier 2 (≥90). |
| Conclusiones | `docs/06_conclusiones/conclusiones.md` | ⚠️ Pendiente revisión | — | Verificar alineación con hallazgos Fase C |
| Recomendaciones | `docs/07_recomendaciones/recomendaciones.md` | ⚠️ Pendiente revisión | — | Verificar alineación con hallazgos Fase C |
| Bibliografía | `docs/08_bibliografia/referencias_apa.md` | ✅ Actualizado | — | +Nabi et al. (2017), +Frese et al. (2016) |
| Anexos | `docs/09_anexos/` | ✅ Completo | — | `anexos.md` + `A1_Fuentes_Cualitativas_Completas.md` |
| DOCX compilado | `Tesis_DBA_Loaiza_2026.docx` | ✅ Vigente (142K) | — | Todos los capítulos incluidos en orden correcto |
| Dataset | `data/processed/datos_encuesta_2025.csv` | ✅ Disponible | — | N=540 global, N=41 Colombia (country==5) |
| Scripts análisis | `code/analysis/` | ✅ Completo | — | `fase_c_regression.py`, `fix_cap3_fase_c.py`, `fix_cap3.py` |

*Score estimado post-correcciones; pendiente revisión formal writer-critic.

---

## Hallazgos Clave Fase C (referencia rápida)

| Hipótesis | Resultado real |
|-----------|---------------|
| H1a: EA predice EI | ✅ β_std=0.665***, predictor dominante |
| H1b: SE predice EI | ❌ β_std=0.046, ns en M1 |
| H1: FK, FL predicen EI | ❌ FK β=−0.047 ns; FL β=−0.002 ns — operan como antecedentes de EA |
| H2: Contexto universitario modera | ❌ cuantitativo (VIF severo); ✅ cualitativo (intermediación local) |
| LC predictor contextual | ⚠️ β=−0.153*, p=.034 (negativo: locus interno → menor IE declarada) |

**Multicolinealidad M3:** VIF>10 para S(27.3), FK(27.7), FL(13.8), U-AS(25.7), LC(49.3). Solo EA, SE y LC tienen interpretación confiable en M3.

---

## Próximos Pasos Prioritarios

1. **Writer-critic formal Cap. 3** — objetivo ≥88 director, ≥90 comité
2. **Revisar Conclusiones y Recomendaciones** — alinear con hallazgos Fase C
3. **Enmiendas Tier 2 Cap. 4** — llevar 83→90 para comité
4. **Commit git** — `fix: alinear estadísticos reales Fase C en C1/C3/C4/resumen/abstract`

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
