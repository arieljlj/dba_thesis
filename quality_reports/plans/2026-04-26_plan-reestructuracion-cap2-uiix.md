# Plan: Reestructuración Cap. 2 según Estructura UIIX

**Fecha:** 2026-04-26  
**Objetivo:** Reorganizar Cap. 2 de 8 secciones actuales a 5 secciones UIIX con citas completas y fortificación de contenido  
**Estado:** DRAFT — Pendiente aprobación  
**Prioridad:** TIER 1 BLOQUEANTE

---

## Contexto

**Problema Identificado:**
- Cap. 2 actual tiene estructura no-UIIX (8 secciones, incluye 2.6, 2.7, 2.8 fuera de estándar)
- Secciones 2.3 (Conceptual), 2.4 (Contextual), 2.5 (Legal) carecen de citas a autores
- 2.1 Estado del arte es muy corto (< 2,000 palabras)
- Hay dos reportes de literatura en `drafts/` con 174 + 432 estudios + referencias completas

**Estructura UIIX Requerida:**
```
Capítulo II — Fundamentos Teóricos Referenciales
  2.1 Estado del arte (Marco Histórico y Actual)
  2.2 Marco Teórico
  2.3 Marco Conceptual
  2.4 Marco Contextual
  2.5 Marco Legal y Normativo
```

**Acción:** Redistribuir contenido de 2.6, 2.7, 2.8 en otros capítulos, agregar citas masivas desde reportes drafts.

---

## Plan de Implementación

### FASE 1: Análisis y Extracción (30 min)

**Tarea 1.1:** Extraer todas las citas + referencias de:
- `entrepreneurial_intention_frameworks_synthesis.md` (174 estudios)
- `EI_Literature_Mapping_Report.md` (432 estudios)
- Identificar autores clave por tema: TCP, contexto colombiano, marco legal, operacionalización

**Tarea 1.2:** Mapear contenido actual de Cap. 2:
- Líneas 24–100: TCP (2.1–2.2) → Mantener + Enriquecer
- Líneas 107–208: Operacionalización → Integrar en 2.3 Marco Conceptual
- Líneas 209–325: Colombia + Marco Legal → 2.4 + 2.5
- Líneas 376–429: Validación cualitativa → Distribuir a Cap. 1 (justificación mixta) o Cap. 3 (diseño)
- Líneas 433–507: Integración/modelo → Distribuir a Cap. 1 (presentación de hipótesis/modelo)

**Tarea 1.3:** Identificar brechas por sección UIIX:
- 2.1 Estado del arte: Necesita 3,000–4,000 palabras, actualmente ~1,000
- 2.2 Marco teórico: TCP sólido, necesita cita de meta-análisis (Schlaegel & Koenig 2014)
- 2.3 Marco conceptual: Operacionalización + constructos centrales; FALTA citación de fuentes originales
- 2.4 Marco contextual: Datos colombianos OK, FALTA citación de contexto LATAM, GEM, DANE
- 2.5 Marco legal: Ley 1014, Ley 2069, CONPES OK, FALTA conexión con intención emprendedora + autores que han estudiado esto

---

### FASE 2: Reestructuración del Documento (2 horas)

**Tarea 2.1:** Crear estructura UIIX vacía con secciones y subsecciones planeadas

```markdown
# Capítulo II — Fundamentos Teóricos Referenciales

## 2.1 Estado del arte (Marco Histórico y Actual)
   ### 2.1.1 Evolución conceptual de la intención emprendedora (2010-2026)
   ### 2.1.2 Teorías fundamentales: TCP vs. Modelo de Evento Emprendedor
   ### 2.1.3 Estado actual de la investigación: hallazgos clave y tendencias

## 2.2 Marco Teórico
   ### 2.2.1 Teoría del Comportamiento Planificado (TCP/TPB)
   ### 2.2.2 Constructos centrales del TCP: validación meta-analítica
   ### 2.2.3 Limitaciones teóricas del TCP y extensiones contemporáneas

## 2.3 Marco Conceptual
   ### 2.3.1 Definición operacional de intención emprendedora
   ### 2.3.2 Constructos medibles derivados del TCP
      - Actitud hacia el emprendimiento (AT)
      - Normas subjetivas (SN)
      - Control conductual percibido (PBC)
      - Factores de conocimiento familiar (FK)
      - Factores de locus de control (LC)
   ### 2.3.3 Moderadores contextuales: integración conceptual

## 2.4 Marco Contextual
   ### 2.4.1 Contexto latinoamericano de emprendimiento
   ### 2.4.2 Contexto colombiano: datos GEM, ALBA, ecosistema emprendedor
   ### 2.4.3 Factores contextuales que modulan la intención emprendedora

## 2.5 Marco Legal y Normativo
   ### 2.5.1 Política pública de emprendimiento en Colombia
   ### 2.5.2 Instrumentos normativos: Ley 1014, Ley 2069, CONPES
   ### 2.5.3 Conexión entre marcos legales e intención emprendedora
```

**Tarea 2.2:** Redactar 2.1 Estado del arte (~3,500 palabras)
- Párrafo introductorio: Evolución de la intención emprendedora como campo 2010-2026 (citando reportes)
- Subsección 2.1.1: Síntesis de los dos marcos teóricos dominantes con autores clave
  - Ajzen & TPB (Schlaegel & Koenig 2014 meta-análisis; Liñán & Chen 2009)
  - Shapero & Sokol (Krueger; Iakovleva et al. 2009)
- Subsección 2.1.2: Tendencias recientes (2020-2026): sostenibilidad, digitalización, COVID-19
- Subsección 2.1.3: Estado actual en contextos LATAM y Colombia

**Tarea 2.3:** Enriquecer 2.2 Marco Teórico con citas
- Mantener estructura TCP existente
- Agregar citación completa de meta-análisis (Schlaegel & Koenig 2014)
- Citaciones de estudios colombianos (Blanco-Mesa 2023; Zenodo ALBA dataset)
- Agregar limitaciones del TCP con citas (LiHua 2022; Kautonen et al. 2015)

**Tarea 2.4:** Reescribir 2.3 Marco Conceptual
- Sección 2.3.1: Definición operacional de IE con cita de Liñán & Chen
- Sección 2.3.2: Mapeo de constructos del TCP
  - AT (Ajzen 1991; Yang 2013; Hassan 2013)
  - SN (Ajzen 1991; Yang 2013)
  - PBC (Bandura; Ajzen; Hassan 2013; Su et al. 2021)
  - FK, LC: Constructos nuevos/extensiones — citar fuentes en Schlaegel & Koenig 2014
- Sección 2.3.3: Moderadores contextuales — integrar contenido actual 2.6 + citaciones del reporte EI_Literature_Mapping

**Tarea 2.5:** Reescribir 2.4 Marco Contextual
- Sección 2.4.1: Contexto LATAM (citar: Regional Overview de reporte 2; autores LATAM específicos)
- Sección 2.4.2: Contexto colombiano (GEM 2024 23.5% TEA; dataset ALBA N=540; estudios colombianos)
- Sección 2.4.3: Factores contextuales moderadores — integrar datos de tabla de moderadores actual

**Tarea 2.6:** Reescribir 2.5 Marco Legal y Normativo
- Sección 2.5.1: Evolución de política pública (Ley 1014, Ley 2069, CONPES)
- Sección 2.5.2: Descripción detallada de instrumentos normativos
- Sección 2.5.3: Nexo con IE — citar estudios que conectan política → IE (Reporte 2, sección 7)

---

### FASE 3: Eliminación y Redistribución de Contenido (1 hora)

**Tarea 3.1:** Eliminar secciones actuales 2.6, 2.7, 2.8
- 2.6 "Por qué contexto es crítico..." → **Redistribuir a Cap. 1 (Justificación de la investigación)**
  - Párrafo adicional en 1.5 (Justificación) que cite esta argumentación
- 2.7 "Marco cualitativo: perspectivas de actores ecosistema..." → **Redistribuir a Cap. 3 (Diseño metodológico)**
  - Sección 3.2.3 (Integración mixta) o 3.5 (Análisis cualitativo)
- 2.8 "Integración: modelo conceptual..." → **Redistribuir a Cap. 1 (Presentación del modelo)**
  - Sección 1.4 o nueva 1.6 (Modelo de investigación)
  - Presentar hipótesis operadas desde el modelo

**Tarea 3.2:** Crear notas de trazabilidad
- En Cap. 1: "El modelo de intención emprendedora moderada por contexto se desarrolla teóricamente en Cap. 2 (Secciones 2.2-2.4)"
- En Cap. 3: "El enfoque mixto para validación de constructos se detalla en la sección de diseño"

---

### FASE 4: Normalización APA y Verificación (1 hora)

**Tarea 4.1:** Normalizar todas las referencias inline a APA 7ª
- Garantizar consistencia de formato: (Autor, Año, p. #) para citas directas
- Verificar que todas las fuentes estén en Bibliography_base.bib
- Agregar DOI/URL para todas las fuentes (especialmente legales colombianas)

**Tarea 4.2:** Verificación de números en texto
- Línea 210: "23.5% TEA" → Agregar cita año + fuente (GEM 2024)
- Línea 215: "70% estudiantes" → Aclarar fuente y año
- Todas las referencias a Cronbach alphas → Citar fuente original de cada escala

**Tarea 4.3:** Aplicar humanización selectiva
- Variación sintáctica en párrafos densos (2.1, 2.4)
- Lenguaje académico natural sin copula avoidance

---

## Cambios en Archivos

| Archivo | Acción | Líneas Afectadas |
|---------|--------|------------------|
| `docs/03_cap2_fundamentos_teoricos/02_capitulo_2.md` | Reescribir completamente | Líneas 1-507 → Nueva estructura 5 secciones |
| `docs/01_introduccion/01_capitulo_1.md` | Agregar secciones | Líneas finales: 1.5 (Justificación enriquecida) + 1.6 (Modelo) |
| `docs/04_cap3_metodologia_resultados/01_capitulo_3.md` | Agregar subsecciones | Sección 3.2 o 3.5: Validación cualitativa + integración mixta |
| `Bibliography_base.bib` | Expandir | Agregar ~100 referencias nuevas de reportes (copilot puede extraer) |

---

## Estimación de Tiempo

| Fase | Tarea | Estimado |
|------|-------|----------|
| 1 | Análisis y extracción | 30 min |
| 2 | Reestructuración | 120 min |
| 3 | Redistribución | 60 min |
| 4 | Normalización | 60 min |
| **TOTAL** | | **270 min (4.5 horas)** |

---

## Criterios de Éxito

✅ Cap. 2 reorganizado en 5 secciones UIIX exactas (sin 2.6, 2.7, 2.8)  
✅ 2.1 Estado del arte: ≥ 3,500 palabras con ≥ 15 citas de estudios clave  
✅ Secciones 2.3, 2.4, 2.5: Citas completas (mínimo 3 citas por sección)  
✅ Todas las referencias APA 7ª normalizadas + en Bibliography_base.bib  
✅ Números en texto: GEM 2024 + año explícito + fuente  
✅ Contenido 2.6, 2.7, 2.8 redistribuido a Cap. 1 y Cap. 3 con notas de trazabilidad  
✅ Writer-critic review: Score ≥ 85/100  

---

## Decisión Requerida

**¿Proceder con este plan de reestructuración?**

Alternativas:
1. **Sí, proceder ahora** — Implementar las 4 fases (4.5 horas)
2. **Sí, pero redacción minimalista** — Versión comprimida (2 horas, menos citas)
3. **No, esperar más feedback** — Ajustar plan antes de ejecutar
4. **Otro enfoque** — ¿Cambios al plan?
