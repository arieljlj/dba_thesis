# Plan: Reformulación de Hipótesis con H₀/Ha y Verificación de Coherencia Integral

**Fecha:** 2026-04-18  
**Autor:** Claude (strategist-critic)  
**Fase:** Diseño (Cap. 1) — Re-entrada por mejora metodológica  
**Status:** PROPUESTA PARA APROBACIÓN

---

## 1. Objetivo del Plan

Reformular las hipótesis del estudio incluyendo hipótesis nulas (H₀) e hipótesis alternativas (Ha) para garantizar que sean:
1. **Estadísticamente testables** — mediante regresión múltiple y análisis de moderación
2. **Coherentes** — alineadas con pregunta de investigación → objetivos → operacionalización → análisis
3. **Precisas** — en notación y directionalidad esperada

---

## 2. Problema Identificado

**Situación actual (Cap. 1, sección 1.8):**
- Solo hay formulaciones de hipótesis alternativas: H1, H2, H1a, H1b
- **Faltan** las hipótesis nulas (H₀) correspondientes
- Las hipótesis están en forma narrativa, no en notación estadística precisa
- No hay especificación de cómo se testearán en el análisis

**Por qué importa:**
- En estudios cuantitativos con análisis estadístico, las hipótesis nulas son necesarias para pruebas de significancia (α = .05)
- La notación H₀: β = 0 vs Ha: β ≠ 0 (o direccional: β > 0) es estándar en regresión
- Sin H₀ claras, falta claridad sobre qué es el resultado "nulo" vs "significativo"
- La matriz de operacionalización también necesita H₀/Ha para alineación completa

---

## 3. Verificación de Coherencia: Pregunta → Objetivos → Hipótesis

### 3.1 Mapeo Pregunta de Investigación → Objetivo Específico → Hipótesis

| PE | Pregunta de Investigación | OE Correspondiente | Hipótesis Relacionada | Variables Operacionalizadas |
|----|-----------------------------|-------------------|----------------------|---------------------------|
| PE1 | ¿Cuál es el perfil de IE y qué variables individuales (EA, SE, Mot) presentan mayor asociación? | OE1 | H1a (actitud), H1b (autoeficacia) | VD: EI; VI proxy individual: EA (α=0.920), SE (α=0.948) |
| PE2 | ¿Qué nivel de conocimiento y acceso percibido a políticas públicas? ¿Cómo varía según contexto? | OE2 | H1 (percepción de políticas → IE) | VI: FK (α=0.933), FL (α=0.868); VM: Contexto universitario |
| PE3 | ¿Existe relación significativa entre percepción de políticas públicas e IE, controlando por TCP? | OE3 | H1 (principal) | VI: FK + FL; VD: EI; Control: EA, SE, EW |
| PE4 | ¿El contexto universitario modera la relación políticas → IE? | OE4 | H2 (moderadora) | VI: FK+FL; VM: U-D (α=0.912), U-AS (α=0.916), LC (α=0.616); VD: EI |
| PE5 | ¿Qué lineamientos de política se derivan? (exploratoria) | OE5 | Síntesis de H1, H2, H1a, H1b | Todas las variables anteriores |

**Conclusión:** Hay coherencia clara. Cada PE tiene su OE y su hipótesis. Ahora necesitan H₀/Ha precisas.

---

## 4. Formulación de H₀ y Ha para Cada Hipótesis

### 4.1 Hipótesis Principal (H1)

**Formulación Descriptiva Actual:**  
"Las políticas públicas de emprendimiento —medidas a través de la percepción estudiantil del conocimiento formal del ecosistema (FK) y la alfabetización financiera (FL)— se relacionan positiva y significativamente con la intención emprendedora de los estudiantes universitarios."

**Formulación Estadística (NUEVA):**

| Hipótesis | Notación | Interpretación | Test Estadístico |
|-----------|----------|-----------------|-----------------|
| **H₀₁** | β(FK→IE) = 0 **AND** β(FL→IE) = 0 | Las políticas públicas (FK, FL) NO tienen efecto significativo sobre la IE | F-test múltiple (regresión) |
| **Ha₁** | β(FK→IE) > 0 **AND** β(FL→IE) > 0 | Las políticas públicas se relacionan positivamente con IE (direccional, unilateral) | t-test unilateral p < .05 |

**Nota:** Se adopta direccionalidad unilateral (β > 0) porque la teoría y literatura sustentan un efecto positivo (no hay razón teórica para efecto negativo).

---

### 4.2 Hipótesis Moderadora (H2)

**Formulación Descriptiva Actual:**  
"El contexto universitario —medido a través del desarrollo universitario, el apoyo académico y el clima de aprendizaje— modera la relación entre las políticas públicas de emprendimiento y la intención emprendedora: un contexto universitario más favorable amplifica el efecto positivo de las políticas sobre la IE."

**Formulación Estadística (NUEVA):**

| Hipótesis | Notación | Interpretación | Test Estadístico |
|-----------|----------|-----------------|-----------------|
| **H₀₂** | β(FK×VM→IE) = 0 **AND** β(FL×VM→IE) = 0 | No hay interacción significativa (sin efecto de moderación) | F-test de cambio en R² (ΔR² para términos de interacción) |
| **Ha₂** | β(FK×VM→IE) > 0 **AND** β(FL×VM→IE) > 0 | La VM amplifica (modera positivamente) el efecto de políticas sobre IE | t-test unilateral p < .05 |

**Nota:** La moderación se testea comparando dos modelos: modelo base (H1) vs modelo con interacciones (H2). Se usa ΔR² como criterio.

---

### 4.3 Hipótesis Subsidiaria — Actitud (H1a)

**Formulación Descriptiva Actual:**  
"La actitud emprendedora se relaciona positiva y significativamente con la intención emprendedora, siendo el predictor individual de mayor magnitud en el modelo."

**Formulación Estadística (NUEVA):**

| Hipótesis | Notación | Interpretación | Test Estadístico |
|-----------|----------|-----------------|-----------------|
| **H₀₁ₐ** | β(EA→IE) = 0 | La actitud NO tiene efecto significativo sobre IE | t-test (parámetro individual) |
| **Ha₁ₐ** | β(EA→IE) > 0 **AND** \|β(EA→IE)\| > \|β(SE→IE)\| | La actitud tiene efecto positivo Y es el predictor más fuerte (magnitud) | Comparación de β estandarizados |

**Nota:** Parte 1 es significancia; Parte 2 es comparación de magnitud (se usa β estandarizados de la regresión).

---

### 4.4 Hipótesis Subsidiaria — Autoeficacia (H1b)

**Formulación Descriptiva Actual:**  
"La autoeficacia emprendedora se relaciona positiva y significativamente con la intención emprendedora, de forma independiente al efecto de la actitud."

**Formulación Estadística (NUEVA):**

| Hipótesis | Notación | Interpretación | Test Estadístico |
|-----------|----------|-----------------|-----------------|
| **H₀₁ᵦ** | β(SE→IE) = 0 (cuando EA está en el modelo) | La autoeficacia NO tiene efecto significativo, independientemente de actitud | t-test (parámetro individual, modelo con EA) |
| **Ha₁ᵦ** | β(SE→IE) > 0 (cuando EA está en el modelo) | La autoeficacia tiene efecto positivo significativo, independiente de actitud | t-test unilateral p < .05 |

**Nota:** Se enfatiza "cuando EA está en el modelo" para subrayar que es un efecto parcial/independiente.

---

## 5. Estructura del Modelo de Regresión y Dónde Se Testean las Hipótesis

```
MODELO BASE (H1a, H1b):
IE = β₀ + β₁(EA) + β₂(SE) + β₃(EW) + ε

MODELO AMPLIADO (H1):
IE = β₀ + β₁(EA) + β₂(SE) + β₃(EW) + β₄(FK) + β₅(FL) + ε

MODELO CON MODERACIÓN (H2):
IE = β₀ + β₁(EA) + β₂(SE) + β₃(EW) 
     + β₄(FK) + β₅(FL)
     + β₆(U-D) + β₇(U-AS) + β₈(LC)
     + β₉(FK × U-D) + β₁₀(FK × U-AS) + β₁₁(FK × LC)
     + β₁₂(FL × U-D) + β₁₃(FL × U-AS) + β₁₄(FL × LC)
     + ε

VD: IE (SCORE_EI, α=0.960)
VI proxy: FK (α=0.933), FL (α=0.868)
VM: U-D (α=0.912), U-AS (α=0.916), LC (α=0.616⚠️)
Control: EA (α=0.920), SE (α=0.948), EW (α=0.920)
```

**¿Dónde se testea cada hipótesis?**
- **H₀₁ᵃ, Ha₁ᵃ:** Modelo Base — t-test para β₁
- **H₀₁ᵇ, Ha₁ᵇ:** Modelo Base — t-test para β₂
- **H₀₁, Ha₁:** Modelo Ampliado — t-test para β₄, β₅ (o prueba F conjunta)
- **H₀₂, Ha₂:** Modelo con Moderación vs Modelo Ampliado — ΔR² y t-test para β₉–β₁₄

---

## 6. Cambios Propuestos: Qué Se Modifica

### 6.1 Capítulo 1 — Sección 1.8 (Hipótesis)

**Cambios:**
1. Mantener la formulación narrativa/conceptual (H1, H2, H1a, H1b) como está
2. Agregar DESPUÉS una tabla con formulación estadística (H₀ y Ha)
3. Agregar una nota sobre cómo se testearán en el análisis (regresión)

**Estructura nueva de 1.8:**
```
## 1.8. Hipótesis

[Párrafo introductorio actual — sin cambios]

[Párrafos con H1, H2, H1a, H1b narrativas — sin cambios]

---

### 1.8.1. Formulación Estadística de Hipótesis (NEW)

[Tabla con H₀/Ha en notación estadística]

### 1.8.2. Especificación de Análisis (NEW)

[Párrafo explicando cómo se testean: regresión múltiple, análisis de moderación, etc.]
```

---

### 6.2 Matriz de Operacionalización (markdown_from_excel)

**Archivo:** `Matriz_Operacionalizacion_Variables_DBA-1_Hipótesis_y_Consistencia.md`

**Cambios:**
1. Agregar H₀ junto a H1 y H2 existentes
2. Agregar notación estadística (β, direccionalidad)
3. Columna nueva: "Testeable mediante"

---

## 7. Verificación de Coherencia: Matriz de Consistencia

| Componente | ¿Alineado? | Observación |
|-----------|-----------|------------|
| Pregunta de investigación | ✅ | 5 preguntas cubren los 5 objetivos y las 4 hipótesis |
| Objetivos especificados | ✅ | OE1–OE5 van de descriptivo a analítico a propositivo |
| Hipótesis formuladas | ✅ (Con mejora) | 4 hipótesis propuestas, ahora con H₀/Ha |
| Variables operacionalizadas | ✅ | VD, VI, VM, Control definidas con escalas y α |
| Análisis estadístico especificado | ⚠️ Parcial | Propuesto arriba; debe confirmarse en Cap. 3 |
| Muestra y dataset | ✅ | N=540, ALBA 2025, Zenodo DOI presente |
| Tipo de estudio | ✅ | Correlacional transversal declarado |
| Diseño mixto (QUAN→qual) | ✅ | Componente cuali pendiente de especificación |

**Síntesis:** Coherencia robusta. Las mejoras son refinamiento, no cambio fundamental.

---

## 8. Deliverables y Archivos a Modificar

| # | Archivo | Tipo | Acción | Urgencia |
|---|---------|------|--------|----------|
| 1 | `docs/02_cap1_proyeccion_investigacion/01_capitulo_1.md` | .md | Agregar secciones 1.8.1 y 1.8.2 con tabla H₀/Ha | 🔴 Alta |
| 2 | `docs/02_cap1_proyeccion_investigacion/Capitulo_1_Proyeccion_Investigacion.docx` | .docx | Regenerar con nuevas secciones 1.8.1–1.8.2 | 🔴 Alta |
| 3 | `docs/04_cap3_metodologia_resultados/markdown_from_excel/Matriz_Operacionalizacion_Variables_DBA-1_Hipótesis_y_Consistencia.md` | .md | Agregar H₀ y notación estadística | 🟡 Media |
| 4 | `MEMORY.md` | .md | Guardar decisión: adopción de H₀/Ha para coherencia estadística | 🟢 Baja |
| 5 | `quality_reports/plans/2026-04-18_hipotesis-nulas-coherencia-integral.md` | .md | Este plan (guardar después de aprobación) | 🟢 Baja |

---

## 9. Estimación de Esfuerzo y Riesgos

| Aspecto | Estimación | Notas |
|---------|-----------|--------|
| **Tiempo de ejecución** | 2–3 horas | Escritura de tabla de H₀/Ha, ajustes al Cap. 1, regenerar .docx |
| **Riesgo de cambio de rumbo** | Bajo | Las hipótesis narrativas NO cambian, solo se agregan formalizaciones |
| **Impacto en Cap. 2** | Ninguno | El marco TCP y estado del arte se escriben igual |
| **Impacto en Cap. 3** | Medio | La operacionalización se clarifica; el análisis estadístico es más preciso |
| **Testabilidad estadística** | Completa | Todas las H₀/Ha son falsables y estadísticamente testables |

---

## 10. Decisiones a Tomar

**Pregunta 1: ¿Adoptar H₀/Ha para todas las hipótesis?**  
Recomendación: **SÍ**. Es estándar en estudios cuantitativos.

**Pregunta 2: ¿Mantener la formulación narrativa original?**  
Recomendación: **SÍ**. La narrativa es clara para el lector. La formulación estadística es complementaria.

**Pregunta 3: ¿Usar direccionalidad unilateral (β > 0) o bilateral (β ≠ 0)?**  
Recomendación: **Unilateral (β > 0)** porque la teoría TCP sustenta efectos positivos. Se especifica en cada caso.

**Pregunta 4: ¿Cuándo testear H2 (moderación)?**  
Recomendación: **Después de confirmar H1**. Si FK y FL no tienen efecto significativo, la moderación no tiene sentido testear.

---

## 11. Cronograma Propuesto

| Paso | Tarea | Responsable | Plazo |
|------|-------|-------------|--------|
| 1 | Revisar este plan con investigador | Investigador | Hoy |
| 2 | Redactar secciones 1.8.1–1.8.2 en Cap. 1 Markdown | Claude (writer) | Hoy |
| 3 | Revisar redacción con coherencia estadística | Claude (strategist-critic) | Hoy |
| 4 | Regenerar .docx del Cap. 1 | Claude (docx skill) | Hoy |
| 5 | Actualizar matriz de operacionalización | Claude + investigador | Hoy o mañana |
| 6 | Guardar plan en disk y commit a git | Investigador | Hoy |
| 7 | Iniciar Cap. 2 (Fundamentos) con H₀/Ha en mente | Claude (writer) | Próxima sesión |

---

## 12. Aprobación

Este plan requiere aprobación del investigador antes de proceder.

**¿Está de acuerdo con los cambios propuestos?**
- [ ] Sí, proceder
- [ ] Sí, con ajustes (especificar abajo)
- [ ] No, rechazar y explicar alternativa

**Comentarios del investigador:**

---

**Fin del Plan**
