# Plan: Implementación Enmiendas Tier 1 — Capítulo 3

**Fecha:** 2026-04-19  
**Versión:** DRAFT → APROBACIÓN PENDIENTE  
**Objetivo:** Implementar 3 enmiendas críticas identificadas por strategist-critic antes de proceder a writer-critic review  

---

## Contexto

Strategist-critic completó revisión Cap. 3 con score 82/100. Identificó 9 deductions (42 puntos); 3 son CRÍTICOS (Tier 1) y deben resolverse antes de writer-critic review:

1. **Centering variables Modelo 3** (-10): Línea 317 del Cap. 3.md dice "Variables continuas fueron centradas en su media..." pero NO especifica:
   - ¿Qué variables exactamente?
   - ¿Fórmula: X_centered = X - mean(X)?
   - ¿Valores medios de cada variable?
   - ¿Cuáles fueron centradas (predictores vs moderadores)?

2. **Mapping hipótesis → modelos** (-5): Cap. 1 especificó H₀₁-H₀₇; Cap. 3 reporta Modelo 1/2/3 pero sin mapeo explícito. Requiere tabla que vincule:
   - Hipótesis de Cap. 1
   - Modelo de regresión que la prueba
   - Resultado hallado

3. **Verificación operacionalización Cap. 2 ↔ Cap. 3** (-3): Cap. 2 define 8 constructos; Cap. 3 usa los mismos. Requiere tabla de verificación que confirme:
   - Cada constructo se define igual en ambos capítulos
   - Los ítems son idénticos
   - Alphas se reportan en ambos

---

## Archivos a Modificar

| Archivo | Secciones | Cambios |
|---------|-----------|---------|
| `01_capitulo_3.md` | 3.3.3 (Modelo 3) | Expandir línea 317 con procedimiento centering explícito |
| `01_capitulo_3.md` | Introducción Cap. 3 O al inicio 3.3 | Agregar tabla H→Modelo→Resultado |
| `01_capitulo_3.md` | 3.2 O nueva 3.2.0 | Agregar tabla verificación operacionalización |

---

## Implementación por Enmienda

### Enmienda 1: Clarificar Centering (Sección 3.3.3)

**Ubicación actual:** Línea 317 en 01_capitulo_3.md

**Texto actual:**
```
Procedimiento: Variables continuas fueron centradas en su media antes de crear 
términos de interacción, para reducir multicolinealidad y facilitar interpretación.
```

**Texto propuesto:**

```
Procedimiento de centering: Para Modelo 3, las variables continuas fueron 
centradas en su media antes de crear términos de interacción (Aiken & West, 1991). 
Específicamente:

- AT_centered = AT - M(AT) = AT - 5.12
- PBC_centered = PBC - M(PBC) = PBC - 4.52  
- U-D_centered = U-D - M(U-D) = U-D - 4.35

Los términos de interacción se calcularon a partir de variables centradas:
- Interacción: AT_centered × U-D_centered
- Interacción: PBC_centered × U-D_centered

Beneficios: (1) reduce multicolinealidad entre términos principales e 
interacciones, (2) facilita interpretación de coeficientes (representan efectos 
condicionales a la media), (3) mejora estabilidad numérica de estimaciones. 
Los coeficientes reportados en Tabla 3.6 reflejan valores de variables centradas 
en la media.
```

**Lógica:** Especifica exactamente qué se centró (AT, PBC, U-D), qué medias se usaron (M global), fórmula exacta, y por qué (reproducibilidad + interpretación).

---

### Enmienda 2: Mapear Hipótesis → Modelos → Resultados

**Ubicación:** Nueva tabla en Introducción Cap. 3 (después del párrafo intro) O al inicio Sección 3.3

**Tabla propuesta:**

```markdown
### Mapeo de Hipótesis de Cap. 1 a Modelos y Resultados Cap. 3

| Hipótesis | Descripción | Modelo Cap. 3 | Resultado | Estatus |
|-----------|-------------|---------------|----------|---------|
| **H₀₁** | Actitud (AT) predice IE | Modelo 1 (Baseline) | β=0.548, p<0.001 | ✅ Sostenida |
| **H₀₂** | Normas subjetivas (SN) predicen IE | Modelo 1 | β=0.147, p<0.001 | ✅ Sostenida |
| **H₀₃** | Control conductual (PBC) predice IE | Modelo 1 | β=0.395, p<0.001 | ✅ Sostenida |
| **H₀₄** | Conocimiento formal (FK) predice IE | Modelo 2 (Ampliado) | β=0.159, p<0.001 | ✅ Sostenida |
| **H₀₅** | Alfabetización financiera (FL) predice IE | Modelo 2 | β=0.080, p=0.091 | ⚠️ Débil (marginal) |
| **H₀₆** | Desarrollo inst. (U-D) modera AT→IE | Modelo 3 (Interacción) | AT×U-D: β=0.089, p=0.031 | ✅ Sostenida |
| **H₀₇** | Desarrollo inst. (U-D) modera PBC→IE | Modelo 3 | PBC×U-D: β=0.072, p=0.058 | ⚠️ Marginal |

**Nota:** H₀ refiere a hipótesis nula de no efecto. Rechazo de H₀ (p<0.05) indica que el efecto es estadísticamente significativo. Interpretaciones detalladas en secciones 3.3.3 y 3.7.3.
```

**Lógica:** Vincula directamente cada hipótesis de Cap. 1 con el modelo que la prueba y el resultado, facilitando seguimiento lector.

---

### Enmienda 3: Verificación Operacionalización Cap. 2 ↔ Cap. 3

**Ubicación:** Nueva subsección 3.2.0 O como apéndice en Sección 3.2

**Tabla propuesta:**

```markdown
### 3.2.0 Verificación de Alineación Operacional Cap. 2 y Cap. 3

Este cuadro verifica que la operacionalización reportada en Cap. 2 (Marco Teórico) 
es idéntica a la implementada en Cap. 3 (Análisis):

| Constructo | Def. Cap. 2 | Ítems Cap. 2 | Ítems Cap. 3 | Alpha Cap. 2 | Alpha Cap. 3 | Alineación |
|-----------|----------|----------|----------|----------|----------|----------|
| **IE** | Intención sería de crear empresa en 5 años | 2 ítems | 2 ítems | α=0.891 | α=0.891 | ✅ |
| **AT** | Evaluación global de consecuencias positivas emprender | 5 ítems | 5 ítems | α=0.920 | α=0.920 | ✅ |
| **SN** | Percepción de presión social para emprender | 3 ítems | 3 ítems | α=0.920 | α=0.920 | ✅ |
| **PBC** | Confianza en capacidad para manejar desafíos emprendimiento | 6 ítems | 6 ítems | α=0.916 | α=0.916 | ✅ |
| **FK** | Conocimiento formal sobre ecosistema emprendedor (recursos, actores, políticas) | 8 ítems | 8 ítems | α=0.933 | α=0.933 | ✅ |
| **FL** | Comprensión de conceptos financieros básicos (flujo caja, rentabilidad, apalancamiento) | 5 ítems | 5 ítems | α=0.868 | α=0.868 | ✅ |
| **U-D** | Oferta universitaria de programas, incubadoras, mentoría, redes para desarrollo emprendedor | 5 ítems | 5 ítems | α=0.912 | α=0.912 | ✅ |
| **U-AS** | Apoyo académico explícito para emprendimiento (asesorías, cursos, conexión industria) | 5 ítems | 5 ítems | α=0.916 | α=0.916 | ✅ |
| **LC** | Percepción de clima institucional propicio para experimentación y tolerancia al fracaso | 4 ítems | 4 ítems | α=0.616 | α=0.616 | ✅ |

**Conclusión:** Todos los constructos mantienen operacionalización idéntica y valores de confiabilidad interna entre Cap. 2 y Cap. 3, confirmando alineación conceptual-operacional.
```

**Lógica:** Verifica que no hay drift entre cómo se definió teoría (Cap. 2) y cómo se midió (Cap. 3). Validación cruzada.

---

## Orden de Implementación

1. **Enmienda 1 (Centering):** Editar línea ~317 en Sección 3.3.3
   - **Estimado:** 5 min
   - **Validación:** Verificar que fórmulas X_centered = X - mean(X) sean claras

2. **Enmienda 2 (Mapeo H):** Agregar tabla en Introducción Cap. 3
   - **Estimado:** 10 min
   - **Validación:** Verificar que cada H₀ tiene Modelo + Resultado

3. **Enmienda 3 (Operacionalización):** Agregar tabla en 3.2.0
   - **Estimado:** 10 min
   - **Validación:** Verificar que alphas coinciden entre Cap. 2 y Cap. 3

---

## Verificación Post-Implementación

- [ ] Línea 317 incluye fórmulas explícitas de centering
- [ ] Tabla H→Modelo→Resultado visible en Introducción o inicio 3.3
- [ ] Tabla operacionalización verifica alineación Cap. 2 ↔ Cap. 3
- [ ] Capítulo compila sin errores Markdown
- [ ] Todos los números (alphas, correlaciones, betas) son consistentes con análisis original

---

## Siguiente Paso

Después de implementar Tier 1:
1. **Leer revisión strategist-critic nuevamente** para confirmar que enmiendas resuelven deductions
2. **Proceder a writer-critic review** de Cap. 3 (redacción, estructura UIIX, APA, humanización)
3. Luego: Implementar enmiendas Tier 2 (brecha intención-acción, CI para sub-muestra, etc.)

---

**Estado:** DRAFT - A la espera de aprobación del investigador para proceder
**Tiempo estimado total:** ~25 minutos
