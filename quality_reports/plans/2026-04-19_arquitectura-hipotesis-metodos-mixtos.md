# Plan: Clarificación de Arquitectura de Hipótesis para Estudio de Métodos Mixtos

**Fecha:** 2026-04-19  
**Investigador:** Jorge Ariel Loaiza Loaiza  
**Estado:** PENDIENTE APROBACIÓN  
**Objetivo:** Articular coherentemente las hipótesis cuantitativas, preguntas cualitativas y pregunta de integración mixta; resolver la tensión multi-país (ALBA) vs. contexto colombiano (entrevistas); alinear con Cap. 2 ya escrito.

---

## 1. CLASIFICACIÓN DEL DISEÑO

### Tipo de Diseño: SECUENCIAL CONFIRMATORIO MIXTO

Tu estudio sigue la secuencia:
1. **ALBA 2025** (cuantitativo, multi-país): Recopilación de datos de 540 estudiantes de educación superior en múltiples países (incluyendo Colombia)
2. **Entrevistas Mar 2026** (cualitativo, Colombia-específico): Scraping de datos de actores ecosistema colombiano (MinCIT, iNNpulsa, SENA, universidades, investigadores)
3. **Integración**: Explicar hallazgos cuantitativos usando perspectivas de actores colombianos

Esta es una estrategia legítima: no es inusual usar datos cuantitativos multi-país para identificar patrones, luego validar mecanismos con contexto específico.

**Implicación para hipótesis**: Las hipótesis nulas/alternativas (H₀/Ha) se aplican a la **MUESTRA ALBA COMPLETA** (todos los países), mientras que la **MUESTRA CUALITATIVA** (entrevistas) se enfoca en **explicar mecanismos en CONTEXTO COLOMBIANO ESPECÍFICAMENTE**.

---

## 2. ARQUITECTURA DE TRES NIVELES DE HIPÓTESIS/PREGUNTAS

### NIVEL 1: HIPÓTESIS CUANTITATIVAS (Componente ALBA)

Estas son las hipótesis que ya están en Cap. 1, ahora claramente etiquetadas como **componente cuantitativo**:

#### H0/H1 sobre Predicción TCP de Intención (Baseline)
```
H0₁: β_actitud = 0      |  H1₁: β_actitud > 0
H0₂: β_normas = 0       |  H1₂: β_normas > 0  
H0₃: β_PBC = 0          |  H1₃: β_PBC > 0
```
**Interpretación**: En ALBA (muestra multi-país), ¿predicen actitud, normas subjetivas y control conductual percibido la intención emprendedora?

#### H0/H1 sobre Efecto de Políticas Públicas (Ampliado)
```
H0₄: β_FK = 0           |  H1₄: β_FK > 0  (conocimiento formal ecosistema)
H0₅: β_FL = 0           |  H1₅: β_FL > 0  (alfabetización financiera)
```
**Interpretación**: ¿Aumenta conocimiento formal y alfabetización financiera la predicción de intención?

#### H0/H1 sobre Moderación Contextual Universitaria (Moderación)
```
H0₆: interaction(AT × U-D) = 0    |  H1₆: interaction(AT × U-D) > 0
H0₇: interaction(PBC × U-D) = 0   |  H1₇: interaction(PBC × U-D) > 0
... (otros términos de interacción por contexto universitario)
```
**Interpretación**: ¿Modula el contexto universitario (desarrollo, apoyo, clima) los efectos TCP sobre intención?

**Nota**: Estas hipótesis se prueban en la **MUESTRA ALBA COMPLETA**, que incluye estudiantes de múltiples países. Los hallazgos son **globales con datos que incluyen a Colombia**.

### NIVEL 2: PREGUNTAS CUALITATIVAS (Componente Entrevistas)

Estas NO tienen H₀/Ha predeterminada. Son preguntas abiertas que exploran mecanismos:

#### PQ1: Validación Conceptual de Constructos
```
¿Reconocen y articulan los actores ecosistema colombiano los constructos 
de nuestra investigación (actitud emprendedora, control conductual percibido, 
normas subjetivas, conocimiento del ecosistema, alfabetización financiera, 
contexto universitario) como factores relevantes en intención emprendedora 
de estudiantes?
```
**Objetivo**: Verificar que nuestro marco TCP + contexto tiene validez en concepto colombiano (no es construcción académica desconectada de realidad)

**Métodos**: Análisis temático de entrevistas, codificación inductiva de cómo actores hablan de factores que impulsan/frenan intención

#### PQ2: Mecanismos de Operación de Políticas Públicas
```
¿Cuáles son los mecanismos específicos a través de los cuales los actores 
ecosistema entienden que las políticas públicas (Ley 1014, Ley 2069, 
Fondo Emprender, iNNpulsa, SENA) influyen en intención emprendedora? 
¿Y cuáles son las brechas entre la intención de las políticas y su ejecución?
```
**Objetivo**: Explorar cómo se materializa "conocimiento formal del ecosistema" en la experiencia de estudiantes según actores

**Métodos**: Análisis de comunicados, discursos; identificar narrativas sobre accesibilidad de programas

#### PQ3: Brecha Intención-Acción desde Perspectiva de Actores
```
¿Cómo experimentan y explican los actores ecosistema la brecha entre 
intención emprendedora reportada por estudiantes (70-75% en universidades) 
y acción emprendedora real (20-25% en 5 años posteriores)?
¿Qué barreras perciben como más críticas?
```
**Objetivo**: Entender cuáles son las barreras REALES según actores vs. PERCIBIDAS según estudiantes (ALBA)

**Métodos**: Análisis temático de factores de fracaso mencionados; triangulación con hallazgos ALBA

### NIVEL 3: PREGUNTA DE INTEGRACIÓN MIXTA

Esta es la pregunta central que une ambos componentes:

```
¿Qué mecanismos identificados en perspectivas de actores ecosistema 
colombiano explican por qué ciertos estudiantes en ALBA (de múltiples 
países, incluyendo Colombia) con intención emprendedora alta no logran 
emprender, y cómo operan diferentemente estos mecanismos en contexto 
colombiano específico versus otros contextos?
```

**Desempaque de esta pregunta**:

1. **Parte cuantitativa**: ALBA identifica que algunos estudiantes tienen intención alta pero no emprenden
   - Preguntas ALBA: ¿Qué predice intención? ¿Qué factores contextuales moderan TCP?
   
2. **Parte cualitativa**: Entrevistas exploran por QUÉ ocurre la brecha, desde perspectiva de actores colombianos
   - Preguntas cualitativas: ¿Cuál es la "realidad" detrás de la brecha intención-acción desde el lado de la oferta institucional?
   
3. **Integración**: Explicación triangulada de la brecha intención-acción
   - Síntesis: Los datos cuantitativos dicen QUÉ predice intención y cómo contexto modula; los datos cualitativos dicen POR QUÉ algunos estudiantes no actúan (barreras reales) y cómo actores perciben facilitación/obstaculización

**Ventaja de esta formulación**: Reconoce que ALBA es multi-país pero permite usar perspectiva colombiana específica para **interpretar mecanismos** sin pretender que entrevistas generalizables a otros países.

---

## 3. RESOLUCIÓN DE LA TENSIÓN MULTI-PAÍS vs. COLOMBIA

### El Desafío
- ALBA: 540 estudiantes de múltiples países → hallazgos sobre TCP y moderación contexto son GLOBALES
- Entrevistas: Actores COLOMBIANOS únicamente → perspectiva LOCAL específica

### La Solución: Estrategia de Triangulación ANIDADA

**Paso 1**: Análisis ALBA produce hallazgos cuantitativos globales
- "En la muestra multi-país, la actitud predice intención (β=0.68)"
- "El contexto universitario modula el efecto de actitud (p<.05)"

**Paso 2**: Análisis de sub-muestra ALBA COLOMBIA
- Se extrae y analiza separately la sub-muestra colombiana de ALBA (¿cuántos son colombianos en ALBA?)
- Se compara: ¿Son patrones TCP similares en Colombia vs. otros países?
- Esto ancla los datos cuantitativos en contexto colombiano

**Paso 3**: Análisis cualitativo entrevistas COLOMBIA
- Explora mecanismos que explican los patrones hallados en ALBA (y en sub-muestra ALBA-Colombia)
- No pretende generalizar a otros países, solo profundizar en contexto donde se recopilaron datos cualitativos

**Paso 4**: Integración
- Triangulación: "Los datos ALBA (global y Colombian sub-set) muestran que contexto universitario modula TCP. ¿Cómo? Según actores ecosistema colombiano, porque [mecanismos explicitados]"

### Implicación para Cap. 3 Metodología
Necesitas especificar:
- Tamaño de sub-muestra colombiana en ALBA
- Si análisis separado por país es feasible (N suficiente?)
- Claridad sobre dónde resultados aplican globalmente vs. específicamente a Colombia

---

## 4. COHERENCIA CON CAP. 2 (Fundamentos Teóricos)

Cap. 2 ya escrito proporciona **marco teórico para componente cuantitativo** principalmente:
- TCP es el marco para predecir intención (H0/H1 del Nivel 1)
- Contexto universitario y políticas públicas como moderadores (H0/H1 del Nivel 1)
- Constructos operacionalizados basados en ALBA

**Lo que FALTA en Cap. 2 para métodos mixtos**:
- Ausencia de marco teórico CUALITATIVO explícito
- Cap. 2 no introduce un modelo teórico de cómo actores ecosistema **comunican/operacionalizan** políticas públicas
- No hay discusión de "perspectivas de stakeholders" como fuente de datos sobre mecanismos

**Recomendación**: Agregar una sección 2.8 o subsección final en Cap. 2 titulada:
```
"2.8 Perspectivas de Actores Ecosistema como Validación Cualitativa del Marco"
```
Que articule:
- Por qué validación cualitativa de constructos importa
- Qué preguntas cualitativas se harán (PQ1-PQ3 del Nivel 2)
- Cómo entrevistas con actores complementan el marco TCP

Esto haría que Cap. 2 presente AMBOS marcos (cuantitativo TCP + cualitativo perspectivas) en equilibrio.

---

## 5. ARQUITECTURA DE CAP. 3 (Metodología)

Cap. 3 debe tener estructura:

### 3.1-3.3: Metodología Cuantitativa
- 3.1 Descripción ALBA dataset (N=540, países, variables)
- 3.2 Operacionalización variables (8 constructos de Cap. 2)
- 3.3 Análisis: Regresión baseline (H0/H1₁-₃), regresión ampliada (H0/H1₄-₅), regresión con interacciones (H0/H1₆-₇)

### 3.4-3.6: Metodología Cualitativa  
- 3.4 Datos cualitativos: Fuentes (YouTube interviews + entrevistas institucionales), N unidades, período recolección
- 3.5 Operacionalización: Cómo codificar respecto a PQ1, PQ2, PQ3
- 3.6 Análisis: Análisis temático, protocolo de codificación, software (NVivo, Atlas.ti, o manual)

### 3.7: Estrategia de Integración Mixta
- 3.7.1 Triangulación: Cómo responden datos cualitativos a hallazgos cuantitativos
- 3.7.2 Sub-análisis ALBA-Colombia: Resultados cuantitativos solo en sub-muestra colombiana
- 3.7.3 Convergencia/Divergencia: ¿Convergen las perspectivas cualitativas con patrones cuantitativos?

### 3.8: Limitaciones del Diseño Mixto
- Tamaño desigual (N=540 cuantitativo vs. N=X cualitativo)
- Temporalidad desigual (ALBA 2025 vs. entrevistas Mar 2026)
- Geografía: ALBA multi-país pero entrevistas solo Colombia
- Validez externa: Resultados sobre intención aplicables globalmente; mecanismos específicos a Colombia

---

## 6. DECISIONES PARA JORGE

Antes de que escribamos Cap. 3, necesito que confirmes:

### Decisión 1: ✅ APROBADA — Análisis sub-muestra Colombia (N=41)

**Sub-muestra colombiana confirmada: 41 estudiantes**

Con N=41, análisis feasible:
- ✅ Estadística descriptiva (medias, desviaciones, distribuciones)
- ✅ Correlaciones bivariadas (relaciones pares de variables)
- ✅ Comparación descriptiva vs. muestra global (perfiles, diferencias medias)
- ✅ ANOVA simple (factores categóricos)
- ❌ Regresión multivariada con múltiples interacciones (requeriría 10:1 ratio, máximo ~4 predictores)

**Estrategia ajustada para Cap. 3**:
- Análisis ALBA GLOBAL (N=540): Regresión completa con todos términos TCP + contexto + interacciones (H₁₁-H₁₇)
- Análisis ALBA COLOMBIA (N=41): Correlaciones y descriptivas para verificar si patrones TCP similares en sub-muestra
- Síntesis: "Patrones TCP globales se replican descriptivamente en sub-muestra colombiana, aunque con poder estadístico menor"

**Opción B**: NO — Mantener análisis ALBA como global multi-país; cualitativas contextualizan pero no replican análisis
- Ventaja: Análisis más simple, evita problemas de sub-muestras pequeñas
- Desventaja: Menos integración directa; cualitativas se vuelven más "exploratorias" que confirmatoria

### Decisión 2: ¿Refinar Cap. 2 para incluir marco cualitativo?
**Opción A**: SÍ — Agregar sección 2.8 sobre perspectivas de actores como marco cualitativo
- Ventaja: Cap. 2 presenta ambos componentes mixtos equilibradamente
- Desventaja: Revise Cap. 2 que acabamos de terminar (aunque sería agregar, no reescribir)

**Opción B**: NO — Mantener Cap. 2 como está; Cap. 3 introduce marco cualitativo
- Ventaja: Cap. 2 está completo y aprobado
- Desventaja: Cap. 3 siente como tiene que "crear" nuevo marco en sección de metodología

---

## 7. RECOMENDACIONES

Mi recomendación es:

1. **Opción A en ambas decisiones**:
   - Sí analizar sub-muestra ALBA-Colombia (verificar N primero)
   - Sí agregar sección 2.8 "Perspectivas de Actores como Validación Cualitativa"
   
   Esto proporciona **coherencia arquitectónica**: Cap. 2 presenta ambos marcos, Cap. 3 ejecuta ambos métodos, resultados integran ambos.

2. **Pregunta de integración mixta refinada**:
   ```
   ¿Qué mecanismos identificados en perspectivas de actores ecosistema 
   colombiano explican la brecha intención-acción hallada en ALBA, 
   y cómo estos mecanismos operan específicamente en contexto colombiano 
   versus el patrón global?
   ```

3. **Arquitectura de hipótesis clara**:
   - Nivel 1: H₀/H₁ cuantitativas (globales, ALBA completa + sub-análisis Colombia si N permite)
   - Nivel 2: PQ₁-₃ cualitativas (exploratorias, contexto Colombia)
   - Nivel 3: Pregunta de integración mixta (triangulación)

---

## APROBACIÓN

¿Confirmas estas decisiones y arquitectura? Una vez aprobado, procedo a escribir Cap. 3 con claridad total sobre hipótesis, preguntas y estrategia de integración.

Cambios sugeridos a decisiones iniciales:
- [ ] Sí a análisis sub-muestra ALBA-Colombia (verificar N)
- [ ] Sí a sección 2.8 en Cap. 2
- [ ] Pregunta de integración mixta como refinada arriba
- [ ] Otro (especificar):

