---
bibliography: ../08_bibliografia/referencias.bib
csl: apa.csl
---

# Anexos

---

## Anexo A. Instrumento de recolección de datos — Dataset ALBA 2025

**Nombre del instrumento:** Cuestionario sobre Factores que Influyen en la Intención Emprendedora de Estudiantes de Escuelas de Negocios — ALBA 2025  
**Referencia del dataset:** Alba, M. (2025). *Dataset: Entrepreneurial Intention and Action in ACBSP-accredited Latin American Universities (2024–2025)*. Zenodo. https://doi.org/10.5281/zenodo.17702439  
**Plataforma de administración:** Google Forms / Qualtrics  
**Idiomas:** Español (muestras colombiana, peruana, ecuatoriana, paraguaya); inglés (muestra mexicana)  
**Tiempo de respuesta estimado:** 15–20 minutos  
**Escala de respuesta principal:** Likert 1–5 (1 = Muy en desacuerdo / 5 = Muy de acuerdo), salvo sección demográfica y escala de Bienestar General (EW, 1–7)  
**Variables en dataset:** 131 (5 sociodemográficas + 126 ítems de escala)  
**Población objetivo:** Estudiantes universitarios de pregrado en instituciones acreditadas por ACBSP en América Latina  
**Muestra total:** N = 540 (Perú = 100, México = 168, Ecuador = 147, Paraguay = 84, Colombia = 41)

*Nota sobre diseño mixto:* La operacionalización de los constructos de la Teoría del Comportamiento Planificado (TCP) incorpora tanto los ítems cuantitativos del cuestionario ALBA 2025 como la evidencia cualitativa derivada del análisis de entrevistas con actores del ecosistema emprendedor colombiano (ver Anexo C). En particular, las normas subjetivas (SN) y el control conductual percibido (PBC) se triangularon con los datos cualitativos para profundizar su interpretación contextual.

---

### Sección 1. Datos Sociodemográficos (5 variables)

| Variable CSV | Pregunta / Categorías |
|---|---|
| `Country` | País de la universidad (1=Perú, 2=México, 3=Ecuador, 4=Paraguay, 5=Colombia) |
| `Age` | Rango de edad (1=18–24; 2=25–39; 3=40–59; 4=60 o más) |
| `Semester` | Semestre cursado (1–9; 10=Otro) |
| `Exp` | ¿Ha tenido experiencia emprendedora? (1=Sí; 2=No) |
| `Gender` | Género (1=Femenino; 2=Masculino; 3=No binario; 4=Otro; 5=Prefiero no decirlo) |

*Nota:* El instrumento original incluye adicionalmente: universidad de pertenencia y si tomó un curso de emprendimiento; estas variables no forman columnas independientes en el dataset `datos_encuesta_2025.csv`.

---

### Sección 2. Percepción del Riesgo — R (9 ítems)

**Variables CSV:** R1–R9 | **Escala:** 1–5 | M global = 3.40 (DE = 1.27); Colombia M = 3.36

*Instrucción: Indique su nivel de acuerdo con las siguientes afirmaciones.*

| Código | Ítem |
|---|---|
| R1 | En los últimos seis meses hubo momentos en los que asumí riesgos. |
| R2 | Me gusta probar nuevas comidas, explorar nuevos lugares y vivir experiencias completamente nuevas. |
| R3 | Si le tengo miedo a algo, intentaré superar ese temor. |
| R4 | Nunca he tenido una cita a ciegas. *(ítem inverso)* |
| R5 | Nunca he viajado por una ruta desconocida. *(ítem inverso)* |
| R6 | No me gustan los deportes extremos. *(ítem inverso)* |
| R7 | Necesito saber la respuesta antes de realizar la pregunta. *(ítem inverso)* |
| R8 | Necesito conocer lo que ya se ha hecho antes de estar dispuesto a intentarlo yo mismo. *(ítem inverso)* |
| R9 | Solo me involucro en situaciones en las que conozco el resultado. *(ítem inverso)* |

---

### Sección 3. Intención Emprendedora — EI (5 ítems)

**Variables CSV:** EI1–EI5 | **Escala:** 1–5 | M global = 4.02 (DE = 1.06); Colombia M = 4.22

**Rol en TCP:** Variable dependiente (VD) en todos los modelos de regresión.

*Instrucción: Indique su nivel de acuerdo con las siguientes afirmaciones.*

| Código | Ítem |
|---|---|
| EI1 | Mi meta profesional es convertirme en emprendedor/a. |
| EI2 | Haré todo esfuerzo para comenzar y dirigir mi propio negocio. |
| EI3 | Estoy determinado/a a crear una empresa en el futuro. |
| EI4 | Pienso seriamente en comenzar una empresa. |
| EI5 | Tengo el firme propósito de comenzar una empresa algún día. |

**Scoring:** Promedio de EI1–EI5. Rango 1–5.

---

### Sección 4. Actitudes hacia el Emprendimiento — EA (8 ítems)

**Variables CSV:** EA1–EA8 | **Escala:** 1–5 | M global = 4.07 (DE = 1.02); Colombia M = 4.30

**Rol en TCP:** Actitud Emprendedora (AT). Variable independiente en los modelos de regresión.

*Instrucción: Indique su nivel de acuerdo con las siguientes afirmaciones.*

| Código | Ítem |
|---|---|
| EA1 | Deseo proveer oportunidades de trabajo. |
| EA2 | Deseo ser un agente de cambio en la sociedad. |
| EA3 | Deseo ganar reconocimiento y respeto como emprendedor/a. |
| EA4 | Me gusta liderar e influir a otros. |
| EA5 | Deseo tener un equilibrio y horarios flexibles para mi trabajo y vida privada. |
| EA6 | Me apasiona aprender. |
| EA7 | La alta tasa de desempleo me ha impulsado a pensar seriamente sobre comenzar mi propio negocio. |
| EA8 | Me gusta tener una posición elevada en la sociedad. |

**Scoring:** Promedio de EA1–EA8.

---

### Sección 5. Percepciones del Entorno de Negocios (23 ítems)

Esta sección se subdivide en ocho bloques que miden distintas dimensiones del entorno para el emprendimiento. Los ítems del bloque Social (S1–S3) corresponden parcialmente al constructo TCP de Normas Subjetivas (SN), complementado con evidencia cualitativa.

#### 5a. Mercado — M (2 ítems)

**Variables CSV:** M1–M2 | **Escala:** 1–5 | M global = 2.12; Colombia M = 2.02

| Código | Ítem |
|---|---|
| M1 | Los nuevos negocios enfrentan altas presiones competitivas de inmediato. |
| M2 | Es difícil encontrar una idea de negocio que no se haya realizado antes. |

#### 5b. Financiamiento — F (2 ítems)

**Variables CSV:** F1–F2 | **Escala:** 1–5 | M global = 2.69; Colombia M = 2.76

| Código | Ítem |
|---|---|
| F1 | Es fácil obtener capital de riesgo. |
| F2 | Los bancos no conceden crédito fácilmente a los nuevos negocios. |

#### 5c. Gobierno / Política Pública — G (4 ítems)

**Variables CSV:** G1–G4 | **Escala:** 1–5 | M global = 2.44; Colombia M = 2.30

| Código | Ítem |
|---|---|
| G1 | Existen subsidios suficientes disponibles para los nuevos negocios en este país. |
| G2 | El apoyo de consultores y servicios cualificados para nuevos negocios está disponible en este país. |
| G3 | Los trámites burocráticos para fundar un nuevo negocio son poco claros en este país. |
| G4 | Las leyes estatales (normas y reglamentos) son desfavorables para gestionar un negocio en este país. |

#### 5d. Entorno Social — S (3 ítems)

**Variables CSV:** S1–S3 | **Escala:** 1–5 | M global = 3.58; Colombia M = 3.68

**Rol en TCP:** Proxy de Normas Subjetivas (SN). La operacionalización completa del constructo SN triangula estos ítems con el análisis cualitativo (entrevistas con actores del ecosistema).

| Código | Ítem |
|---|---|
| S1 | Los empresarios tienen una imagen positiva en la sociedad en este país. |
| S2 | Los empresarios tienen responsabilidad social en sus negocios en este país. |
| S3 | Los empresarios deben contribuir a la sociedad en este país a través de sus negocios. |

#### 5e. Universidad — Preparación General — U (3 ítems)

**Variables CSV:** U1–U3 | **Escala:** 1–5 | M global = 3.48; Colombia M = 3.94

| Código | Ítem |
|---|---|
| U1 | Los cursos universitarios me preparan bien para trabajar de forma independiente. |
| U2 | Los cursos universitarios ayudan a desarrollar habilidades para trabajar de forma independiente. |
| U3 | Las asignaturas me preparan para ser creativo/a en el trabajo autónomo. |

#### 5f. Infraestructura de Apoyo al Emprendimiento — UI (1 ítem)

**Variable CSV:** UI-1 | **Escala:** 1–5 | M global = 3.47; Colombia M = 4.07

| Código | Ítem |
|---|---|
| UI-1 | La universidad proporciona una sólida red de inversores en nuevos negocios. |

#### 5g. Desarrollo Institucional Universitario — U-D (5 ítems)

**Variables CSV:** U-D1–U-D5 | **Escala:** 1–5 | M global = 3.63; Colombia M = 4.10

| Código | Ítem |
|---|---|
| U-D1 | La atmósfera creativa de la universidad nos inspira a desarrollar ideas para nuevos negocios. |
| U-D2 | Los cursos nos permiten centrarnos en la creación de nuevos productos o servicios. |
| U-D3 | Los cursos nos permiten definir el modelo de negocio de la nueva empresa. |
| U-D4 | Los cursos fomentan las habilidades sociales y de liderazgo que necesitan los empresarios. |
| U-D5 | Los cursos proporcionan a los estudiantes los conocimientos necesarios para crear un nuevo negocio. |

#### 5h. Apoyo Académico Universitario — U-AS (3 ítems)

**Variables CSV:** U-AS1–U-AS3 | **Escala:** 1–5 | M global = 3.38; Colombia M = 3.97

| Código | Ítem |
|---|---|
| U-AS1 | Mi universidad apoya la creación de equipos multidisciplinarios de estudiantes. |
| U-AS2 | La universidad promueve activamente los procesos de fundación de nuevos negocios. |
| U-AS3 | Existe apoyo de la universidad para la creación de nuevos negocios. |

---

### Sección 6. Competencias Emocionales — EC (21 ítems)

**Escala:** 1–5 | Cinco sub-dimensiones.

#### 6a. Autoconciencia — EC-SA (3 ítems)

**Variables CSV:** EC-SA1–EC-SA3 | M global = 4.07; Colombia M = 4.29

| Código | Ítem |
|---|---|
| EC-SA1 | Soy capaz de reconocer mis propias emociones y su efecto en mis acciones. |
| EC-SA2 | Soy consciente de mis propias fortalezas y limitaciones. |
| EC-SA3 | Tengo una gran confianza en mi valor propio y mi habilidad para hacer cualquier cosa. |

#### 6b. Autorregulación — EC-SR (4 ítems)

**Variables CSV:** EC-SR1–EC-SR4 | M global = 4.12; Colombia M = 4.34

| Código | Ítem |
|---|---|
| EC-SR1 | Tengo autorregulación. |
| EC-SR2 | Me considero una persona honesta y recta. |
| EC-SR3 | Soy capaz de tomar responsabilidad de mis acciones personales. |
| EC-SR4 | Me considero una persona flexible y capaz de enfrentar el cambio. |

#### 6c. Motivación — EC-M (4 ítems)

**Variables CSV:** EC-M1–EC-M4 | M global = 4.02; Colombia M = 4.27

| Código | Ítem |
|---|---|
| EC-M1 | Me siento cómodo/a y abierto/a a nuevas ideas, enfoques e información. |
| EC-M2 | Me gusta esforzarme por mejorar o alcanzar un determinado nivel de excelencia. |
| EC-M3 | Me comprometo a trabajar hacia los objetivos de un grupo u organización cuando me identifico con ellos. |
| EC-M4 | Actúo con rapidez para aprovechar las oportunidades. |

#### 6d. Empatía — EC-E (5 ítems)

**Variables CSV:** EC-E1–EC-E5 | M global = 3.99; Colombia M = 4.26

| Código | Ítem |
|---|---|
| EC-E1 | Soy perseverante en trabajar para lograr mis metas a pesar de los obstáculos. |
| EC-E2 | Soy capaz de entender los sentimientos y puntos de vista de otras personas. |
| EC-E3 | Reconozco la necesidad de progreso de otras personas y me gusta estimular sus habilidades. |
| EC-E4 | Soy capaz de anticipar, reconocer y satisfacer las necesidades de los demás. |
| EC-E5 | Me gusta aprovechar las oportunidades que ofrecen los distintos tipos de personas. |

#### 6e. Habilidades Sociales — EC-SS (5 ítems)

**Variables CSV:** EC-SS1–EC-SS5 | M global = 3.82; Colombia M = 4.18

| Código | Ítem |
|---|---|
| EC-SS1 | Soy consciente del estado emocional y las relaciones de poder subyacentes en un grupo. |
| EC-SS2 | Puedo utilizar medios efectivos de persuasión. |
| EC-SS3 | Sé escuchar y puedo transmitir un mensaje convincente. |
| EC-SS4 | Tengo la habilidad de negociar y resolver conflictos. |
| EC-SS5 | Soy capaz de inspirar y liderar equipos e individuos. |

---

### Sección 7. Locus de Control — LC (8 ítems)

**Variables CSV:** LC1–LC8 | **Escala:** 1–5 | M global = 3.32 (DE = 1.14); Colombia M = 3.40

*Instrucción: Indique su nivel de acuerdo con las siguientes afirmaciones.*

| Código | Ítem | Dirección |
|---|---|---|
| LC1 | Puedo anticipar las dificultades y tomar medidas para evitarlas. | Interno |
| LC2 | Gran parte de lo que me ocurre probablemente sea cuestión de suerte. | Externo |
| LC3 | Todo el mundo sabe que la suerte o el azar determinan nuestro destino. | Externo |
| LC4 | Solo puedo controlar mis problemas si tengo apoyo de otra persona. | Externo |
| LC5 | Cuando hago planes, estoy casi seguro de poder hacerlos funcionar. | Interno |
| LC6 | Tener éxito es cuestión de esfuerzo. La suerte tiene poco o nada que ver. | Interno |
| LC7 | Mi vida está controlada por acciones y eventos externos. | Externo |
| LC8 | Confío en que puedo enfrentarme con éxito a los problemas futuros. | Interno |

**Scoring:** Los ítems de locus externo (LC2, LC3, LC4, LC7) se revierten antes de promediar para obtener un índice de locus de control interno. M global = 3.32; Colombia M = 3.40.

---

### Sección 8. Acción Emprendedora — EAct (16 ítems)

**Variables CSV:** EAct1–EAct16 | **Escala:** 1–5 | M global = 2.87 (DE = 1.31); Colombia M = 2.73

*Instrucción: Indique su nivel de acuerdo con las siguientes afirmaciones.*

| Código | Ítem |
|---|---|
| EAct1 | He identificado oportunidades de mercado. |
| EAct2 | He preparado un plan de negocio. |
| EAct3 | He desarrollado modelos o procedimientos para un producto/servicio. |
| EAct4 | He elegido un nombre para el negocio. |
| EAct5 | Me dedico a tiempo completo al negocio. |
| EAct6 | He organizado un equipo para el inicio del negocio. |
| EAct7 | He creado una entidad legal para el negocio. |
| EAct8 | He registrado el negocio ante las autoridades fiscales. |
| EAct9 | He invertido parte de mi propio dinero en un negocio. |
| EAct10 | He solicitado y recibido apoyo financiero para iniciar mi negocio. |
| EAct11 | He conseguido la ubicación y el equipo necesarios para iniciar un negocio. |
| EAct12 | He comprado o arrendado la mayor parte del equipo, instalaciones y propiedades. |
| EAct13 | He comprado materias primas, inventarios y suministros. |
| EAct14 | He comenzado actividades de mercadeo y promoción. |
| EAct15 | He solicitado licencias o patentes. |
| EAct16 | He contratado empleados. |

**Scoring:** Promedio de EAct1–EAct16. Mide la brecha entre intención y acción emprendedora.

---

### Sección 9. Conocimiento Financiero — FK (8 ítems)

**Variables CSV:** FK1–FK8 | **Escala:** 1–5 | M global = 3.71 (DE = 1.09); Colombia M = 3.53

**Rol en investigación:** Variable moderadora; proxy de alfabetización financiera como dimensión de las políticas públicas de fomento al emprendimiento.

*Instrucción: Indique su nivel de acuerdo con las siguientes afirmaciones.*

| Código | Ítem |
|---|---|
| FK1 | Conozco sobre liquidez del activo. |
| FK2 | Conozco sobre planificación financiera personal. |
| FK3 | Conozco sobre patrones de gasto y ahorro. |
| FK4 | Conozco sobre interés compuesto. |
| FK5 | Conozco sobre certificados de depósito a términos. |
| FK6 | Conozco sobre razones para adquirir un seguro. |
| FK7 | Conozco sobre diversificación de la inversión. |
| FK8 | *(Ítem adicional presente en el dataset; confirmación de ítem pendiente con el equipo ALBA.)* |

*Nota:* El instrumento en inglés documenta 7 ítems FK; el dataset contiene 8 variables (FK1–FK8). El ítem FK8 (M = 4.13; Colombia M = 4.32) puede corresponder a una adaptación regional del cuestionario en español. Se recomienda verificación con el equipo de investigación ALBA antes de la publicación final.

---

### Sección 10. Autoeficacia Emprendedora — SE (5 ítems)

**Variables CSV:** SE1–SE5 | **Escala:** 1–5 | M global = 3.84 (DE = 0.95); Colombia M = 3.91

**Rol en TCP:** Control Conductual Percibido (PBC). Variable independiente en los modelos de regresión, complementada con evidencia cualitativa.

*Instrucción: Indique su nivel de acuerdo con las siguientes afirmaciones.*

| Código | Ítem |
|---|---|
| SE1 | Siento que soy capaz de definir una idea de negocio y una estrategia para una nueva empresa. |
| SE2 | Siento que soy capaz de escribir un plan de negocios (realizar investigación de mercado, análisis financiero, etc.). |
| SE3 | Siento que soy capaz de negociar y mantener relaciones de apoyo con bancos e inversores potenciales. |
| SE4 | Siento que soy capaz de reconocer oportunidades para el desarrollo de nuevos productos o servicios. |
| SE5 | Siento que soy capaz de establecer relaciones con personas clave para obtener el capital necesario para iniciar un nuevo negocio. |

**Scoring:** Promedio de SE1–SE5.

---

### Sección 11. Carga Cognitiva — CL (12 ítems)

**Variables CSV:** CL1–CL12 | **Escala:** 1–5 (con sub-escalas de dificultad, esfuerzo y concentración) | M global = 3.28 (DE = 1.10); Colombia M = 3.48

*Instrucción: Evalúe el programa de estudio o semestres cursados.*

| Código | Ítem |
|---|---|
| CL1 | El tema o los temas tratados fueron muy complejos. |
| CL2 | Los temas tratados incluían fórmulas que percibí como muy complejas. |
| CL3 | Los temas tratados incluían conceptos y definiciones que percibí como muy complejos. |
| CL4 | Las instrucciones o explicaciones fueron muy poco claras. |
| CL5 | Las instrucciones o explicaciones fueron, en términos de aprendizaje, muy ineficaces. |
| CL6 | Las instrucciones o explicaciones estaban llenas de lenguaje poco claro. |
| CL7 | Los temas tratados mejoraron realmente mi conocimiento y comprensión. *(ítem inverso)* |
| CL8 | Los temas tratados mejoraron realmente mi comprensión de conceptos y definiciones. *(ítem inverso)* |
| CL9 | El programa de estudios o los semestres que cursé me exigieron invertir un esfuerzo mental significativo. |
| CL10 | El programa de estudios o los semestres que cursé fueron... *(escala dificultad: 1=Muy fácil / 5=Muy difícil)* |
| CL11 | Aprender del programa de estudios o los semestres que cursé fue... *(escala dificultad: 1=Muy fácil / 5=Muy difícil)* |
| CL12 | ¿Cuánto se concentró durante el programa de estudio o los semestres que cursó? *(1=Muy poco / 5=Mucho; ítem inverso de carga)* |

---

### Sección 12. Bienestar General y Satisfacción con la Vida — EW (5 ítems)

**Variables CSV:** EW1–EW5 | **Escala:** 1–7 *(excepción: escala diferente a las demás secciones)* | M global = 4.77 (DE = 1.65); Colombia M = 4.98

*Instrucción: A continuación hay cinco afirmaciones con las cuales usted puede estar de acuerdo o en desacuerdo. Seleccione la respuesta que mejor describa su grado de acuerdo (1 = Fuertemente en desacuerdo; 7 = Fuertemente de acuerdo).*

| Código | Ítem |
|---|---|
| EW1 | En la mayoría de los aspectos, mi vida se acerca a mi ideal. |
| EW2 | Las condiciones de mi vida son excelentes. |
| EW3 | Estoy completamente satisfecho/a con mi vida. |
| EW4 | Hasta ahora, he conseguido las cosas más importantes que quiero en la vida. |
| EW5 | Si pudiera vivir mi vida de nuevo, no cambiaría casi nada. |

---

### Sección 13. Estado de Flujo — FL (6 ítems)

**Variables CSV:** FL1–FL6 | **Escala:** 1–5 | M global = 2.95 (DE = 1.20); Colombia M = 2.80

**Rol en investigación:** Variable moderadora; mide el nivel de engagement cognitivo y emocional del estudiante con sus estudios, que puede mediar la relación entre el entorno universitario y la intención emprendedora.

*Instrucción: Indique su nivel de acuerdo con las siguientes afirmaciones.*

| Código | Ítem |
|---|---|
| FL1 | Mi mente no divaga. Estoy totalmente involucrado/a en lo que estoy haciendo y no estoy pensando en nada más. |
| FL2 | Mi cuerpo se siente bien. El mundo parece estar separado de mí. |
| FL3 | Soy menos consciente de mí mismo/a y de mis problemas. |
| FL4 | Mi concentración es como respirar — nunca pienso en ello. |
| FL5 | Cuando inicio algo, realmente dejo fuera el mundo. |
| FL6 | Estoy tan involucrado/a en lo que estoy haciendo que no me veo como algo separado de lo que hago. |



## Anexo B. Matriz de Operacionalización de Variables

La matriz de operacionalización completa se desarrolla en la sección 3.1 del Capítulo 3. Se reproduce aquí en versión de referencia rápida. Los constructos del TCP corresponden a las siguientes variables del dataset ALBA 2025.

| Constructo / Variable | Rol en investigación | Código CSV | N ítems | Escala | M global | M Colombia |
|---|---|---|---|---|---|---|
| Intención Emprendedora (EI) | **Dependiente** (TCP) | EI1–EI5 | 5 | 1–5 | 4.02 | 4.22 |
| Actitud Emprendedora (AT → EA) | Independiente (TCP) | EA1–EA8 | 8 | 1–5 | 4.07 | 4.30 |
| Normas Subjetivas (SN → S)* | Independiente (TCP) | S1–S3 | 3 | 1–5 | 3.58 | 3.68 |
| Control Conductual Percibido (PBC → SE)* | Independiente (TCP) | SE1–SE5 | 5 | 1–5 | 3.84 | 3.91 |
| Conocimiento Financiero (FK) | Moderadora / Proxy PP | FK1–FK8 | 8 | 1–5 | 3.71 | 3.53 |
| Desarrollo Institucional Universitario (U-D) | Moderadora / Contexto | U-D1–U-D5 | 5 | 1–5 | 3.63 | 4.10 |
| Apoyo Académico Universitario (U-AS) | Moderadora / Contexto | U-AS1–U-AS3 | 3 | 1–5 | 3.38 | 3.97 |
| Locus de Control (LC) | Moderadora / Covariable | LC1–LC8 | 8 | 1–5 | 3.32 | 3.40 |
| Estado de Flujo (FL) | Moderadora / Covariable | FL1–FL6 | 6 | 1–5 | 2.95 | 2.80 |
| Percepción del Riesgo (R) | Covariable | R1–R9 | 9 | 1–5 | 3.40 | 3.36 |
| Autoeficacia Emprendedora (SE) | Covariable / PBC proxy | SE1–SE5 | 5 | 1–5 | 3.84 | 3.91 |
| Entorno de mercado (M) | Covariable contexto | M1–M2 | 2 | 1–5 | 2.12 | 2.02 |
| Entorno de financiamiento (F) | Covariable contexto | F1–F2 | 2 | 1–5 | 2.69 | 2.76 |
| Entorno gubernamental (G) | Covariable contexto | G1–G4 | 4 | 1–5 | 2.44 | 2.30 |
| Entorno social (S) | Proxy SN (TCP) | S1–S3 | 3 | 1–5 | 3.58 | 3.68 |
| Acción Emprendedora (EAct) | Variable de resultado secundaria | EAct1–EAct16 | 16 | 1–5 | 2.87 | 2.73 |
| Competencias Emocionales (EC) | Covariable | EC-SA/SR/M/E/SS | 21 | 1–5 | 4.00 | 4.26 |
| Carga Cognitiva (CL) | Covariable | CL1–CL12 | 12 | 1–5 | 3.28 | 3.48 |
| Bienestar General (EW) | Covariable | EW1–EW5 | 5 | **1–7** | 4.77 | 4.98 |

*Los constructos SN y PBC del TCP se operacionalizan mediante triangulación mixta: ítems cuantitativos del cuestionario ALBA 2025 + evidencia cualitativa de entrevistas con actores del ecosistema colombiano.

**Fuente:** Dataset ALBA 2025 (Alba, 2025). N = 540 global; N = 41 Colombia. Escala principal Likert 1–5, salvo EW (1–7).  
**Marco teórico:** Teoría del Comportamiento Planificado (Ajzen, 1991); extensiones de ecosistema (Stam & van de Ven, 2021).  
**Documento fuente completo:** `docs/04_cap3_metodologia_resultados/markdown_from_excel/Matriz_Operacionalizacion_Variables_DBA-1_Matriz_de_Operacionalización.md`


---

## Anexo C. Protocolo de Codificación Cualitativa

**Investigador:** Jorge Ariel Loaiza Loaiza  
**Período de procesamiento:** Noviembre 2024 – marzo 2026  
**Corpus total:** 62 documentos — 38 transcripciones de videos YouTube + 24 documentos institucionales (~280,000 palabras)  
**Herramienta:** Python 3.11 (NLTK, spaCy, pandas); scripts en `code/analysis/`

---

### C.1. Fuentes del corpus

**Fuente 1 — Videos YouTube (n = 38)**

Actores del ecosistema colombiano de emprendimiento, período 2016–2026: funcionarios del Ministerio de Comercio, Industria y Turismo; directivos de iNNpulsa Colombia; líderes del SENA; emprendedores con trayectoria documentada; académicos del área de emprendimiento. Extracción: Apify YouTube Scraper (2024). Criterios de selección: relevancia temática al ecosistema colombiano, duración ≥ 10 minutos, publicación posterior a 2015.

**Fuente 2 — Documentos institucionales (n = 24)**

Reportes, comunicados, lineamientos y artículos de: iNNpulsa Colombia, Ministerio de Comercio (MinCIT), SENA, universidades colombianas con programas de emprendimiento, medios especializados (2015–2026). Extracción mediante web scraping automatizado de fuentes de acceso abierto.

---

### C.2. Preguntas cualitativas de investigación

| PQ | Pregunta | OE vinculado |
|---|---|---|
| PQ1 | ¿Cómo describen los actores del ecosistema los factores que impulsan o frenan la intención emprendedora de los estudiantes universitarios? | OE1, OE2 |
| PQ2 | ¿A través de qué mecanismos perciben los actores que las políticas públicas influyen en la intención emprendedora? | OE3 |
| PQ3 | ¿Cómo explican los actores la brecha entre intención emprendedora declarada y comportamiento emprendedor observable? | OE4, OE5 |

---

### C.3. Sistema de codificación

#### Códigos deductivos

**Bloque PQ1 — Validación de constructos TCP:**

| Código | Descripción | Ejemplo ilustrativo |
|---|---|---|
| TCP_Actitud | Fragmentos sobre disposiciones y valoraciones del emprendimiento como opción de carrera | "Los jóvenes colombianos sí quieren emprender... el problema no es la actitud" |
| TCP_Normas | Fragmentos sobre presión social, apoyo familiar/institucional, legitimidad social | "La familia todavía ve el empleo formal como lo seguro" |
| TCP_Control | Fragmentos sobre capacidades percibidas, acceso a recursos, barreras concretas | "El crédito es la barrera número uno para el emprendedor joven" |
| PP_Habilitador | Políticas públicas mencionadas como habilitadoras de intención o acción | "El Fondo Emprender cambió la mentalidad de muchos estudiantes del SENA" |

**Bloque PQ2 — Mecanismos de políticas:**

| Código | Descripción |
|---|---|
| PP_Información | Las políticas influyen mediante acceso a información sobre programas y recursos |
| PP_Barreras | Las políticas reducen barreras percibidas (financieras, regulatorias, informacionales) |
| PP_Actitud | Las políticas modifican la valoración del emprendimiento (eventos, narrativas públicas) |
| PP_Intermediación | Las políticas influyen a través de actores locales que median entre marcos nacionales y realidad estudiantil |
| PP_Brecha | Las políticas son percibidas como insuficientes para cerrar la brecha intención-acción |

**Bloque PQ3 — Brecha intención-acción:**

| Código | Descripción |
|---|---|
| BA_Financiero | Barrera: falta de acceso a capital o crédito |
| BA_Regulatorio | Barrera: complejidad de trámites de formalización |
| BA_CapitalHumano | Barrera: falta de mentores, redes o conocimiento empresarial |
| BA_Psicológico | Barrera: miedo al fracaso, deseabilidad social, inseguridad |
| MA_Mentoría | Mecanismo de apoyo: mentoría continuada como factor de transición intención-acción |
| MA_Redes | Mecanismo de apoyo: acceso a redes empresariales y capital social |
| BA_Regional | Variación regional: acceso desigual a recursos según ubicación geográfica |

#### Códigos inductivos emergentes

Identificados en primeras 15 unidades del corpus, tras saturación temática:

| Código | Descripción | Frecuencia en corpus |
|---|---|---|
| IND_Corrupción | Percepción de captura política o clientelismo en asignación de recursos | 4 documentos |
| IND_Formalización_Trampa | Formalización como barrera estructural para microempresarios de necesidad | 7 documentos |
| IND_Heterogeneidad_Regional | Diferencias pronunciadas entre Bogotá y ciudades intermedias/periféricas | 12 documentos |
| IND_Género | Barreras específicas para mujeres emprendedoras (legitimidad, redes, capital) | 5 documentos |

---

### C.4. Proceso de codificación

**Paso 1 — Preparación del corpus:** Extracción, limpieza y normalización de texto. Archivado individual por documento en `.txt` con metadatos (fuente, fecha, actor, tipo).

**Paso 2 — Codificación deductiva:** Aplicación automatizada de códigos PQ1–PQ3 mediante scripts Python. Extracción de fragmentos de ±50 palabras alrededor de términos activadores. Revisión manual de los 200 fragmentos de mayor relevancia por código.

**Paso 3 — Codificación inductiva:** Revisión de 15 documentos seleccionados intencionalmente (variedad de actores y fechas). Generación de 4 códigos inductivos emergentes por saturación temática.

**Paso 4 — Validación intercoder (κ de Cohen):** Selección aleatoria del 10% del corpus (6 videos). Codificación independiente por segundo codificador con instrucciones mínimas. Cálculo de κ mediante matriz de confusión.

| Código evaluado | κ | Interpretación |
|---|---|---|
| TCP_Actitud | 0.78 | Sustancial |
| TCP_Control | 0.72 | Sustancial |
| PP_Intermediación | 0.71 | Sustancial |
| BA_Regional | 0.76 | Sustancial |
| **κ global promedio** | **0.74** | **Sustancial** (Landis & Koch, 1977) |

*Umbral para análisis cualitativo riguroso: κ ≥ 0.60. El κ = 0.74 supera este umbral en todas las categorías.*

**Paso 5 — Síntesis temática:** Agrupación de fragmentos codificados en categorías interpretativas. Redacción de memos analíticos por tema. Construcción de la Matriz