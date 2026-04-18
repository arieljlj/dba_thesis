# MEMORY.MD — Tesis DBA: Intención Emprendedora

<!--
Este archivo persiste entre sesiones. Agregar entradas [APRENDER] aquí cuando se
descubren preferencias del investigador, correcciones recurrentes, o decisiones
de diseño importantes. Los agentes leen esto al inicio de cada tarea.
-->

## Contexto del Proyecto

**Investigador:** Jorge Ariel Loaiza Loaiza  
**Programa:** DBA — UIIX, México  
**Institución docente:** COTECNOVA, Cartago, Valle del Cauca, Colombia  
**Tema central:** Factores que determinan la intención emprendedora en estudiantes universitarios colombianos y el rol de las políticas públicas  
**Marco teórico principal:** Teoría del Comportamiento Planificado (Ajzen, 1991)  
**Metodología:** Mixta — cuantitativa (ALBA 2026) + cualitativa (entrevistas YouTube)

---

## Preferencias y Decisiones del Investigador

<!-- Agregar entradas con formato [APRENDER] cuando el investigador corrige o especifica algo -->

[APRENDER] El formato de entrega de la tesis es Word (.docx), NO LaTeX. Siempre trabajar en Markdown y convertir a Word al final. (2026-04-11)

[APRENDER] El sistema de citación es APA 7ª edición exclusivamente. No usar notas al pie para citas — solo citas en texto (Apellido, Año). (2026-04-11)

[APRENDER] El investigador trabaja desde Colombia (español colombiano). Preferir terminología académica colombiana cuando exista alternativa regional. (2026-04-11)

[APRENDER] El instrumento de encuesta es el Dataset ALBA 2025/2026 — no intentar cambiar ni sustituir la escala sin consultar al investigador. (2026-04-11)

[APRENDER] Las entrevistas de YouTube son con actores del ecosistema emprendedor colombiano. El análisis cualitativo es complementario al cuantitativo, no reemplazante. (2026-04-11)

---

## Estado del Pipeline (actualizar con cada sesión)

| Capítulo | Score Actual | Última Revisión | Observación |
|---------|-------------|----------------|-------------|
| Cap. 1 | Sin score | — | Solo sec. 1.1 escrita |
| Cap. 2 | Sin score | — | No iniciado |
| Cap. 3 — Metodología | Sin score | — | Matrices Excel disponibles |
| Cap. 3 — Resultados | Sin score | — | Dataset disponible |
| Cap. 4 | Sin score | — | No iniciado |

---

## Decisiones de Diseño Importantes

<!-- Registrar aquí decisiones que no deben cuestionarse en futuras sesiones -->

(Vacío — agregar a medida que se tomen decisiones)

---

## Problemas Recurrentes

<!-- Anotar errores que se repiten para que los agentes los anticipen -->

(Vacío — agregar a medida que se identifiquen)

---

## [APRENDER] 2026-04-18 — Reformulación de Hipótesis con H₀/Ha

**Contexto:** Estudios cuantitativos con análisis de regresión múltiple REQUIEREN formulación de hipótesis nulas (H₀) e hipótesis alternativas (Ha) para pruebas de significancia estadística.

**Decisión tomada:** 
- Mantener formulación narrativa de hipótesis (H1, H2, H1a, H1b) en Cap. 1 sección 1.8
- AGREGAR secciones 1.8.1 (Formulación Estadística) y 1.8.2 (Especificación de Análisis) con:
  - Tabla de H₀/Ha en notación estadística (β, directionalidad unilateral)
  - 3 modelos de regresión OLS: baseline (TCP), ampliado (políticas públicas), con moderación
  - Criterios de decisión (p < .05, unilateral)
  - Supuestos de diagnóstico (linealidad, normalidad, homocedasticidad, multicolinealidad, outliers)

**Formato de H₀/Ha adoptado:**
- H₀ᵢᵃ (nula): β = 0 (sin efecto)
- Haᵢᵃ (alternativa): β > 0 (efecto positivo), con direccionalidad unilateral porque TCP teoría sustenta solo efectos positivos

**Hipótesis con notación estadística:**
- H₀₁ᵃ/Ha₁ᵃ: Actitud → IE (predictor de mayor magnitud)
- H₀₁ᵇ/Ha₁ᵇ: Autoeficacia → IE (efecto independiente de actitud)
- H₀₁/Ha₁: Políticas públicas (FK, FL) → IE
- H₀₂/Ha₂: Contexto universitario modera (FK×VM, FL×VM) → IE

**Matrices actualizadas:**
- `Cap. 1 sección 1.8.1–1.8.2` (Cap.1_Proyeccion_Investigacion.docx regenerado)
- `Matriz_Operacionalizacion_Variables_DBA-1_Hipótesis_y_Consistencia.md` (H₀/Ha especificadas para cada hipótesis)

**Coherencia verificada:**
✅ Pregunta investigación → Objetivos → Hipótesis → Operacionalización → Análisis
✅ Todas las hipótesis son estadísticamente testables (falsables)
✅ No hay cambio en sustancia; refinamiento metodológico

