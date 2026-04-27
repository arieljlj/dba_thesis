# Codebook — Dataset ALBA 2025
## `datos_encuesta_2025.csv`

**Fuente:** Alba, M. (2025). *Dataset: Entrepreneurial Intention and Action in ACBSP-accredited Latin American Universities (2024–2025)* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17702439

**Dimensiones del dataset:** 540 observaciones × 131 variables  
**Escala principal:** Likert 1–5 (1 = Muy en desacuerdo / 5 = Muy de acuerdo), salvo EW (1–7)  
**Fecha de codificación:** 2026-04-27

---

## Variables Sociodemográficas (5 variables)

### Variable: `Country`

País al que pertenece la universidad del estudiante.

| Código | País | N |
|--------|------|---|
| 1 | Perú | 100 |
| 2 | México | 168 |
| 3 | Ecuador | 147 |
| 4 | Paraguay | 84 |
| 5 | Colombia | 41 |
| **Total** | | **540** |

---

### Variable: `Age`

Rango de edad del estudiante.

| Código | Categoría |
|--------|-----------|
| 1 | Entre 18 y 24 |
| 2 | Entre 25 y 39 |
| 3 | Entre 40 y 59 |
| 4 | 60 en adelante |

---

### Variable: `Semester`

Semestre que cursa.

| Código | Categoría |
|--------|-----------|
| 1–9 | Semestre 1 al 9 |
| 10 | Otro |

---

### Variable: `Exp`

¿Ha tenido experiencia emprendedora?

| Código | Categoría |
|--------|-----------|
| 1 | Sí |
| 2 | No |

---

### Variable: `Gender`

Género del estudiante.

| Código | Categoría |
|--------|-----------|
| 1 | Femenino |
| 2 | Masculino |
| 3 | No binario |
| 4 | Otro |
| 5 | Prefiero no decirlo |

---

## Escala de respuesta general

Escala Likert 1–5:

| Valor | Etiqueta |
|-------|----------|
| 1 | Muy en desacuerdo |
| 2 | En desacuerdo |
| 3 | Ni de acuerdo ni en desacuerdo |
| 4 | De acuerdo |
| 5 | Muy de acuerdo |

**Excepción — EW (Bienestar/Satisfacción con la vida):** Escala 1–7  
(1 = Fuertemente en desacuerdo … 7 = Fuertemente de acuerdo)

---

## Bloque R — Percepción del Riesgo (9 ítems)

**Variables:** R1, R2, R3, R4, R5, R6, R7, R8, R9  
**Escala:** 1–5  
**Estadísticos:** M global = 3.398 (DE = 1.268); M Colombia = 3.355  
**Nota:** R4–R9 son ítems inversos (orientación hacia evitación del riesgo).

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| R1 | In the past six months, there were moments when I took risks. |
| R2 | I like to try new foods, explore new places, and engage in completely novel experiences. |
| R3 | If I am afraid of something, I will try to overcome my fears. |
| R4 | I have never been on a blind date. *(inverso)* |
| R5 | I have never traveled on an unfamiliar route. *(inverso)* |
| R6 | I do not like extreme sports. *(inverso)* |
| R7 | I need to know the answer before asking the question. *(inverso)* |
| R8 | I need to know what has been done before in order to be willing to try it myself. *(inverso)* |
| R9 | I only get involved in situations where I know the outcome. *(inverso)* |

---

## Bloque EI — Intención Emprendedora (5 ítems)

**Variables:** EI1, EI2, EI3, EI4, EI5  
**Escala:** 1–5  
**Estadísticos:** M global = 4.021 (DE = 1.057); M Colombia = 4.224  
**Rol TCP:** Variable dependiente (VD).

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EI1 | My professional goal is to become an entrepreneur. |
| EI2 | I will make every effort to start and run my own business. |
| EI3 | I am determined to create a company in the future. |
| EI4 | I seriously consider starting a business. |
| EI5 | I firmly intend to start a company someday. |

---

## Bloque EA — Actitudes hacia el Emprendimiento (8 ítems)

**Variables:** EA1, EA2, EA3, EA4, EA5, EA6, EA7, EA8  
**Escala:** 1–5  
**Estadísticos:** M global = 4.065 (DE = 1.019); M Colombia = 4.299  
**Rol TCP:** Actitud Emprendedora (AT). Variable independiente principal.

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EA1 | I want to provide job opportunities. |
| EA2 | I want to be an agent of change in society. |
| EA3 | I want to gain recognition and respect as an entrepreneur. |
| EA4 | I enjoy leading and influencing others. |
| EA5 | I want to have balance and flexible schedules for my work and private life. |
| EA6 | I am passionate about learning. |
| EA7 | The high unemployment rate has prompted me to seriously consider starting my own business. |
| EA8 | I like to hold a high position in society. |

---

## Bloque M — Percepción del Entorno de Mercado (2 ítems)

**Variables:** M1, M2  
**Escala:** 1–5  
**Estadísticos:** M global = 2.115; M Colombia = 2.024

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| M1 | New businesses face high competitive pressures immediately. |
| M2 | It is difficult to find a business idea that has not been implemented before. |

---

## Bloque F — Percepción del Entorno de Financiamiento (2 ítems)

**Variables:** F1, F2  
**Escala:** 1–5  
**Estadísticos:** M global = 2.688; M Colombia = 2.756

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| F1 | It is easy to obtain venture capital. |
| F2 | Banks do not easily provide credit to new businesses. |

---

## Bloque G — Percepción del Entorno Gubernamental (4 ítems)

**Variables:** G1, G2, G3, G4  
**Escala:** 1–5  
**Estadísticos:** M global = 2.436 (DE = 1.246); M Colombia = 2.299

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| G1 | There are sufficient subsidies available for new businesses in this country. |
| G2 | Support from consultants and qualified services for new businesses is available in this country. |
| G3 | The bureaucratic procedures for founding a new business are unclear in this country. |
| G4 | State laws (rules and regulations) are unfavorable for running a business in this country. |

---

## Bloque S — Percepción del Entorno Social (3 ítems)

**Variables:** S1, S2, S3  
**Escala:** 1–5  
**Estadísticos:** M global = 3.577 (DE = 1.049); M Colombia = 3.683  
**Rol TCP:** Proxy de Normas Subjetivas (SN); complementado con análisis cualitativo.

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| S1 | Entrepreneurs have a positive image in society in this country. |
| S2 | Entrepreneurs have social responsibility in their businesses in this country. |
| S3 | Entrepreneurs should contribute to society in this country through their businesses. |

---

## Bloque U — Percepción Universidad: Preparación General (3 ítems)

**Variables:** U1, U2, U3  
**Escala:** 1–5  
**Estadísticos:** M global = 3.479 (DE = 1.101); M Colombia = 3.943

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| U1 | The university courses prepare me well to work independently. |
| U2 | The university courses help develop skills for working independently. |
| U3 | The subjects prepare me to be creative in self-employment. |

---

## Variable: `UI-1` — Infraestructura de Inversión Universitaria (1 ítem)

**Escala:** 1–5  
**Estadísticos:** M global = 3.470 (DE = 1.087); M Colombia = 4.073

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| UI-1 | The university provides a strong network of investors in new businesses. |

---

## Bloque U-D — Desarrollo Institucional Universitario (5 ítems)

**Variables:** U-D1, U-D2, U-D3, U-D4, U-D5  
**Escala:** 1–5  
**Estadísticos:** M global = 3.634 (DE = 1.031); M Colombia = 4.102

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| U-D1 | The university's creative atmosphere inspires us to develop ideas for new businesses. |
| U-D2 | The courses allow us to focus on the creation of new products or services. |
| U-D3 | The courses allow us to define the business model of the new venture. |
| U-D4 | The courses foster the social and leadership skills needed by entrepreneurs. |
| U-D5 | The courses provide students with the knowledge required to start a new business. |

---

## Bloque U-AS — Apoyo Académico Universitario (3 ítems)

**Variables:** U-AS1, U-AS2, U-AS3  
**Escala:** 1–5  
**Estadísticos:** M global = 3.383 (DE = 1.114); M Colombia = 3.967

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| U-AS1 | My university supports the creation of multidisciplinary student teams. |
| U-AS2 | The university actively promotes the processes of founding new businesses. |
| U-AS3 | There is support from the university for the creation of new businesses. |

---

## Bloque LC — Locus de Control (8 ítems)

**Variables:** LC1, LC2, LC3, LC4, LC5, LC6, LC7, LC8  
**Escala:** 1–5  
**Estadísticos:** M global = 3.315 (DE = 1.136); M Colombia = 3.396  
**Nota:** LC2, LC3, LC4, LC7 son ítems de locus externo (se revierten para calcular índice de locus interno).

| Variable | Ítem (versión en inglés) | Dirección |
|----------|--------------------------|-----------|
| LC1 | I can anticipate difficulties and take action to avoid them. | Interno |
| LC2 | Much of what happens to me is probably a matter of luck. | Externo |
| LC3 | Everyone knows that luck or chance determines our destiny. | Externo |
| LC4 | I can only control my problems if I have support from someone else. | Externo |
| LC5 | When I make plans, I am almost certain I can make them work. | Interno |
| LC6 | Being successful is a matter of hard work. Luck has little or nothing to do with it. | Interno |
| LC7 | My life is controlled by external actions and events. | Externo |
| LC8 | I am confident that I can successfully deal with future problems. | Interno |

---

## Bloque EAct — Acción Emprendedora (16 ítems)

**Variables:** EAct1–EAct16  
**Escala:** 1–5  
**Estadísticos:** M global = 2.871 (DE = 1.312); M Colombia = 2.733

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EAct1 | I have identified market opportunities. |
| EAct2 | I have prepared a business plan. |
| EAct3 | I have developed models or procedures for a product/service. |
| EAct4 | I have chosen a name for the business. |
| EAct5 | I am dedicated full-time to the business. |
| EAct6 | I have organized a team for the start-up of the business. |
| EAct7 | I have created a legal entity for the business. |
| EAct8 | I have registered the business with the tax authorities. |
| EAct9 | I have invested some of my own money in a business. |
| EAct10 | I have applied for and received financial support to start my business. |
| EAct11 | I have secured the location and equipment needed to start a business. |
| EAct12 | I have purchased or leased most of the equipment, facilities, and properties. |
| EAct13 | I have purchased raw materials, inventories, and supplies. |
| EAct14 | I have started marketing and promotional activities. |
| EAct15 | I have applied for licenses or patents. |
| EAct16 | I have hired employees. |

---

## Bloque FK — Conocimiento Financiero (8 ítems)

**Variables:** FK1, FK2, FK3, FK4, FK5, FK6, FK7, FK8  
**Escala:** 1–5  
**Estadísticos:** M global = 3.709 (DE = 1.089); M Colombia = 3.534  
**Nota:** El cuestionario en inglés documenta 7 ítems FK. El dataset contiene 8 variables (FK1–FK8). FK8 (M = 4.133; Colombia M = 4.317) puede corresponder a un ítem adicional incorporado en la versión en español para muestras latinoamericanas. Requiere confirmación con el equipo ALBA.

| Variable | Ítem (versión en inglés) | M global |
|----------|--------------------------|---------|
| FK1 | I know about asset liquidity. | 3.665 |
| FK2 | I know about personal financial planning. | 3.696 |
| FK3 | I know about spending and saving patterns. | 3.693 |
| FK4 | I know about compound interest. | 3.744 |
| FK5 | I know about time deposit certificates. | 3.428 |
| FK6 | I know about reasons for acquiring insurance. | 3.615 |
| FK7 | I know about investment diversification. | 3.700 |
| FK8 | *(Ítem no documentado en versión inglesa — verificar con equipo ALBA)* | 4.133 |

---

## Bloque EC — Competencias Emocionales (21 ítems)

**Escala:** 1–5  
**Sub-dimensiones:** Autoconciencia (SA), Autorregulación (SR), Motivación (M), Empatía (E), Habilidades Sociales (SS)

### EC-SA — Autoconciencia (3 ítems)

**Variables:** EC-SA1, EC-SA2, EC-SA3  
**Estadísticos:** M global = 4.070 (DE = 0.924); M Colombia = 4.293

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EC-SA1 | I am able to recognize my own emotions and their effect on my actions. |
| EC-SA2 | I am aware of my own strengths and limitations. |
| EC-SA3 | I have great confidence in my self-worth and my ability to do anything. |

### EC-SR — Autorregulación (4 ítems)

**Variables:** EC-SR1, EC-SR2, EC-SR3, EC-SR4  
**Estadísticos:** M global = 4.124 (DE = 0.939); M Colombia = 4.341

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EC-SR1 | I have self-regulation. |
| EC-SR2 | I consider myself an honest and upright person. |
| EC-SR3 | I am able to take responsibility for my personal actions. |
| EC-SR4 | I consider myself a flexible person, capable of facing change. |

### EC-M — Motivación (4 ítems)

**Variables:** EC-M1, EC-M2, EC-M3, EC-M4  
**Estadísticos:** M global = 4.022 (DE = 0.941); M Colombia = 4.274

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EC-M1 | I feel comfortable and open to new ideas, approaches, and information. |
| EC-M2 | I like to push myself to improve or achieve a certain standard of excellence. |
| EC-M3 | I commit to working toward the goals of a group or organization when I identify with them. |
| EC-M4 | I act quickly to take advantage of opportunities. |

### EC-E — Empatía (5 ítems)

**Variables:** EC-E1, EC-E2, EC-E3, EC-E4, EC-E5  
**Estadísticos:** M global = 3.993 (DE = 0.912); M Colombia = 4.259

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EC-E1 | I am persistent in working to achieve my goals despite obstacles and setbacks. |
| EC-E2 | I am able to understand other people's feelings and points of view, and I take an active interest in the things that concern them. |
| EC-E3 | I recognize other people's need for progress, and I like to stimulate their abilities. |
| EC-E4 | I am able to anticipate, recognize, and meet the needs of others. |
| EC-E5 | I like to take advantage of opportunities offered by different types of people. |

### EC-SS — Habilidades Sociales (5 ítems)

**Variables:** EC-SS1, EC-SS2, EC-SS3, EC-SS4, EC-SS5  
**Estadísticos:** M global = 3.819 (DE = 0.969); M Colombia = 4.176

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EC-SS1 | I am aware of the emotional state and the underlying power relationships in a group. |
| EC-SS2 | I can make use of effective means of persuasion. |
| EC-SS3 | I know how to listen and can deliver a convincing message. |
| EC-SS4 | I have the ability to negotiate and resolve conflicts. |
| EC-SS5 | I am able to inspire and lead teams and individuals. |

---

## Bloque SE — Autoeficacia Emprendedora (5 ítems)

**Variables:** SE1, SE2, SE3, SE4, SE5  
**Escala:** 1–5  
**Estadísticos:** M global = 3.839 (DE = 0.945); M Colombia = 3.907  
**Rol TCP:** Control Conductual Percibido (PBC). Variable independiente principal; complementada con análisis cualitativo.

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| SE1 | I feel that I am capable of defining a business idea and strategy for a new venture. |
| SE2 | I feel that I am capable of writing a business plan (conducting market research, financial analysis, etc.). |
| SE3 | I feel that I am capable of negotiating and maintaining supportive relationships with banks and potential investors. |
| SE4 | I feel that I am capable of recognizing opportunities for the development of new products and/or services. |
| SE5 | I feel that I am capable of building relationships with key people to obtain the necessary capital to start a new business. |

---

## Bloque CL — Carga Cognitiva (12 ítems)

**Variables:** CL1–CL12  
**Escala:** 1–5 (sub-escalas de complejidad, claridad, esfuerzo y concentración)  
**Estadísticos:** M global = 3.282 (DE = 1.100); M Colombia = 3.476

| Variable | Ítem (versión en inglés) | Dirección |
|----------|--------------------------|-----------|
| CL1 | The topic or topics covered were very complex. | Carga (+) |
| CL2 | The topics covered included formulas that I perceived as very complex. | Carga (+) |
| CL3 | The topics covered included concepts and definitions that I perceived as very complex. | Carga (+) |
| CL4 | The instructions and/or explanations were very unclear. | Carga (+) |
| CL5 | The instructions and/or explanations were, in terms of learning, very ineffective. | Carga (+) |
| CL6 | The instructions and/or explanations were full of unclear language. | Carga (+) |
| CL7 | The topics covered really improved my knowledge and understanding. | Aprendizaje (inverso) |
| CL8 | The topics covered really improved my understanding of concepts and definitions. | Aprendizaje (inverso) |
| CL9 | The study program or the semesters I attended required me to invest significant mental effort. | Esfuerzo (+) |
| CL10 | The study program or the semesters I attended were… (1=Very easy / 5=Very difficult) | Dificultad (+) |
| CL11 | Learning from the study program or the semesters I attended was… (1=Very easy / 5=Very difficult) | Dificultad (+) |
| CL12 | How much did you concentrate during the study program or the semesters you attended? (1=Very little / 5=A lot; inverso de carga) | Concentración (inverso) |

---

## Bloque EW — Bienestar General y Satisfacción con la Vida (5 ítems)

**Variables:** EW1, EW2, EW3, EW4, EW5  
**Escala:** 1–7 *(excepción: escala Likert diferente al resto del instrumento)*  
**Estadísticos:** M global = 4.770 (DE = 1.646); M Colombia = 4.976

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| EW1 | In most respects, my life is close to my ideal. |
| EW2 | The conditions of my life are excellent. |
| EW3 | I am completely satisfied with my life. |
| EW4 | So far, I have achieved the important things I want in life. |
| EW5 | If I could live my life over, I would change almost nothing. |

---

## Bloque FL — Estado de Flujo (6 ítems)

**Variables:** FL1, FL2, FL3, FL4, FL5, FL6  
**Escala:** 1–5  
**Estadísticos:** M global = 2.949 (DE = 1.195); M Colombia = 2.797

| Variable | Ítem (versión en inglés) |
|----------|--------------------------|
| FL1 | My mind does not wander. I am fully involved in what I am doing and not thinking about anything else. |
| FL2 | My body feels good. The world seems to be separated from me. |
| FL3 | I am less aware of myself and my problems. |
| FL4 | My concentration is like breathing — I never think about it. |
| FL5 | When I start something, I really shut out the world. |
| FL6 | I am so involved in what I am doing that I do not see myself as separate from what I am doing. |

---

## Resumen de bloques y estadísticos descriptivos

| Bloque | N ítems | Escala | M global | DE global | M Colombia |
|--------|---------|--------|---------|-----------|------------|
| R (Riesgo) | 9 | 1–5 | 3.398 | 1.268 | 3.355 |
| EI (Intención Emprendedora) | 5 | 1–5 | 4.021 | 1.057 | 4.224 |
| EA (Actitudes Emprendedoras) | 8 | 1–5 | 4.065 | 1.019 | 4.299 |
| M (Mercado) | 2 | 1–5 | 2.115 | 0.973 | 2.024 |
| F (Financiamiento) | 2 | 1–5 | 2.688 | 1.059 | 2.756 |
| G (Gobierno) | 4 | 1–5 | 2.436 | 1.246 | 2.299 |
| S (Entorno Social) | 3 | 1–5 | 3.577 | 1.049 | 3.683 |
| U (Universidad general) | 3 | 1–5 | 3.479 | 1.101 | 3.943 |
| UI-1 (Infraestructura universitaria) | 1 | 1–5 | 3.470 | 1.087 | 4.073 |
| U-D (Desarrollo universitario) | 5 | 1–5 | 3.634 | 1.031 | 4.102 |
| U-AS (Apoyo académico) | 3 | 1–5 | 3.383 | 1.114 | 3.967 |
| LC (Locus de Control) | 8 | 1–5 | 3.315 | 1.136 | 3.396 |
| EAct (Acción Emprendedora) | 16 | 1–5 | 2.871 | 1.312 | 2.733 |
| FK (Conocimiento Financiero) | 8 | 1–5 | 3.709 | 1.089 | 3.534 |
| EC-SA (Autoconciencia) | 3 | 1–5 | 4.070 | 0.924 | 4.293 |
| EC-SR (Autorregulación) | 4 | 1–5 | 4.124 | 0.939 | 4.341 |
| EC-M (Motivación) | 4 | 1–5 | 4.022 | 0.941 | 4.274 |
| EC-E (Empatía) | 5 | 1–5 | 3.993 | 0.912 | 4.259 |
| EC-SS (Habilidades Sociales) | 5 | 1–5 | 3.819 | 0.969 | 4.176 |
| SE (Autoeficacia Emprendedora) | 5 | 1–5 | 3.839 | 0.945 | 3.907 |
| CL (Carga Cognitiva) | 12 | 1–5 | 3.282 | 1.100 | 3.476 |
| EW (Bienestar General) | 5 | **1–7** | 4.770 | 1.646 | 4.976 |
| FL (Estado de Flujo) | 6 | 1–5 | 2.949 | 1.195 | 2.797 |
| **TOTAL** | **131** | | | | |

*Nota: Los estadísticos se calculan sobre todos los valores disponibles sin imputación. N = 540 global; N = 41 Colombia.*

---

*Codebook creado: 2026-04-20. Actualizado: 2026-04-27. Country codes provistos por el investigador. Estadísticos calculados desde `data/processed/datos_encuesta_2025.csv`.*
