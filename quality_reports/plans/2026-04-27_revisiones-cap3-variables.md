# Plan de Revisión: Capítulo 3 — Corrección de Variables y Estadísticos
**Fecha:** 2026-04-27  
**Estado:** PENDIENTE DE APROBACIÓN  
**Prioridad:** Alta — afecta análisis cuantitativo central de la tesis  
**Archivo afectado:** `docs/04_cap3_metodologia_resultados/01_capitulo_3.md`

---

## Contexto

Durante la auditoría del Anexo A se detectó que los nombres de variables, códigos CSV, número de ítems, escala Likert y valores de medias reportados en el Capítulo 3 **no corresponden al dataset real** (`datos_encuesta_2025.csv`). Las discrepancias son sistemáticas y afectan toda la sección de operacionalización, estadísticos descriptivos y modelos de regresión.

---

## Discrepancias Identificadas

### 1. Escala de respuesta

| Ubicación | Valor actual (incorrecto) | Valor correcto |
|-----------|--------------------------|----------------|
| Línea ~64 del Cap. 3 | `Likert 1–7 (excepto demografía)` | `Likert 1–5 (excepto EW que usa 1–7)` |
| Tabla operacionalización (todas las filas) | `Likert 1–7` | `Likert 1–5` |
| Sección 3.2.1 (texto) | `escala Likert 1–7` | `Likert 1–5` |
| Limpieza de datos: `eliminación de casos con valores >7` | `valores >7` | `valores >5` |

### 2. Variable Dependiente: Intención Emprendedora

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Código CSV | IE1–IE2 | **EI1–EI5** |
| Número de ítems | 2 | **5** |
| Media global | M = 3.68 (DE = 1.92) | **M = 4.021 (DE = 1.057)** |
| Escala | 1–7 | **1–5** |

### 3. Actitud Emprendedora (constructo TCP: AT)

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Código CSV | AT1–AT5 | **EA1–EA8** |
| Número de ítems | 5 | **8** |
| Media global | M = 5.12 (DE = 1.45) | **M = 4.065 (DE = 1.019)** |
| Media Colombia | (no reportada) | M = 4.299 |
| Escala | 1–7 | **1–5** |
| Descripción ítems | "attractiveness, oportunidad económica, prestigio social, autorrealización" | Ítems reales: proveer empleo, agente de cambio, reconocimiento, liderazgo, flexibilidad, pasión, desempleo, posición social |

### 4. Normas Subjetivas (constructo TCP: SN)

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Código CSV | SN1–SN3 | **S1–S3** |
| Media global | M = 4.23 (DE = 1.58) | **M = 3.577 (DE = 1.049)** |
| Media Colombia | (no reportada) | M = 3.683 |
| Escala | 1–7 | **1–5** |
| Descripción ítems | "presión social de referentes (familia, pares, profesores)" | Ítems reales miden imagen social de empresarios en la sociedad — **no presión normativa directa**. Requiere nota metodológica sobre diferencia con SN clásico de TCP. |
| **Nota adicional** | — | Los ítems S1–S3 no miden SN en el sentido TCP estricto. La operacionalización es híbrida (cuantitativa + cualitativa). El texto debe aclararlo. |

### 5. Control Conductual Percibido (constructo TCP: PBC)

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Código CSV | PBC1–PBC6 | **SE1–SE5** |
| Número de ítems | 6 | **5** |
| Media global | M = 4.52 (DE = 1.51) | **M = 3.839 (DE = 0.945)** |
| Media Colombia | M = 4.18 | **M = 3.907** |
| Escala | 1–7 | **1–5** |
| Descripción ítems | "autoeficacia + percepción de barreras/recursos" | Ítems reales: autoeficacia emprendedora pura (SE1–SE5); las barreras no están en estos ítems |

### 6. Conocimiento Formal del Ecosistema (FK)

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Media global | M = 3.94 | **M = 3.709 (DE = 1.089)** |
| Media Colombia | M = 3.56 | **M = 3.534** |
| Escala | 1–7 | **1–5** |
| Número de ítems | 8 | **8** (correcto, pero verificar FK8) |

### 7. Alfabetización Financiera (FL)

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Código CSV | FL1–FL5 | **FL1–FL6** |
| Número de ítems | 5 | **6** |
| Media global | M = 4.01 (DE = 1.54) | **M = 2.949 (DE = 1.195)** |
| Media Colombia | M = 3.78 | **M = 2.797** |
| Escala | 1–7 | **1–5** |

### 8. Desarrollo Institucional Universitario (U-D)

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Media global | M = 4.35 (DE = 1.59) | **M = 3.634 (DE = 1.031)** |
| Media Colombia | M = 4.22 | **M = 4.102** |
| Escala | 1–7 | **1–5** |

### 9. Apoyo Académico (U-AS)

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Media global | M = 4.29 (DE = 1.58) | **M = 3.383 (DE = 1.114)** |
| Media Colombia | M = 4.15 | **M = 3.967** |
| Escala | 1–7 | **1–5** |

### 10. Locus de Control / Clima de Aprendizaje (LC)

| Aspecto | Valor actual (incorrecto) | Valor correcto |
|---------|--------------------------|----------------|
| Código CSV | LC1–LC4 (Clima de Aprendizaje) | **LC1–LC8 (Locus de Control)** |
| Número de ítems | 4 | **8** |
| Media global | M = 4.41 (DE = 1.44) | **M = 3.315 (DE = 1.136)** |
| Media Colombia | M = 4.28 | **M = 3.396** |
| Escala | 1–7 | **1–5** |
| **Constructo** | "Clima de Aprendizaje Emprendedor" | **Locus de Control** (ítems miden locus interno vs. externo) |

---

## Impacto en Análisis Estadístico

### ⚠️ CRÍTICO: Los modelos de regresión en Cap. 3 sección 3.3 deben rehacerse

Los coeficientes de regresión (β), errores estándar, valores t, R², y la matriz de correlaciones fueron calculados (o especificados) con las variables incorrectas. Las correcciones de nombres de variables y medias implican que **todos los valores estadísticos del Cap. 3.3 deben recalcularse** con el dataset real.

**Variables a corregir en los modelos:**

| Modelo | Variable incorrecta | Variable correcta |
|--------|--------------------|--------------------|
| Todos | AT (AT1–AT5) | EA (EA1–EA8) |
| Todos | SN (SN1–SN3) | S (S1–S3) |
| Todos | PBC (PBC1–PBC6) | SE (SE1–SE5) |
| Todos | IE (IE1–IE2) | EI (EI1–EI5) |
| M2, M3 | FL1–FL5 | FL1–FL6 |

**Centrado en Modelo 3 (valores de media para centrado):**

| Variable | Valor de centrado actual (incorrecto) | Valor correcto |
|----------|--------------------------------------|----------------|
| AT → EA | M = 5.12 | M = 4.065 |
| PBC → SE | M = 4.52 | M = 3.839 |
| U-D | M = 4.35 | M = 3.634 |

---

## Plan de Corrección (Fases)

### Fase A — Correcciones textuales inmediatas (no requieren re-análisis)
Estas correcciones pueden hacerse sin recalcular los modelos:

1. Cambiar `Likert 1–7` → `Likert 1–5` en todo el capítulo (excepto EW)
2. Cambiar `IE1–IE2` → `EI1–EI5` (y actualizar descripción de ítems)
3. Cambiar `AT1–AT5` → `EA1–EA8` (y actualizar descripción de ítems)
4. Cambiar `SN1–SN3` → `S1–S3` (y agregar nota sobre diferencia con SN clásico)
5. Cambiar `PBC1–PBC6` → `SE1–SE5` (y actualizar descripción: 5 ítems, autoeficacia pura)
6. Cambiar `FL1–FL5` → `FL1–FL6` (6 ítems)
7. Cambiar `LC1–LC4 (Clima)` → `LC1–LC8 (Locus de Control)` (8 ítems, con descripción correcta)
8. Nota sobre diseño mixto: SN y PBC operacionalizados mediante triangulación cuantitativa + cualitativa

### Fase B — Corrección de medias y estadísticos descriptivos
Reemplazar todos los valores de M y DE con los del dataset real (tabla de este documento).

### Fase C — Re-análisis y corrección de modelos de regresión ⚠️ REQUIERE ANÁLISIS EN R/PYTHON
Correr los 3 modelos de regresión con:
- Variable dependiente: `EI` (promedio EI1–EI5)
- Predictores TCP: `EA` (EA1–EA8), `S` (S1–S3), `SE` (SE1–SE5)
- Moderadores: `FK` (FK1–FK8), `FL` (FL1–FL6), `U-D`, `U-AS`, `LC`
- Matriz de correlaciones completa
- VIF para cada modelo
- Actualizar todos los coeficientes, R², valores t y p

---

## Estado de Cada Fase

| Fase | Estado | Notas |
|------|--------|-------|
| A — Correcciones textuales | ✅ COMPLETADA (2026-04-27) | Ejecutada con `fix_cap3.py`; nombres, escala, ítems corregidos |
| B — Medias y descriptivos | ✅ COMPLETADA (2026-04-27) | Ejecutada con `fix_cap3.py`; M y DE actualizadas con valores reales del dataset |
| C — Re-análisis regresión | ✅ COMPLETADA (2026-04-27) | Script `code/analysis/fase_c_regression.py`; Cap. 3 actualizado con coeficientes reales; hallazgos divergen significativamente de los originales (ver nota abajo) |

---

## Acciones Prioritarias para Próxima Sesión

1. ~~Aprobar este plan de revisión~~ ✅
2. ~~Ejecutar Fase A~~ ✅ Completada 2026-04-27
3. ~~Ejecutar Fase B~~ ✅ Completada 2026-04-27
4. ~~Re-generar DOCX~~ ✅ Completado 2026-04-27 (119K, incluye Cap. 3 actualizado)
5. ~~Ejecutar Fase C~~ ✅ Completada 2026-04-27 — Ver hallazgos clave abajo

---

## ⚠️ Hallazgos Clave Fase C — Divergencias Significativas

### Resultados reales vs. especificación original

| Hipótesis | Esperado | Real |
|-----------|----------|------|
| H₀₁: EA predice EI | β_std≈0.55 | **β_std=0.665*** — Confirmada, efecto mayor** |
| H₀₂: S predice EI | β_std≈0.15 | β_std=0.071* — Marginalmente confirmada |
| H₀₃: SE predice EI | β_std≈0.40 | β_std=0.046 ns en M1 — **No confirmada en baseline** |
| H₀₄: FK predice EI | β_std=0.159*** | β_std=-0.047 ns — **Rechazada** |
| H₀₅: FL predice EI | β_std=0.080* | β_std=-0.012 ns — **Rechazada** |
| H₀₆: EA×U-D modera | β=0.089* | β=-0.057 ns — **Rechazada** |
| H₀₇: SE×U-D modera | β=0.072† | β=0.014 ns — **Rechazada** |

### Multicolinealidad severa en Modelo 3
VIF>10 para: S(27.3), FK(27.7), FL(13.8), U-AS(25.7), LC(49.3)  
→ Coeficientes inestables para estas variables. Solo EA, SE, LC tienen interpretación confiable en M3.

### Único hallazgo contextual robusto
LC (Locus de Control) es el único predictor contextual significativo en M3: β=-0.153, p=.034 (negativo — mayor locus interno asociado a menor intención declarada, posiblemente por realismo mayor ante barreras).

### Implicación para revisión futura
El Capítulo 4 (Propuesta) está construido parcialmente sobre H₀₄, H₀₅, H₀₆, H₀₇ que no se confirman. Requiere revisión crítica de las implicaciones de política basadas en FK y efectos moderadores.
