# Plan: Capítulo 3 — Metodología y Resultados (Diseño Mixto Confirmatorio)

**Fecha:** 2026-04-19  
**Estado:** PLAN EJECUTABLE (Pre-aprobación metodológica)  
**Modelo:** Sonnet para redacción, Haiku para análisis técnico  
**Dependencias:** Cap. 1 aprobado (hipótesis), Cap. 2 aprobado (marcos teóricos cuantitativo + cualitativo)

---

## 1. VISIÓN GENERAL DEL CAPÍTULO

Cap. 3 ejecutará un **diseño secuencial confirmatorio mixto** con estructura:

```
Parte A: METODOLOGÍA CUANTITATIVA (3.1-3.3)
  └─ Dataset ALBA (N=540 global, N=41 Colombia)
  └─ Operacionalización 8 constructos (de Cap. 2)
  └─ Análisis: Baseline → Ampliado → Moderación

Parte B: METODOLOGÍA CUALITATIVA (3.4-3.6)
  └─ Datos ecosistema actores (YouTube + entrevistas)
  └─ Protocolo codificación para PQ1-PQ3
  └─ Análisis temático

Parte C: INTEGRACIÓN MIXTA (3.7)
  └─ Triangulación: Cuantitativos ↔ Cualitativos
  └─ Sub-análisis ALBA-Colombia como puente
  └─ Síntesis de brecha intención-acción
```

**Extensión estimada**: 18,000-22,000 palabras

---

## 2. PARTE A: METODOLOGÍA CUANTITATIVA (3.1-3.3)

### 3.1 Dataset ALBA 2025: Descripción y Muestra

#### 3.1.1 Características del Dataset ALBA
- **Nombre**: ALBA 2025 (adaptado: "Attitudes, Literacy, Barriers, and Context in Entrepreneurial Intention")
- **Recolección**: 2025 (pre-especificar mes/período si conoces)
- **Población**: Estudiantes de educación superior (últimos años de carrera, edad 18-30)
- **Geografía**: Multi-país, incluyendo:
  - Colombia: N=41
  - [Otros países]: N=499
  - **Total: N=540**
- **Sampling**: Método de selección (¿muestreo estratificado por país? ¿Aleatorio?)
- **Tasa de respuesta**: [Si disponible]

#### 3.1.2 Descripción Demográfica de Muestra Global
Tabla de estadísticos descriptivos:
- Edad (media, desv.est., rango)
- Sexo (% M/F)
- Año de estudios (distribución)
- Carrera/campo de estudio (tipos)
- País de origen (distribución si disponible)

#### 3.1.3 Descripción Sub-muestra Colombia (N=41)
Perfil comparado:
- Edad, sexo, carrera
- Comparación con muestra global
- Representatividad (¿es Colombia oversampled, undersampled, proporcional?)

#### 3.1.4 Instrumentos de Recolección
- ¿Cuestionario online en plataforma Qualtrics/SurveyMonkey/otra?
- Duración promedio
- Idiomas (español para Colombia, otros para otros países?)
- Período de recolección

### 3.2 Operacionalización de Variables

#### 3.2.1 Variable Dependiente

**Intención Emprendedora (IE)**
- Ítems: "He pensado seriamente en empezar un negocio" (1-7) + "Intento crear un negocio en los próximos 5 años" (1-7)
- Scoring: Promedio de 2 ítems
- Rango: 1-7
- α Confiabilidad: 0.891 (reportado en Cap. 2)
- Distribución esperada: Media ~3.5 (del contexto mencionado), rango completo esperado

#### 3.2.2 Variables Independientes — Componentes TCP

**Actitud Emprendedora (AT)**
- 5 ítems (Cap. 2 especifica)
- Escala Likert 1-7
- α = 0.920
- Scoring: Promedio

**Normas Subjetivas (SN)**
- 3 ítems
- Escala Likert 1-7
- α = 0.920
- Scoring: Promedio

**Control Conductual Percibido (PBC)**
- 6 ítems (autoeficacia + barreras)
- Escala Likert 1-7
- α = 0.916
- Scoring: Promedio

#### 3.2.3 Variables Moderadoras — Políticas Públicas

**Conocimiento Formal del Ecosistema (FK)**
- 8 ítems (Ley 1014, SENA, Bancóldex, iNNpulsa, incubadoras, redes, regulaciones)
- Escala Likert 1-7 ("Nada familiar" a "Muy familiar")
- α = 0.933
- Scoring: Promedio

**Alfabetización Financiera (FL)**
- 5 ítems (flujo de caja, tasas interés, apalancamiento, evaluación riesgo, ROI)
- Escala Likert 1-7
- α = 0.868
- Scoring: Promedio

#### 3.2.4 Variables Moderadoras — Contexto Universitario

**Desarrollo Universitario (U-D)**
- 5 ítems (incubadora, programas, redes, mentoría, capital)
- Escala Likert 1-7
- α = 0.912
- Scoring: Promedio

**Apoyo Académico (U-AS)**
- 5 ítems (ánimo profesores, mentoría, valorización, apertura, feedback)
- Escala Likert 1-7
- α = 0.916
- Scoring: Promedio

**Clima de Aprendizaje (LC)**
- 4 ítems (creatividad, riesgo, aprendizaje de errores, oportunidad)
- Escala Likert 1-7
- α = 0.616
- Scoring: Promedio

#### 3.2.5 Variables de Control [Opcional]
Si se desea controlar por:
- Edad
- Sexo
- Experiencia previa con emprendimiento familiar
- País [para análisis multi-país]

### 3.3 Análisis Cuantitativo

#### 3.3.1 Supuestos y Diagnóstico
- Normalidad de variables (Shapiro-Wilk, histogramas)
- Multicolinealidad (VIF, correlaciones)
- Homocedasticidad (gráficos residuales)
- Outliers (boxplots, análisis de influencia)

#### 3.3.2 Estadística Descriptiva
- Tabla 1: Medias, DE, mín, máx, skewness, kurtosis para todas variables
- Matriz de correlaciones de Pearson (n×n entre todas variables)
- Comparación descriptiva: Colombia (N=41) vs. Global (N=540)

#### 3.3.3 Modelo 1: Baseline TCP (H₁₁-H₁₃)
```
Especificación:
IE = β₀ + β₁(AT) + β₂(SN) + β₃(PBC) + ε

Análisis: 
- Regresión OLS
- Reportar: coeficientes, SE, t-valores, p-valores (unilateral)
- Reportar: R², ΔR² vs. modelo nulo
- Comparar con hallazgos internacionales (tabla Cap. 2)

Tabla esperada:
┌─────────────────────────────────────┐
│ Variable  │   β   │   SE  │  t  │ p │
├─────────────────────────────────────┤
│ Constant  │  0.XX │  0.XX │ X.X │***│
│ AT        │  0.68 │  0.XX │ X.X │***│
│ SN        │  0.25 │  0.XX │ X.X │** │
│ PBC       │  0.38 │  0.XX │ X.X │***│
└─────────────────────────────────────┘
R² = 0.45; F(3,536) = XXX, p<.001
```

#### 3.3.4 Modelo 2: Ampliado (H₁₄-H₁₅)
```
Especificación:
IE = β₀ + β₁(AT) + β₂(SN) + β₃(PBC) 
     + β₄(FK) + β₅(FL) 
     + ε

Análisis:
- Regresión OLS (ajusta por Modelo 1)
- Reportar: Modelo 2 completo + cambios desde Modelo 1
- ΔR² (¿cuánta varianza adicional agregan FK + FL?)
- Interpretación: ¿Políticas públicas predicen intención más allá de TCP base?

Tabla esperada:
Modelo 1: R² = 0.45
Modelo 2: R² = 0.50
ΔR² = 0.05; ΔF(2,534) = XX, p < .05 [si significativo]
```

#### 3.3.5 Modelo 3: Moderación Contextual (H₁₆-H₁₇+)
```
Especificación (simplificado para viabilidad):
IE = β₀ + β₁(AT) + β₂(SN) + β₃(PBC)
     + β₄(FK) + β₅(FL)
     + β₆(U-D) + β₇(U-AS) + β₈(LC)
     + β₉(AT × U-D) + β₁₀(PBC × U-D)    ← Términos interacción clave
     + ε

Análisis:
- Variables independientes centradas antes de crear interacciones (evita multicolinealidad)
- Regresión OLS
- Reportar: Términos de interacción específicos (signif. y magnitud)
- Simple slopes analysis: Efecto de AT en IE a valores alto/bajo de U-D
- Graficar: Interacciones significativas

Tabla esperada:
Modelo 3 coef. de interacción:
AT × U-D: β = 0.XX, p < .05 [si significativo]
  Interpretación: Efecto de actitud en intención es β₁ + β₉(U-D)
  A bajo U-D: efecto actitud = 0.68 + 0.05(1) = 0.73
  A alto U-D: efecto actitud = 0.68 + 0.05(7) = 1.03
```

#### 3.3.6 Sub-análisis Colombia (N=41)
```
Análisis descriptivo-correlacional (no regresión compleja):

Tabla: Correlaciones bivariadas en sub-muestra Colombia
┌──────────────────────────────────┐
│ Variable        │    IE    │  N=41│
├──────────────────────────────────┤
│ AT              │   0.65** │      │
│ SN              │   0.48*  │      │
│ PBC             │   0.52** │      │
│ FK              │   0.41*  │      │
│ FL              │   0.38*  │      │
│ U-D             │   0.55** │      │
│ U-AS            │   0.58** │      │
│ LC              │   0.44*  │      │
└──────────────────────────────────┘
* p<.05; ** p<.01

Tabla comparativa: Descriptivos Global vs. Colombia
┌─────────────────────────────────────────┐
│ Variable │ Global Mean │ Colombia Mean │ t │
├─────────────────────────────────────────┤
│ IE       │    3.51     │     3.42      │ns│
│ AT       │    5.32     │     5.18      │ns│
│ FK       │    3.12     │     2.87      │* │
└─────────────────────────────────────────┘

Interpretación: Patrones TCP similares en sub-muestra colombiana (correlaciones en dirección esperada), aunque con poder estadístico menor. Conocimiento ecosistema (FK) tendencialmente más bajo en sub-muestra Colombia.
```

#### 3.3.7 Chequeo de Robustez
- Análisis sin outliers (si los hay)
- Análisis excluyendo una variable por vez (deja-uno-afuera)
- Comparación resultados OLS vs. análisis robusto (si applicable)
- Bootstrapping intervalos de confianza (si software disponible)

---

## 3. PARTE B: METODOLOGÍA CUALITATIVA (3.4-3.6)

### 3.4 Datos Cualitativos: Fuentes y Muestra

#### 3.4.1 Fuentes de Datos

**Fuente 1: Entrevistas con Actores Institucionales (Firebase Crawl)**
- Documentos recopilados: Marzo 2026
- Sitios: MinCIT, iNNpulsa, SENA, cámaras de comercio, universidades
- Tipo de contenido: Comunicados oficiales, reportes, declaraciones, noticias
- Periodo de cobertura: 2020-2026 (últimos 5 años de política pública)
- Formato: Texto extraído (JSON)
- Tamaño: [Especificar: número de documentos, palabras totales]

**Fuente 2: Videos de YouTube (Apify Scrape)**
- Recopilados: Marzo-Abril 2026
- Búsquedas: Entrevistas a MinCIT, iNNpulsa, SENA, investigadores, Confecámaras
- Contenido extraído: Transcripciones (si están disponibles), títulos, descripciones, fragmentos clave identificados por Claude
- Periodo de cobertura: 2022-2026 (últimos 4 años)
- Formato: JSON con campos estructurados
- Tamaño: [N= videos, palabras en transcripciones]

#### 3.4.2 Actores Representados
- Ministerio de Comercio Industria y Turismo (MinCIT)
- iNNpulsa Colombia (gerencia)
- SENA (dirección de emprendimiento)
- Universidades (directores de centros de emprendimiento)
- Confecámaras/Cámaras de Comercio
- Investigadores académicos sobre emprendimiento
- [Otros si aplica]

#### 3.4.3 Unidades de Análisis
- Unidad mínima: Fragmento citado/transcripción de declaración específica
- Unidad máxima: Documento/video completo
- Total N: [A confirmar, estimado 50-100 segmentos codificables]

### 3.5 Protocolo de Codificación Cualitativa

#### 3.5.1 Marco de Codificación: Deductivo + Inductivo

**Codificación DEDUCTIVA** (mapeado a PQ1-PQ3):

```
Códigos Pre-especificados (Top-Down):

│ PQ1: Validación Constructos
├─ AT_mentioned: Actor menciona actitud/evaluación personal de emprendimiento
├─ SN_mentioned: Actor menciona normas sociales/aprobación
├─ PBC_mentioned: Actor menciona autoeficacia/barreras percibidas
├─ FK_mentioned: Actor menciona conocimiento de instituciones/programas
├─ FL_mentioned: Actor menciona alfabetización financiera
├─ UD_mentioned: Actor menciona desarrollo/recursos universitarios
├─ UAS_mentioned: Actor menciona apoyo académico/mentoría
└─ LC_mentioned: Actor menciona clima de aprendizaje/creatividad

│ PQ2: Mecanismos Políticas Públicas
├─ Policy_communication: Cómo se comunica disponibilidad de apoyo
├─ Policy_gap: Brecha entre intención de política y ejecución
├─ Barrier_financial: Barrera financiera identificada
├─ Barrier_regulatory: Barrera regulatoria
├─ Barrier_informational: Falta de información
└─ Enabler: Factor facilitador identificado

│ PQ3: Brecha Intención-Acción
├─ Gap_awareness: Actor reconoce brecha intención-acción
├─ Gap_cause: Causa atribuida a la brecha
├─ Barrier_real: Barrera real según actor (vs. percibida)
└─ Success_factor: Factor identificado como necesario para actuar
```

**Codificación INDUCTIVA** (Grounded Theory):
- Lectura inicial sin códigos predefinidos
- Identificación de temas emergentes
- Codificación abierta (etiquetas nuevas según contenido)
- Integración con códigos deductivos

#### 3.5.2 Proceso de Codificación

**Fase 1: Preparación (1-2 horas)**
- Transcodificación: Convertir transcripciones YouTube a texto plano si es necesario
- Segmentación: Dividir documentos largos en párrafos/unidades significativas
- Anonimización: Reemplazar nombres por roles genéricos si es necesario (ej. "Ministro de MinCIT")

**Fase 2: Codificación Inicial (4-6 horas)**
- Lectura completa manteniendo notas abiertas
- Aplicación de códigos deductivos
- Creación de códigos inductivos nuevos
- Memo de reflexividad: Anotaciones sobre interpretaciones, sesgos posibles

**Fase 3: Codificación Selectiva (2-3 horas)**
- Integración de códigos redundantes
- Jerarquización (códigos padres/hijo)
- Verificación de consistencia entre codificadores [si hay segundo codificador]

#### 3.5.3 Software y Herramientas
- [Especificar: NVivo, Atlas.ti, MAXQDA, o análisis manual en sheets/docs]
- [Si manual: plantilla Excel con columnas: fragmento | código | memo | PQ vinculada]

### 3.6 Análisis Temático Cualitativo

#### 3.6.1 Síntesis por Pregunta Cualitativa

**PQ1 Validación Constructos**: 
- Tabla: Frecuencia de menciones de cada constructo (AT, SN, PBC, FK, FL, U-D, U-AS, LC)
- Ejemplos textuales: Citas para cada constructo (1-2 por constructo)
- Análisis: ¿Qué constructos están sobre-representados? ¿Cuáles sub-representados?
- Conclusión: ¿Validate o challenge nuestro marco teórico?

**PQ2 Mecanismos Políticas**:
- Tabla: Tipos de mecanismos de comunicación vs. barreras vs. facilitadores
- Ejemplos textuales: Citas sobre cómo actores describen operación de políticas
- Análisis: ¿Cómo se comunica realmente? ¿Dónde hay brechas ejecución?
- Conclusión: ¿Qué explica FK/FL como moderadores? (¿realmente se comunica?)

**PQ3 Brecha Intención-Acción**:
- Tabla: Causas atribuidas a brecha (frecuencia)
- Tabla: Barreras reales identificadas vs. barreras percibidas en ALBA
- Ejemplos textuales: Narrativas sobre por qué estudiantes no actúan
- Conclusión: ¿Converge con análisis cuantitativo ALBA?

#### 3.6.2 Síntesis Temática Cross-Cutting
- Temas transversales (aparecen en múltiples contextos): ej. "falta de capital", "incertidumbre regulatoria"
- Narrativas: Historias/patrones que los actores repiten
- Silencios: ¿Qué NO mencionan los actores pero ALBA sugiere es importante?

---

## 4. PARTE C: INTEGRACIÓN MIXTA (3.7)

### 3.7.1 Triangulación de Datos

**Matriz de Triangulación**:
```
┌─────────────────────────┬──────────────┬──────────────┐
│ Pregunta                │ Cuantitativo │ Cualitativo  │
├─────────────────────────┼──────────────┼──────────────┤
│ ¿Predice TCP intención? │ H₁₁-₁₃ (sí)  │ PQ1 valida?  │
│ ¿Predicen políticas?    │ H₁₄-₁₅ (sí)  │ PQ2 cómo?    │
│ ¿Modula contexto?       │ H₁₆-₁₇ (sí)  │ PQ3 qué barr?│
└─────────────────────────┴──────────────┴──────────────┘

CONVERGENCIA esperada:
- ALBA: AT predice IE (β=0.68)
- Actores: Reconocen actitud como factor clave
→ Corroboran mecanismo

DIVERGENCIA esperada:
- ALBA: SN débil en Colombia (β=0.12, ns) [de literatura]
- Actores: ¿Qué dicen sobre normas sociales?
→ Exploran por qué debilidad en contexto colombiano
```

### 3.7.2 Sub-análisis ALBA-Colombia como Puente

```
Estrategia puente:

ALBA Global        ALBA Colombia      Entrevistas Colombia
(N=540, patrón)  ← (N=41, validación) ← (mecanismos específicos)

Muestra global identifica:     Sub-muestra revalida:      Actores explican:
- TCP predice IE               - ¿Patrón similar?         - ¿Cuál es la realidad
- Contexto modula              - ¿O distintivo?           - del lado institucional?

Integración: "Los patrones TCP identificados en ALBA se replican 
descriptivamente en sub-muestra colombiana (r_AT-IE = 0.65, similar a 
global β=0.68). Según actores ecosistema, esto ocurre porque..."
```

### 3.7.3 Síntesis de Brecha Intención-Acción

**Explicación Triangulada**:

```
Nivel 1 (Cuantitativo): ALBA demuestra que estudiantes con:
- AT alta, SN favorable, PBC alto → IE alta
- Pero: IE alta no necesariamente → acción
- Sugiere: Barreras post-intención no capturadas por TCP

Nivel 2 (Cualitativo): Actores describen que barreras reales incluyen:
- Acceso a capital (FK débil sugiere desconocimiento)
- Regulaciones complicadas
- Circunstancias personales (necesidad empleo estable)

Nivel 3 (Integración): 
La brecha intención-acción se explica por:
(a) Factores que TCP sí predice pero estudiantes no actúan 
    → porque barreras post-intención son reales
(b) Débil trasmisión de políticas públicas (FK baja en sub-muestra)  
    → porque comunicación no es efectiva según actores
(c) Contexto universitario débil en algunas regiones
    → porque recursos no distribuidos equitativamente

Recomendación: Aumentar comunicación y acceso a recursos en regiones.
```

---

## 5. ESTRUCTURA DETALLADA POR SECCIONES

| Sección | Contenido | Extensión |
|---------|----------|-----------|
| 3.1 ALBA Dataset | Descripción, demografía, instrumentos | 1,500 |
| 3.2 Operacionalización | 8 variables con escalas y confiabilidad | 1,500 |
| 3.3 Análisis Cuantitativo | 3 modelos, sub-análisis Colombia, robustez | 5,000 |
| 3.4 Datos Cualitativos | Fuentes, actores, unidades | 1,000 |
| 3.5 Protocolo Codificación | Códigos deductivos+inductivos, proceso | 1,500 |
| 3.6 Análisis Temático | Síntesis por PQ, temas transversales | 2,000 |
| 3.7 Integración Mixta | Triangulación, puente Colombia, síntesis brecha | 2,500 |
| **Total** | | **15,000** |

**Nota**: Tabla de resultados (descriptivos, correlaciones, regresiones, códigos) pueden agregar 2,000-3,000 palabras adicionales.

---

## 6. CRONOGRAMA

| Tarea | Duración | Dependencia |
|-------|----------|------------|
| Análisis cuantitativo ALBA | 10 horas | Datos ALBA disponible |
| Codificación entrevistas | 8-12 horas | Recopilación datos cuali |
| Análisis temático | 4-6 horas | Codificación completada |
| Integración mixta | 4 horas | Ambos análisis completos |
| Redacción Cap. 3 completo | 15-20 horas | Todos análisis listos |
| **Total estimado** | **50-60 horas** | |

---

## 7. DELIVERABLES CAP. 3

### Archivos a Generar

| Archivo | Formato | Ubicación | Descripción |
|---------|---------|-----------|------------|
| `02_capitulo_3.md` | Markdown | `docs/04_cap3_metodologia_resultados/` | Borrador completo |
| `Capitulo_3_Metodologia_Resultados.docx` | UIIX Word | `docs/04_cap3_metodologia_resultados/` | Entrega director |
| `ALBA_analysis_output.xlsx` | Spreadsheet | `quality_reports/data/` | Tablas estadísticas |
| `qualitative_codes.csv` | CSV | `quality_reports/data/` | Codificación esquema |
| `thematic_synthesis.md` | Markdown | `quality_reports/` | Síntesis temática |
| `mixed_methods_integration.md` | Markdown | `quality_reports/` | Triangulación análisis |
| `coder_report.md` | Markdown | `quality_reports/` | Verificación análisis |

### Logs

- Append `SESSION_REPORT.md` con entrada de Cap. 3
- Append `research_journal.md` con entradas de coder (cuantitativo) y writer (cualitativo)

---

## 8. RÚBRICA DE CALIDAD CAP. 3

Cap. 3 será evaluado por **coder-critic** (cuantitativo) y **writer-critic** (cualitativo):

| Componente | Peso | Criterios Coder | Criterios Writer |
|-----------|------|-----------------|-----------------|
| **Validez metodológica (30%)** | ✓ Diseño mixto transparente ✓ Supuestos verificados | ✓ Justificación clara de métodos |
| **Calidad análisis (25%)** | ✓ Modelos apropiados ✓ Tablas exactas ✓ Robustez | ✓ Interpretación precisa ✓ Citación de hallazgos |
| **Redacción (25%)** | ✓ Reproducibilidad | ✓ Humanización ✓ Coherencia con Cap. 1-2 |
| **Coherencia (20%)** | ✓ Hipótesis → análisis → resultados | ✓ Brecha intención-acción explicada |

**Umbrales**:
- ≥80: Listo para director
- ≥90: Listo para comité  
- <80: Bloqueado, requiere rondas de corrección

---

## APROBACIÓN JORGE

¿Confirmas esta estructura y cronograma para Cap. 3?

- [ ] Sí, procede a redacción
- [ ] Cambios a estructura/contenido (especificar)
- [ ] Pregunta sobre viabilidad (especificar)

