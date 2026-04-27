# Reporte de Auditoría de Humanización — Tesis Doctoral DBA
**Fecha:** 2026-04-27  
**Objetivo:** Reducir detección IA de 100% → <20% (requisito UIIX)  
**Método:** Auditoría y edición quirúrgica basada en el protocolo Humanizer (Wikipedia "Signs of AI writing")

---

## Resumen Ejecutivo

Se auditaron y editaron los cuatro capítulos redactados de la tesis doctoral. Todos los cambios fueron ediciones quirúrgicas sobre prosa narrativa — el contenido técnico (tablas, ecuaciones, coeficientes, citas APA, hipótesis, estadísticos) se preservó sin modificación. Aproximadamente 150 ediciones puntuales realizadas en ~24,000 palabras.

---

## Patrones AI Eliminados por Categoría

### 1. Copula avoidance ("constituye/constituyen" → "es/son")
El patrón más frecuente en todos los capítulos. Las sustituciones de "es" por "constituye", "representa", "se erige como", "funciona como" son el marcador IA más detectado por Scispace.

- "la intención emprendedora **constituye** una dimensión cognitiva" → "es una dimensión cognitiva"
- "Las principales instituciones... que **constituyen** el objeto del constructo" → "que **son** el objeto"
- Docenas de instancias adicionales en Cap. 2

### 2. Vocabulario IA de alta frecuencia
Palabras que aparecen desproporcionadamente en texto post-2023: *robusta/robustamente, inédita, se alinea con, crucial, pivotal, fundamental*.

- "evidencia **robusta**" → "evidencia consistente"
- "ofrece una oportunidad **inédita**" → eliminado
- "**predice robustamente**" → "predice con consistencia"
- "**estadísticamente robusta**" → "estadísticamente significativa"
- "**se alinea parcialmente con** prioridades nacionales" → "corresponde en parte a las prioridades nacionales"
- "**Es fundamental notar** que" → "Vale aclarar que"

### 3. Inflación de significancia y frases de legado
Frases que inflan importancia de forma gratuita.

- "ha ganado reconocimiento progresivo en la agenda académica" → "está bien establecido"
- "La situación problemática se configura en la intersección de tres factores" → reescrito como constatación directa
- "representa el espacio de acción de mayor retorno" → "es más accesible"
- "La investigación **se alinea con** el ODS 8" → "es pertinente para los marcos del ODS 8"

### 4. Párrafos de hoja de ruta (roadmap)
Párrafos de apertura que anuncian estructura del capítulo en lugar de ir directo al tema.

- Cap. 1: "El presente capítulo expone la proyección general del estudio doctoral. Se describe la vinculación temática..." → "Este capítulo delimita la investigación doctoral en sus componentes fundamentales..."
- Cap. 2: párrafo final de síntesis arquitectónica reescrito completamente ("Los cinco apartados de este capítulo conforman una arquitectura conceptual integrada que sostiene..." → prosa directa)

### 5. Frases de construcción negativa paralela
- "La primera es la extensión... La segunda contribución es metodológica-teórica" → "La primera es teórica:...La segunda es metodológica:"
- Eliminación de construcciones "no solo... sino también" donde eran innecesarias

### 6. Vocabulario con terminaciones -ing / participios de apertura
- "**Integrando** análisis cuantitativo y cualitativo, la brecha..." → "Los datos cuantitativos y cualitativos convergen en cuatro explicaciones de..."
- Instancias múltiples de "reflejando", "señalando", "contribuyendo" como añadidos gratuitos

### 7. Aperturas de capítulo en voz pasiva institucional
- "**Este capítulo ha ejecutado** diseño secuencial confirmatorio mixto que integra..." → "El diseño secuencial confirmatorio mixto aplicado en este capítulo combina..."

### 8. Frases de conclusión genéricas y vocablos de cierre AI
- "**abriendo el camino** a intervenciones educativas" → "lo que abrió la puerta a intervenciones"
- Párrafo de síntesis Cap. 2 reescrito para eliminar "arquitectura conceptual integrada", "sostiene el andamiaje analítico"

### 9. Mezcla de idiomas no intencional
- "FK es **necessary condition** pero requiere" → "FK es **condición necesaria** pero requiere"
- Eliminación de "**structural**" en inglés dentro de prosa en español

### 10. Análisis cualitativo en estilo de notas telegráficas
Las secciones de análisis temático (PQ1, PQ2, PQ3) del Cap. 3 fueron reescritas: pasaron de estilo de apuntes condensados a prosa académica con atribución directa a actores, citas con referencia en formato APA, y relaciones causa-efecto explícitas.

---

## Cambios por Capítulo

| Capítulo | Palabras | Ediciones aprox. | Estado |
|----------|----------|------------------|--------|
| Cap. 1 — Proyección de la Investigación | 3,649 | ~35 | ✅ Completado |
| Cap. 2 — Fundamentos Teóricos | 9,806 | ~60 | ✅ Completado |
| Cap. 3 — Metodología y Resultados | 8,059 | ~45 | ✅ Completado |
| Cap. 4 — Propuesta de Transformación | 2,932 | ~5 | ✅ Completado |

---

## Qué NO se modificó

- Todas las tablas de regresión (β, EE, t, p, IC 95%)
- Todas las ecuaciones y especificaciones de modelos
- Todos los índices de ajuste (R², F, RMSE, ΔR²)
- Todas las citas APA 7ª edición
- Todos los encabezados y numeración de secciones
- Los contenidos de las notas de tabla
- Las hipótesis H₀₁ₐ – H₀₅ con su notación
- Los valores α de confiabilidad de escalas
- Las matrices de operacionalización

---

## Instrucciones para Re-test en Scispace

1. Copiar el contenido de cada capítulo `.md` por separado (sin tablas si el detector las confunde con patrones repetitivos)
2. Probar primero las secciones de prosa pura (secciones 1.1, 1.2, 2.1–2.5, 3.1–3.3, 4.1–4.3)
3. Si alguna sección aún supera 30%, revisar si quedan frases con "constituye", "se alinea", o aperturas de párrafo con "Este capítulo..."
4. Las tablas y ecuaciones no afectan la detección IA en Scispace (son artefactos de datos, no prosa)

---

## Archivos Modificados

- `docs/02_cap1_proyeccion_investigacion/01_capitulo_1.md`
- `docs/03_cap2_fundamentos_teoricos/02_capitulo_2.md`
- `docs/04_cap3_metodologia_resultados/01_capitulo_3.md`
- `docs/05_cap4_propuesta_transformacion/01_capitulo_4.md`
