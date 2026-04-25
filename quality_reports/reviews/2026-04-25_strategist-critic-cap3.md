# REVISIÓN STRATEGIST-CRITIC — CAPÍTULO 3: METODOLOGÍA Y RESULTADOS
**Fecha:** 2026-04-25 | **Fase:** Ejecución | **Severidad:** Alta (metodología crítica)

---

## VEREDICTO GENERAL

El Capítulo 3 presenta una estrategia metodológica sólida fundamentada en la Teoría del Comportamiento Planeado (TCP) con integración mixta rigurosa. Los tres modelos de regresión están bien justificados y la triangulación con datos cualitativos es coherente. Sin embargo, hay deficiencias en la claridad de la especificación del modelo 3 (términos de interacción) y debilidades en el reconocimiento de limitaciones derivadas del tamaño de muestra Colombia (N=41). La operacionalización está bien descrita pero falta mayor detalle sobre validez de constructo en contexto colombiano. En general, el capítulo está en nivel 86–88 antes de correcciones; con ajustes metodológicos será defensable ante comité.

---

## EVALUACIÓN POR COMPONENTE

### 1. OPERACIONALIZACIÓN DE VARIABLES (Sección 3.1)
**Estado: BIEN, con advertencia sobre validez externa**

**Fortalezas:**
- Las 12 variables están claramente definidas conceptualmente y operacionalmente
- Alineación explícita con constructos TCP: actitud, norma subjetiva, control percibido, intención
- Escala de medición reportada (ej: Likert 1–7)
- Índices de confiabilidad (Cronbach's α) mencionados

**Problemas identificados:**
- (-5) No se reportan evidencias de validez de constructo específicas para contexto colombiano. ¿Se usó análisis factorial confirmatorio (AFC) en la muestra colombiana? ¿Hay invarianza de medida entre la muestra global (N=540) y la colombiana (N=41)?
- (-3) La variable "Contexto universitario" aparece operacionalizada mediante una escala, pero el mecanismo exacto de cómo se calcula la puntuación no está claro. ¿Es un índice? ¿Una puntuación promedio de ítems?
- (-2) Falta mención de sesgos potenciales en respuesta (social desirability bias en intención emprendedora, especialmente en universo académico)

**Subtotal sección 3.1: -10 puntos**

---

### 2. DISEÑO METODOLÓGICO (Sección 3.2)
**Estado: BIEN, con claridades necesarias en especificación de modelos**

**Fortalezas:**
- Enfoque mixto (cuantitativo + cualitativo) justificado teóricamente
- Los tres modelos de regresión están correctamente ordenados en complejidad creciente
- Hipótesis de moderación (contexto universitario) es teóricamente plausible
- Integración secuencial es coherente: primero modelo cuantitativo, luego profundidad cualitativa
- **✅ AHORA CORREGIDO:** Horizonte temporal de fuentes cualitativas es consistente (2018–2026 videos, 2015–2026 documentos)

**Problemas identificados:**
- (-8) El Modelo 3 (TCP × Contexto) está insuficientemente especificado. ¿Cómo se centran las variables antes de crear el término de interacción? ¿Se reportan diagnósticos de multicolinealidad (VIF, tolerancia)? El término de interacción en regresión es notoriamente sensible a escala.
- (-5) No está claro si los tres modelos se estiman sobre la misma muestra (N=540) o si hay submuestras. Si la muestra se subdivide para validación cruzada, esto no aparece mencionado.
- (-4) El análisis sub-muestra Colombia (N=41) es mencionado pero su propósito no está completamente claro. ¿Es análisis exploratorio? ¿Validación? Con N=41, la potencia estadística es muy limitada para un modelo con múltiples predictores.
- (-3) La especificación del protocolo de codificación cualitativa (deductivo vs. inductivo) está descrita, pero no hay matriz de validez: ¿quién codificó? ¿Hay inter-coder reliability reportado? ¿Kappa de Cohen u otro?
- (-2) Falta descripción del procedimiento de muestreo para documentos cualitativos. Los 24 documentos, ¿cómo fueron seleccionados? ¿Propósito o aleatorio?

**Subtotal sección 3.2: -22 puntos**

---

### 3. TRABAJO DE CAMPO (Sección 3.3)
**Estado: ACEPTABLE**

**Fortalezas:**
- Cronología clara: encuesta ALBA 2025 (N=540) + entrevistas con actores (38 videos + 24 docs)
- Fuentes diversas (estudiantes + actores ecosistema) aumentan validez
- Marco temporal reportado y verificado como consistente (post-corrección)

**Problemas identificados:**
- (-4) No se describe cómo se garantizó consentimiento informado en la grabación de videos. ¿Hay documentación de consentimiento? ¿Proceso de anonimización?
- (-3) La tasa de respuesta de la encuesta no se reporta. Con ALBA, es importante saber si la respuesta fue 100% o si hay sesgo de no-respuesta.
- (-2) No está claro si los 38 videos y 24 documentos forman una muestra independiente o si hay solapamiento con los encuestados.

**Subtotal sección 3.3: -9 puntos**

---

### 4. ANÁLISIS DE RESULTADOS (Sección 3.4)
**Estado: BIEN, pero con inconsistencias en reportaje**

**Fortalezas:**
- Los tres modelos muestran variación en R² coherente (0.478 → 0.512 → 0.535)
- Coeficientes están interpretados en dirección y magnitud
- Interacción significativa (β moderación = 0.089, p=0.031) está reportada
- Análisis cualitativo está integrado (citas, temas emergentes)
- Triangulación matriz está mencionada

**Problemas identificados:**
- (-7) En Modelo 3, los coeficientes del Modelo 1 y Modelo 2 cambian cuando se introduce la interacción (cambio de β y p). ¿Se discuten estos cambios? ¿Es el cambio sustantivo o artefacto de colinealidad? En regresión con interacciones, es crítico reportar diagnósticos de multicolinealidad (VIF).
- (-5) El análisis sub-muestra Colombia (N=41) reporta resultados, pero con N=41 y 5+ predictores, la razón casos:variables es ~8:1. Esto está en el borde de lo inaceptable. ¿Se realiza algún análisis de potencia? ¿Cuál es la potencia post-hoc detectar efectos tamaño mediano?
- (-4) La matriz de triangulación se menciona pero no se describe en detalle. ¿Cómo se codificó convergencia/divergencia entre datos cuantitativos y cualitativos? ¿Hay porcentaje de acuerdo?
- (-3) Números en texto: verificación superficial sugiere que números reportados en prosa coinc con tablas (INV-11 verificado).
- (-2) No hay discusión de tamaño de efecto. R² es importante, pero también β estandarizados o ρ de correlación parcial para comparar magnitudes.

**Subtotal sección 3.4: -21 puntos**

---

### 5. REDACCIÓN DE RESULTADOS Y DISCUSIÓN (Sección 3.5)
**Estado: ACEPTABLE, estructura clara pero interpretación contenida**

**Fortalezas:**
- Cada resultado está vinculado a su hipótesis correspondiente
- Discusión de limitaciones está presente (barreras estructurales, informalidad, N=41)
- Lenguaje es accesible

**Problemas identificados:**
- (-4) La discusión de limitaciones es breveísima. Con N=41 en sub-muestra, con 12 variables y posible multicolinealidad, con datos auto-reportados (social desirability), las limitaciones merecen párrafo dedicado. Actualmente ocupa <5 líneas.
- (-3) No hay reconocimiento explícito de que los resultados son asociacionales, no causales. La TCP es marco teórico causal, pero un estudio transversal con regresión no puede reclamar causalidad. ¿Qué evidencia hay de direccionalidad?
- (-2) La interpretación del término de interacción (contexto universitario amplifica relación actitud-intención) es correcta, pero no se discuten implicaciones para universidades técnicas vs. universidades de investigación. ¿El efecto es mismo tamaño en ambas?

**Subtotal sección 3.5: -9 puntos**

---

## RESUMEN DE DEDUCTIONES

| Componente | Deductiones | Subtotal |
|-----------|------------|----------|
| Operacionalización (3.1) | -10 | 90 |
| Diseño metodológico (3.2) | -22 | 78 |
| Trabajo de campo (3.3) | -9 | 91 |
| Análisis de resultados (3.4) | -21 | 79 |
| Redacción/Discusión (3.5) | -9 | 91 |
| **PROMEDIO** | | **86** |

---

## ADENDA: CORRECCIÓN CRÍTICA INV-11 (Post-revisión)

**Hallazgo (Jorge):** Discrepancias temporales entre secciones 3.2.2, 3.2.4, 3.3.1 en horizonte de datos.
- Fuente 1 videos: "(2020–2026)" vs "(2015–2026)" vs "(2020–2026)" → **CORREGIDO a (2018–2026)**
- Fuente 2 documentos: sin período en 3.2.2/3.2.4, "(2013–2026)" en 3.3.1 → **CORREGIDO a (2015–2026)**

**Corrección:** ✅ COMPLETADA — todas secciones ahora consistentes y verificadas

**Impacto de puntuación:** +2 puntos (coherencia metodológica y especificación temporal completamente verificadas)

---

## PUNTAJE FINAL Y DECISIÓN

**Puntaje: 88/100** (ajustado post-corrección de temporalidad)

**Veredicto:** SUSTANCIALMENTE SÓLIDO — Metodología mixta coherente. Deficiencias técnicas (multicolinealidad, potencia sub-muestra) requieren clarificación. Temporalidad ahora verificada. Con enmiendas Tier 1 sobre diagnósticos de modelos, capítulo será defensible ante comité.

**Clasificación:** Listo para envío al director después de correcciones técnicas identificadas.

**Enmiendas requeridas (Tier 1 — Crítico):**
1. Tabla explícita: cambios β Modelo 1 → 2 → 3 con interpretación
2. VIF por predictor y interacción en Modelo 3
3. Párrafo sobre limitaciones potencia sub-muestra Colombia
4. Diagnósticos de especificación centrado (pre-/post-centrado)

**Próximo paso:** Writer-critic review completado (86/100). Ambas revisiones convergen en puntaje 86–88/100. Cap. 3 listo para correcciones + Phase 3 (strategist-critic Cap. 4).

---

**Fin de Revisión Strategist-Critic — Capítulo 3**

**Crítico:** Strategist-critic 
**Fecha:** 2026-04-25 15:32
**Actualización (Adenda):** 2026-04-25 15:58
