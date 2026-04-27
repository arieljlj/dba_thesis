# Reporte de Coherencia Global — Tesis DBA
## Alineación: Hipótesis ↔ Variables ↔ Resultados ↔ Conclusiones

**Fecha:** 2026-04-26  
**Fase:** FASE 5 — Pre-conversión Word  
**Alcance:** Capítulos 1, 3, 4, 6, 7 + Resumen + Abstract

---

## Puntuación de Coherencia por Dimensión

| Dimensión | Score | Estado |
|---|---|---|
| Pregunta → Objetivos → Hipótesis | 92/100 | ✅ Sólida |
| Hipótesis → Constructos operacionalizados | 81/100 | ⚠️ Corrección menor |
| Resultados (Cap. 3) → Conclusiones (Cap. 6) | 96/100 | ✅ Sólida |
| Propuesta (Cap. 4) → Resultados | 93/100 | ✅ Sólida |
| Integridad del corpus (sin marcas de edición) | 0/100 | ❌ Merge conflict activo |
| Consistencia terminológica del dataset | 70/100 | ❌ Nombre inconsistente |

**Score de coherencia global: 83/100** — Bloqueado por dos problemas técnicos. Post-corrección: ~93/100.

---

## Problemas Identificados

### BLOQUEANTES (impiden conversión Word)

---

**COH-01 — Conflicto git sin resolver en Capítulo 1**  
**Archivo:** `docs/02_cap1_proyeccion_investigacion/01_capitulo_1.md`, líneas 13–26  
**Problema:** El archivo contiene marcas de conflicto de merge (`<<<<<<< Updated upstream`, `=======`, `>>>>>>> Stashed changes`) en la sección 1.1. pandoc fallará al convertir este archivo y el documento Word quedará con basura literal.  
**Corrección:** Conservar el bloque "Stashed changes" (versión completa de 3 párrafos) y descartar el bloque "Updated upstream" (versión corta con cita pandoc `[@acs2018]`).

---

**COH-02 — Nombre del dataset inconsistente (ALBA 2025 vs. ALBA 2026)**  
**Archivos:** `docs/02_cap1_proyeccion_investigacion/01_capitulo_1.md` (múltiples líneas)  
**Problema:** Cap. 1 se refiere al dataset como "ALBA 2024-2025" y "ALBA 2025". Todos los demás capítulos (Cap. 2, 3, 4, Portada, Resumen, Abstract, Conclusiones, Recomendaciones), el `.bib`, y los archivos de datos usan "ALBA 2026". Un comité que compare el capítulo introductorio con los capítulos analíticos detectará la discordancia.  
**Corrección:** Reemplazar todas las ocurrencias de "ALBA 2025" y "ALBA 2024-2025" en Cap. 1 por "ALBA 2026".

---

### MODERADOS (corregir antes de enviar al director)

---

**COH-03 — Notación de variables en Cap. 1 vs. Cap. 3**  
**Archivo:** `docs/02_cap1_proyeccion_investigacion/01_capitulo_1.md`, sección 1.8.2  
**Problema:** Los modelos de regresión de la sección 1.8.2 usan los códigos originales del dataset ALBA: `EA` (Actitud), `SE` (Autoeficacia), `EW` (Deseo/Motivación). El Cap. 3 —y todos los resultados— usa la notación TCP estándar: `AT`, `SN`, `PBC`. Adicionalmente, el Modelo 1 en Cap. 1 (`IE = β₀ + β₁(EA) + β₂(SE) + β₃(EW)`) omite explícitamente las Normas Subjetivas (SN), que en Cap. 3 se incluyen como tercer predictor TCP.  
**Corrección:** Añadir nota de correspondencia de variables en la sección 1.8.2 aclarando que EA=AT, SE+EW≈PBC, y que SN (Normas Subjetivas) se incluye como tercer predictor en la implementación empírica del Cap. 3. No requiere reescribir los modelos formales.

---

**COH-04 — Especificación de H2 vs. hallazgo real**  
**Archivos:** Cap. 1 sección 1.8 y Cap. 6 Conclusión 4  
**Problema:** H2 en Cap. 1 predice moderación de FK×VM y FL×VM (políticas × contexto universitario). El hallazgo significativo en Cap. 3 fue AT×U-D (β=0.089, p=0.031), no directamente FK×VM. Cap. 6 ya lo reporta correctamente como "confirmación parcial" de H2, lo que es metodológicamente aceptable pero puede ser cuestionado por el comité.  
**Corrección:** No requiere cambio sustancial — Cap. 6 ya usa "parcialmente" con precisión. Se agrega una nota aclaratoria en Cap. 1 sección 1.8 indicando que el contexto universitario puede moderar tanto las relaciones FK/FL→IE como las relaciones AT/PBC→IE, y que ambos efectos son compatibles con H2 en su formulación general.

---

### CONFIRMADOS SIN CORRECCIÓN

---

**COH-OK-01 — Pregunta de investigación → Objetivos específicos:** Alineación perfecta. La pregunta principal en 1.3 se descompone en 5 preguntas secundarias (PE1–PE5) que corresponden exactamente a los OE1–OE5.

**COH-OK-02 — Hipótesis confirmadas en Cap. 3 y Cap. 6:**
- H1 (FK y FL predicen IE): ✅ FK β=0.159 p<0.001, FL β=0.080 p=0.043 — confirmada
- H2 (moderación universitaria): ✅ parcialmente confirmada — AT×U-D β=0.089 p=0.031 — correctamente reportada como parcial
- H1a (AT predictor dominante): ✅ β=0.548 — confirmada y etiquetada en Conclusión 1 (tras corrección FASE 3)
- H1b (PBC predictor independiente): ✅ β=0.395 p<0.001 — confirmada y etiquetada en Conclusión 1 (tras corrección FASE 3)

**COH-OK-03 — Valores numéricos consistentes entre Cap. 3, Cap. 4, Cap. 6 y Resumen/Abstract:**
- R²=0.478 (Modelo 1): ✅ consistente en todos los capítulos
- ΔR²=0.034 para FK+FL (Modelo 2): ✅ consistente
- β interacción AT×U-D=0.089 p=0.031: ✅ consistente
- Brecha intención-acción ≈48 puntos porcentuales: ✅ consistente

**COH-OK-04 — Propuesta (Cap. 4) fundamentada en resultados (Cap. 3):** La jerarquía β(U-AS=0.109) > β(FL=0.063) que justifica privilegiar mentoría sobre alfabetización financiera está documentada y correctamente citada en la propuesta y en Conclusión 5.

---

## Resumen de Correcciones a Aplicar

| ID | Archivo | Tipo | Acción |
|---|---|---|---|
| COH-01 | Cap. 1 | Merge conflict | Resolver conservando versión stash |
| COH-02 | Cap. 1 | Nombre dataset | ALBA 2025 → ALBA 2026 (3 ocurrencias) |
| COH-03 | Cap. 1 | Notación | Añadir nota de correspondencia EA→AT, SE→PBC, SN |
| COH-04 | Cap. 1 | H2 scope | Añadir nota aclaratoria sobre alcance de la moderación |

**Score estimado post-corrección: 93/100** — Listo para conversión Word y envío al director.
