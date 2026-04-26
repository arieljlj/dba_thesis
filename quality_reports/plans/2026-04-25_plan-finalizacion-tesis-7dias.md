# Plan de Finalización — Tesis DBA en 7 Días
**Candidato:** Jorge Ariel Loaiza Loaiza  
**Plazo:** 2026-04-25 → 2026-05-02 (7 días calendario)  
**Objetivo:** Defensa doctoral ante comité con documento score ≥90 (global) y todos componentes ≥80  
**Estrategia:** Paralelo máximo, Tier 1 bloqueante, Tier 2 selecta de alta prioridad  

---

## 1. Mapa de Dependencias y Secuencia Crítica

```
HITO 1: Cap. 2 writer-critic aprobado (≥80)
    ↓
HITO 2: Cap. 3 Tier 1-2 enmiendas completas (≥90)
    ↓
HITO 3: Cap. 4 Tier 2 enmiendas completas (≥90)
    ↓
PARALELO (Días 4-5):
    Cap. 5 (Conclusiones) ← depende de Cap. 3-4
    Cap. 6 (Recomendaciones) ← depende de Cap. 4
    Portada + Resumen/Abstract ← depende de Caps. 1-6
    Anexos ← independiente (puede iniciar Día 1)
    ↓
HITO 4: Word UIIX compilado y formateado (Día 6)
    ↓
HITO 5: Pre-defensa review comité + ajustes finales (Día 6-7)
    ↓
DEFENSA DOCTORAL (Día 7 PM o Día 8)
```

---

## 2. Desglose por Día

### **DÍA 1 (Viernes 26 Abril) — Foundation: Cap. 2 + Anexos**

**Mañana: Writer-critic review Cap. 2**
- **Tarea:** Ejecutar writer-critic review de Cap. 2 (`docs/03_cap2_fundamentos_teoricos/02_capitulo_2.md`)
- **Severidad:** Media-alta (Fase Fundamentos: "constructiva-media")
- **Checklist:** 
  - [ ] Estructura UIIX (Sentence case títulos, numeración)
  - [ ] APA 7ª (referencias completas, citación inline, formato)
  - [ ] Humanización (variar estructura oraciones, evitar copula avoidance, tono académico natural)
  - [ ] Coherencia Cap. 2 ↔ Cap. 3 (operacionalización, marcos teóricos)
- **Output:** Reporte de review con Tier 1 + Tier 2 scored (target: ≥80 después de Tier 1)
- **Tiempo estimado:** 2.5 horas

**Tarde: Tier 1 enmiendas Cap. 2**
- **Tarea:** Implementar enmiendas Tier 1 (bloqueantes) de writer-critic Cap. 2
- **Típico:** Referencias faltantes, formato tablas, inconsistencias APA, transiciones
- **Time-box:** 2 horas
- **Output:** Cap. 2 corregido, listo para Tier 2

**Noche: Iniciar Anexos**
- **Paralelo:** Mientras se procesan enmiendas Cap. 2, iniciar redacción de Anexos
- **Contenido anexos:**
  - Apéndice A: Cuestionario ALBA (ES + EN) — **ya disponible** en `code/instruments/`
  - Apéndice B: Protocolo codificación cualitativa completo — **extraer de Cap. 3**
  - Apéndice C: Tablas complementarias (correlaciones completas, análisis por región)
  - Apéndice D: Transcripciones video YouTube seleccionadas (5-10 fragmentos clave)
- **Time-box:** 1.5 horas (compilación, no redacción nueva)
- **Output:** Borrador anexos Markdown

**Estado al cierre Día 1:**
- ✅ Cap. 2 Tier 1 enmiendas implementadas (score: 83–86/100 esperado)
- ✅ Plan de Tier 2 Cap. 2 documentado
- ⏳ Anexos: borrador 30% completo

---

### **DÍA 2 (Sábado 27 Abril) — Convergencia Cap. 2-3**

**Mañana: Tier 2 enmiendas Cap. 2**
- **Tarea:** Implementar Tier 2 selectas (humanización, APA fino, transiciones claras)
- **No aplica:** Tier 2 menor (formato .docx, notas tablas opcionales) — post-defensa
- **Target score:** 88–90/100
- **Time-box:** 2 horas
- **Output:** Cap. 2 finalized (≥88 esperado)

**Mediodía: Commit Cap. 2 + Actualizar research journal**

**Tarde: Completar Tier 1-2 Cap. 3 writer-critic si falta**
- **Verificación:** ¿Cap. 3 Tier 1-2 writer-critic fue completado en sesión anterior?
  - Si NO: ejecutar ahora (writer-critic review → implementar Tier 1 → Tier 2 selectas)
  - Si SÍ: saltar a verificación final
- **Target score Cap. 3:** ≥90/100
- **Time-box:** 3-4 horas si es necesario, 30 min si ya completado

**Noche: Continuación Anexos**
- Terminar compilación Apéndices A-D
- Iniciar Apéndice E: Matriz de triangulación cuantitativo-cualitativo completa
- **Time-box:** 1.5 horas

**Estado al cierre Día 2:**
- ✅ Cap. 2: ≥88/100, listo comité
- ✅ Cap. 3: Verificado ≥90/100
- ⏳ Anexos: 60% completo

---

### **DÍA 3 (Domingo 28 Abril) — Tier 2 Cap. 4 + Conclusiones Iniciales**

**Mañana: Tier 2 enmiendas Cap. 4**
- **Contexto:** Cap. 4 ya tiene 89.5/100 (Tier 1 completo)
- **Tier 2 selectas:** Solo las que suben score rápidamente:
  1. Humanización: estructura variada, tono menos prescriptivo en propuesta (30 min)
  2. APA fino: verificar todas referencias políticas colombianas formales (30 min)
  3. Coherencia Cap. 3 ↔ 4: tabla mapeo resultados → propuesta (45 min)
- **No aplica:** Tier 2 menor (refinamiento editorial) — post-defensa
- **Target score:** 92–94/100
- **Time-box:** 2 horas
- **Output:** Cap. 4 pulido, comité-ready premium

**Mediodía: Commit Cap. 4**

**Tarde: Writer — Redacción Cap. 5 (Conclusiones)**
- **Estructura recomendada (1,500–2,000 palabras):**
  1. **5.1 Síntesis de hallazgos:** Resumen breve resultados Cap. 3 (cuantitativo + cualitativo)
  2. **5.2 Contribuciones teóricas:** 
     - Ampliación de TCP: contexto universitario como moderador
     - Evidencia sobre linaje intención-acción
     - Heterogeneidad regional: Colombia específico
  3. **5.3 Contribuciones prácticas:**
     - Modelo de intermediación local (Cap. 4) fundamentado empíricamente
     - Implicaciones para política pública nacional vs. local
  4. **5.4 Limitaciones y oportunidades:**
     - Transversal, N=41 Colombia, auto-reporte
     - Oportunidades: estudios longitudinales, RCT, extensión a otras regiones
  5. **5.5 Reflexiones finales:** Una reflexión personal sobre implicaciones para ecosistema colombiano

- **Guía de redacción:**
  - Tone: Académico reflexivo, no defensivo
  - Evitar: Resumir resultados (ya está en Cap. 3)
  - Enfatizar: Cambios teóricos, utilidad práctica, preguntas abiertas
  - Humanizar: Conectar con Cap. 1 (pregunta original), mostrar arco investigativo

- **Time-box:** 3 horas
- **Output:** Cap. 5 borrador completo ≥1,500 palabras

**Noche: Continuación Anexos**
- Completar Apéndice E
- Iniciar Apéndice F: Listado de códigos cualitativos + ejemplos (10-15 fragmentos clave)
- **Time-box:** 1 hora

**Estado al cierre Día 3:**
- ✅ Cap. 4: 92–94/100, premium comité-ready
- ✅ Cap. 5: Borrador completo, pendiente writer-critic
- ⏳ Anexos: 75% completo

---

### **DÍA 4 (Lunes 29 Abril) — Redacción paralela + Revisión Cap. 5**

**Mañana: Writer-critic review Cap. 5**
- **Tarea:** Revisar Cap. 5 en paralelo mientras el escritor redacta Cap. 6
- **Severidad:** Media (Fase Cierre: reflexiva, no cuantitativa)
- **Checklist:**
  - [ ] Síntesis clara de hallazgos
  - [ ] Contribuciones explícitas (teórica + práctica)
  - [ ] Limitaciones honestas
  - [ ] Redacción coherente, humanizada
- **Target score:** ≥85/100 (Tier 1 después, Tier 2 post-defensa)
- **Time-box:** 1.5 horas
- **Output:** Reporte writer-critic Cap. 5

**Mañana-Tarde (PARALELO): Writer — Redacción Cap. 6 (Recomendaciones)**
- **Estructura (1,500–2,000 palabras):**
  1. **6.1 Recomendaciones para política pública nacional:**
     - Bifurcación emprendimiento oportunidad vs. necesidad (Ley 1014 vs. nueva rama)
     - Financiamiento de intermediación local (universidades como puentes)
     - Evaluación nacional de intención vs. acción (datos longitudinales)
  2. **6.2 Recomendaciones para universidades técnicas:**
     - Modelo de mentoría estructurada (protocolo Cap. 4)
     - Integración con currículo (no solo actividad complementaria)
     - Evaluación de contexto universitario (U-D, U-AS, LC)
  3. **6.3 Recomendaciones para investigación futura:**
     - RCT con diseño randomizado (mentoría vs. control)
     - Seguimiento longitudinal 5 años post-egreso
     - Análisis heterogeneidad regional exhaustivo
     - Mecánica del fracaso: qué hace que post-fracaso estudiantes reintenten
  4. **6.4 Reflexión sobre brecha intención-acción:**
     - No es problema que se resuelva con más motivación
     - Requiere arquitectura: mentoría + redes + legitimidad
     - Rol de políticas públicas: enabler, no creador de oportunidades

- **Time-box:** 3 horas (paralelo con writer-critic Cap. 5)
- **Output:** Cap. 6 borrador completo ≥1,500 palabras

**Tarde: Tier 1 enmiendas Cap. 5 + Implementación**
- Aplicar recomendaciones writer-critic Cap. 5
- **Time-box:** 1 hora
- **Output:** Cap. 5 mejorado (target: 88–90/100)

**Noche: Anexos finales**
- Completar Apéndices F-G
- Compilar índice de anexos
- **Time-box:** 1 hora

**Estado al cierre Día 4:**
- ✅ Cap. 5: ≥88/100
- ✅ Cap. 6: Borrador completo, pendiente revisión rápida
- ✅ Anexos: 90% completo

---

### **DÍA 5 (Martes 30 Abril) — Portada/Resumen + Writer-critic Cap. 6 + Compilación Inicial**

**Mañana: Redacción Portada + Resumen/Abstract**
- **Portada UIIX:** Formato estándar (título, candidato, director, institución, fecha)
- **Resumen ejecutivo (ES):** 200–300 palabras
  - Pregunta, método (N=540 cuantitativo + análisis cualitativo), hallazgos clave (TCP predice IE, contexto universitario modera, brecha intención-acción explica)
  - Conclusión: Mentoría local > capital
- **Abstract (EN):** Traducción equilibrada del resumen
- **Time-box:** 1.5 horas
- **Output:** Portada + Resumen/Abstract Markdown

**Mediodía: Writer-critic review Cap. 6 (rapid review)**
- **Scope:** Rápida (verificar coherencia, claridad, alineación con Cap. 4)
- **Target score:** ≥85/100
- **Time-box:** 45 min
- **Output:** Reporte crítico Cap. 6

**Tarde: Tier 1 enmiendas Cap. 6 + Compilación inicial**
- Aplicar enmiendas writer-critic
- **Time-box:** 45 min enmiendas

**Tarde: Iniciación compilación Word UIIX**
- Pasar todos Mds a Word (.docx):
  - Portada
  - Resumen/Abstract
  - Cap. 1-6
  - Anexos (A-G compilados)
- Aplicar formato UIIX:
  - Tipografía: Times New Roman 12pt
  - Interlineado: 1.5
  - Márgenes: 4cm izq, 2.5cm otros
  - Numeración: Automática superior derecha
  - Estilos: Heading 1 (capítulo), Heading 2 (sección)
- **Time-box:** 2 horas (herramientas de conversión Md→Word pueden aceleran)
- **Output:** Documento Word preliminar (sin revisión comité aún)

**Noche: Revisión final Anexos**
- Verificar completitud anexos A-G
- Compilar tabla de contenidos detallada
- **Time-box:** 30 min

**Estado al cierre Día 5:**
- ✅ Cap. 6: ≥88/100
- ✅ Portada + Resumen: Completados
- ✅ Anexos: 100% compilados
- ✅ Word UIIX: Versión preliminar compilada
- ⏳ Calidad agregada: ~88–89/100 (falta writer-critic verificación final)

---

### **DÍA 6 (Miércoles 01 Mayo) — Pre-defensa Review + Ajustes Finales**

**Mañana: Writer-critic review FINAL de documento completo**
- **Tarea:** Estratega-crítico + writer-crítico harán revisión rápida de coherencia global
- **Scope:** 
  - Coherencia Cap. 1 (pregunta) → Cap. 5-6 (conclusiones, recomendaciones)
  - Consistencia de notación, citas, formato
  - Verificación final números (¿coinciden Cap. 3 ↔ Cap. 4?)
  - APA verificación final (referencias completas, citas inline)
- **Target:** Identificar Tier 1 bloqueantes solo (Tier 2 post-defensa)
- **Time-box:** 2 horas
- **Output:** Reporte crítico final (gap-list de Tier 1 items)

**Mediodía-Tarde: Implementar Tier 1 finales + Formateo Word**
- Aplicar cualquier enmienda Tier 1 identificada
- Formateo Word final:
  - Tabla de contenidos automática
  - Índice de figuras/tablas
  - Referencias formateadas automáticamente (estilos Word APA)
  - Page breaks entre capítulos
  - Números de página correctos
- **Time-box:** 2.5 horas
- **Output:** Documento Word final formateado, ≥90/100 esperado

**Tarde: Exportar PDF para defensa**
- Exportar documento Word a PDF (preservar formato)
- Verificar renderizado PDF (tablas, figuras, paginación)
- **Time-box:** 30 min
- **Output:** PDF defensa-ready

**Tarde-Noche: Simulación de defensa (OPCIONAL pero recomendado)**
- Si hay tiempo: Jorge presenta Cap. 1-6 resumen (30-45 min)
- Preguntas de comité simuladas (anticipar preguntas sobre brecha intención-acción, validez metodológica, política pública)
- Refinar respuestas
- **Time-box:** 1.5 horas (opcional)

**Estado al cierre Día 6:**
- ✅ Documento Word UIIX compilado, formateado, ≥90/100
- ✅ PDF generado defensa-ready
- ✅ Revisión final completada
- ⏳ Ajustes mínimos completados

---

### **DÍA 7 (Jueves 02 Mayo) — Defensa Doctoral**

**Mañana: Revisión de notas + Ensayo discurso apertura**
- Preparar resumen 10–15 min de investigación para apertura
- Revisar preguntas anticipadas, respuestas clave
- **Time-box:** 1 hora

**Tarde: DEFENSA ante comité doctoral**
- Presentación: 20–30 min
- Preguntas comité: 30–45 min
- Deliberación: 15–30 min
- **Outcome esperado:** Aprobación con cambios menores (post-defensa)

---

## 3. Paralelos y Optimizaciones

### **Actividades que PUEDEN correr en paralelo (para ganar tiempo):**

| Paralelo | Responsabilidad | Duración | Ahorro |
|----------|---|---|---|
| Writer redacta Cap. 5 | Writer | Día 3 Tarde | Mientras writer-critic revisa Cap. 2 Tier 1 |
| Writer redacta Cap. 6 | Writer | Día 4 Tarde | Mientras writer-critic revisa Cap. 5 |
| Redacción Anexos | Asistente o Claude | Días 1–4 noches | Paralelo a enmiendas cuantitativas |
| Compilación Word | Asistente | Día 5 Tarde | Mientras writer hace tier 1 Cap. 6 |

### **Camino crítico (bottleneck):**
```
Cap. 2 writer-critic → enmiendas Tier 1 → Tier 2 (Día 1-2, 4 horas) = BLOQUEANTE
Cap. 5 redacción (3h) → writer-critic (1.5h) → enmiendas (1h) = BLOQUEANTE
Cap. 6 redacción (3h) → writer-critic rápida (45min) = BLOQUEANTE
Word compilación + revisión final (Día 5-6, 5 horas) = CRÍTICA
```

---

## 4. Umbrales de Calidad por Fase

| Componente | Tier 1 Target | Tier 2 Aplica | Comité Mín | Defensa Mín |
|-----------|---|---|---|---|
| Cap. 1 | ✅ 85/100 | N/A (completado) | ≥85 | ≥85 |
| Cap. 2 | ≥83 | ✅ Selecta (humanización, APA) | ≥88 | ≥88 |
| Cap. 3 | ✅ ≥88 | ✅ Selecta (redacción) | ≥90 | ≥90 |
| Cap. 4 | ✅ 89.5/100 | ✅ Selecta (humanización, APA) | ≥92 | ≥92 |
| Cap. 5 | ≥85 | Post-defensa | ≥88 | ≥88 |
| Cap. 6 | ≥85 | Post-defensa | ≥88 | ≥88 |
| **Global** | — | — | **≥90** | **≥92** |

---

## 5. Recursos y Herramientas

| Recurso | Usado en | Notas |
|---------|----------|-------|
| Claude (writer, writer-critic, strategist-critic) | Todos días | Enmiendas, revisiones críticas |
| Markdown → Word (Pandoc, docx Python library) | Día 5 | Conversión automática format |
| Git (commits diarios) | Cada hito | Auditoría, recuperación |
| Template UIIX Word | Día 5 | Aplicar estilos automáticos |
| PDF exporter (Word native o externa) | Día 6 | Generar PDF defensa |

---

## 6. Decisiones Críticas y Contingencias

### **Si Cap. 2 writer-critic score < 80:**
→ Escalar enmiendas Tier 2 a prioritario (Día 2 mañana antes de Cap. 3)

### **Si Cap. 3-4 writer-critic identifica enmiendas no anticipadas:**
→ Implementar Tier 1 solo (Tier 2 post-defensa; no hay tiempo)

### **Si Cap. 5-6 redacción se retrasa:**
→ Atrapar en paralelo: writer-critic revisa mientras writer termina redacción siguiente

### **Si Word compilación falla (formato corrupto, referencias rotas):**
→ Usar conversión Md→HTML→Word o hacer Word manual sección por sección (Día 6 mañana extend)

### **Si pre-defensa review (Día 6) revela issues Tier 1 sustanciales:**
→ Extender a Día 6 noche (preparación defensa se vuelve mínima)
→ Enfocarse en defensa oral (defendible incluso con pequeñas erratas)

---

## 7. Checklist de Validación al Finalizar

- [ ] **Cap. 1:** Score ≥85, coherencia pregunta-objetivos-hipótesis
- [ ] **Cap. 2:** Score ≥88, referencias APA completas, marcos teóricos alineados Cap. 3-4
- [ ] **Cap. 3:** Score ≥90, β valores coinciden exactamente donde se citan en Cap. 4
- [ ] **Cap. 4:** Score ≥92, linaje causal explícito, criterios mentoría operativos
- [ ] **Cap. 5:** Score ≥88, síntesis clara hallazgos, contribuciones explícitas
- [ ] **Cap. 6:** Score ≥88, recomendaciones fundamentadas en Cap. 3-4
- [ ] **Portada+Resumen:** Formato UIIX, resumen ≤300 palabras, abstract traducido bien
- [ ] **Anexos:** A-G completos, tablas/figuras numeradas, códigos cualitativos explícitos
- [ ] **Word UIIX:** Tipografía correcta, márgenes UIIX, numeración automática, índice generado
- [ ] **PDF:** Renderizado correcto, paginación sin corrupts
- [ ] **Global Score:** ≥90/100 (comité), todos componentes ≥80
- [ ] **Git:** Commits limpios, history auditable

---

## 8. Estado Actual vs. Finalización

| Item | Hoy (25 Abril) | Día 7 (2 Mayo) | Esfuerzo |
|-----|---|---|---|
| Cap. 1 | ✅ 85/100 | ✅ 85/100 | 0 |
| Cap. 2 | 🔴 Pendiente review | ✅ 88–90/100 | 4.5h |
| Cap. 3 | ✅ 89–90/100 | ✅ 90–92/100 | 2–3h (si Tier 2) |
| Cap. 4 | ✅ 89.5/100 | ✅ 92–94/100 | 2h (Tier 2) |
| Cap. 5 | 🔴 No iniciado | ✅ 88–90/100 | 5.5h |
| Cap. 6 | 🔴 No iniciado | ✅ 88–90/100 | 4h |
| Portada+Resumen | 🔴 No iniciado | ✅ Completado | 1.5h |
| Anexos | 🔴 Parcial (borrador) | ✅ 100% compilado | 5h |
| Word UIIX | 🔴 No iniciado | ✅ Compilado, formateado | 3h |
| **TOTAL HORAS** | — | — | **~35–40 horas** |

**Ritmo:** ~6 horas/día promedio (viable en 7 días con disciplina + paralelos)

---

## 9. Aprobación Requerida

**Este plan está listo para ejecutión si:**
- [ ] Jorge aprueba timeline 7 días
- [ ] Jorge confirma disponibilidad dedicada (∼6h diarias)
- [ ] Comité doctoral confirma slot de defensa (Día 7 o posterior)

**Próximo paso:** 
1. Jorge revisa plan → aprobación/feedback
2. Claud inicia **Día 1 Mañana** con Cap. 2 writer-critic review
3. Commits + research journal actualizado cada hito

