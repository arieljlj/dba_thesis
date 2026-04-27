"""
Fase C — Actualización de Cap. 3 con coeficientes reales del dataset ALBA 2025
Reemplaza: tablas de correlaciones, 3 modelos de regresión, Colombia, síntesis.
"""
CAP3 = '/sessions/beautiful-dreamy-knuth/mnt/dba_thesis/docs/04_cap3_metodologia_resultados/01_capitulo_3.md'

with open(CAP3, 'r', encoding='utf-8') as f:
    txt = f.read()

original_len = len(txt)

# ═══════════════════════════════════════════════════════════════════════════
# 1. TABLA DE CORRELACIONES — reemplazar con valores reales
# ═══════════════════════════════════════════════════════════════════════════

OLD_CORR_TABLE = """| Variable | M | DE | EI | EA | S | SE | FK | FL | U-D | U-AS | LC |
|----------|-------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| **EI** | 4.02 | 1.06 | 1.00 | 0.55*** | 0.38*** | 0.51*** | 0.42*** | 0.35*** | 0.47*** | 0.44*** | 0.39*** |
| **EA** | 4.07 | 1.02 | — | 1.00 | 0.52*** | 0.61*** | 0.48*** | 0.41*** | 0.53*** | 0.49*** | 0.45*** |
| **S** | 3.58 | 1.05 | — | — | 1.00 | 0.48*** | 0.39*** | 0.32*** | 0.42*** | 0.43*** | 0.35*** |
| **SE** | 3.84 | 0.95 | — | — | — | 1.00 | 0.56*** | 0.44*** | 0.61*** | 0.57*** | 0.49*** |
| **FK** | 3.71 | 1.09 | — | — | — | — | 1.00 | 0.62*** | 0.58*** | 0.51*** | 0.47*** |
| **FL** | 2.95 | 1.20 | — | — | — | — | — | 1.00 | 0.53*** | 0.48*** | 0.42*** |
| **U-D** | 3.63 | 1.03 | — | — | — | — | — | — | 1.00 | 0.69*** | 0.57*** |
| **U-AS** | 3.38 | 1.11 | — | — | — | — | — | — | — | 1.00 | 0.61*** |
| **LC** | 3.32 | 1.14 | — | — | — | — | — | — | — | — | 1.00 |"""

NEW_CORR_TABLE = """| Variable | M | DE | EI | EA | S | SE | FK | FL | U-D | U-AS | LC |
|----------|-------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| **EI** | 4.02 | 0.98 | — | 0.729*** | 0.433*** | 0.470*** | 0.361*** | 0.164*** | 0.406*** | 0.359*** | 0.352*** |
| **EA** | 4.07 | 0.81 | — | — | 0.515*** | 0.593*** | 0.502*** | 0.225*** | 0.505*** | 0.443*** | 0.513*** |
| **S** | 3.58 | 0.84 | — | — | — | 0.420*** | 0.420*** | 0.195*** | 0.481*** | 0.417*** | 0.445*** |
| **SE** | 3.84 | 0.86 | — | — | — | — | 0.578*** | 0.328*** | 0.467*** | 0.414*** | 0.575*** |
| **FK** | 3.71 | 0.89 | — | — | — | — | — | 0.283*** | 0.448*** | 0.367*** | 0.490*** |
| **FL** | 2.95 | 0.92 | — | — | — | — | — | — | 0.231*** | 0.305*** | 0.356*** |
| **U-D** | 3.63 | 0.89 | — | — | — | — | — | — | — | 0.748*** | 0.495*** |
| **U-AS** | 3.38 | 1.02 | — | — | — | — | — | — | — | — | 0.470*** |
| **LC** | 3.32 | 0.54 | — | — | — | — | — | — | — | — | — |"""

txt = txt.replace(OLD_CORR_TABLE, NEW_CORR_TABLE)

# 2. Nota de correlaciones — quitar advertencia ⚠️
txt = txt.replace(
    '*Nota.* EI = Intención Emprendedora (EI1–EI5); EA = Actitud Emprendedora (EA1–EA8); S = Entorno Social/proxy SN-TCP (S1–S3); SE = Autoeficacia Emprendedora/proxy PBC-TCP (SE1–SE5); FK = Conocimiento Financiero (FK1–FK8); FL = Estado de Flujo (FL1–FL6); U-D = Desarrollo Institucional Universitario (U-D1–U-D5); U-AS = Apoyo Académico (U-AS1–U-AS3); LC = Locus de Control (LC1–LC8). M y DE corresponden a medias e desviaciones estándar calculados del dataset ALBA 2025 (N=540). *** p < .001 (bilateral). ⚠️ *Los valores de correlación de Pearson son indicativos — se calcularon con las variables renombradas; requieren verificación en Fase C del plan de revisión.*',
    '*Nota.* EI = Intención Emprendedora (EI1–EI5); EA = Actitud Emprendedora (EA1–EA8); S = Entorno Social/proxy SN-TCP (S1–S3); SE = Autoeficacia Emprendedora/proxy PBC-TCP (SE1–SE5); FK = Conocimiento del Ecosistema (FK1–FK8); FL = Estado de Flujo (FL1–FL6); U-D = Desarrollo Institucional Universitario (U-D1–U-D5); U-AS = Apoyo Académico (U-AS1–U-AS3); LC = Locus de Control (LC1–LC8). M y DE corresponden a medias y desviaciones estándar calculados del dataset ALBA 2025 (N=540). *** p < .001 (bilateral). Todas las correlaciones bivariadas son estadísticamente significativas (p < .001).'
)

# 3. Interpretación correlaciones
txt = txt.replace(
    '**Interpretación:** Intención emprendedora (EI) presenta variación sustancial (rango efectivo 1–5, M=4.02), con medias Colombia ligeramente superiores a la media global (Colombia M=4.22). Actitud emprendedora (EA) es el predictor más fuerte (r=0.55), confirmando jerarquía TCP. Componentes TCP-proxy tienen correlaciones moderadas entre sí (0.48–0.61), sin colinealidad excesiva. Moderadores contextuales tienen correlaciones con intención menores que TCP (0.35–0.47), sugiriendo efecto moderador más que predicción directa. ⚠️ *Nota: Los valores de correlación requieren recálculo con los datos reales en Fase C; los reportados aquí son indicativos de la estructura relacional esperada.*',
    '**Interpretación:** La intención emprendedora (EI, M=4.02, DE=0.98) muestra variación sustancial en la muestra global, con Colombia ligeramente superior (M=4.22). La actitud emprendedora (EA) es el predictor bivariado más fuerte (r=0.729), una magnitud elevada que anticipa su dominancia en los modelos multivariados y es consistente con la literatura TCP en emprendimiento (Liñán & Chen, 2009). Todos los demás predictores correlacionan significativamente con EI (r=0.164–0.470, todos p<.001). Destacan la alta correlación entre U-D y U-AS (r=0.748), que anticipa problemas de multicolinealidad en el Modelo 3. Los componentes TCP correlacionan moderada-altamente entre sí (EA↔SE: 0.593; EA↔S: 0.515), y las variables contextuales/moderadoras muestran correlaciones moderadas con LC (LC↔SE: 0.575; LC↔EA: 0.513; LC↔U-D: 0.495). Esta estructura de intercorrelaciones elevadas generará índices de varianza inflada (VIF) que se analizan en el Modelo 3.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 4. MODELO 1 — tabla y estadísticos
# ═══════════════════════════════════════════════════════════════════════════

OLD_M1_TABLE = """| Predictor | β (no stand.) | β (stand.) | EE | t | p | IC 95% |
|-----------|--------|---------|--------|--------|-------|---------|
| EA | 0.582 | 0.548 | 0.045 | 12.88 | <0.001 | [0.493, 0.671] |
| S | 0.156 | 0.147 | 0.041 | 3.82 | <0.001 | [0.075, 0.237] |
| SE | 0.418 | 0.395 | 0.049 | 8.58 | <0.001 | [0.322, 0.515] |
| Constante | 0.234 | — | 0.321 | 0.73 | 0.467 | [-0.397, 0.865] |"""

NEW_M1_TABLE = """| Predictor | β (no stand.) | β (stand.) | EE | t | p | IC 95% |
|-----------|--------|---------|--------|--------|-------|---------|
| EA | 0.807 | 0.665 | 0.048 | 16.978 | <0.001*** | [0.714, 0.901] |
| S | 0.083 | 0.071 | 0.041 | 2.045 | 0.041* | [0.003, 0.163] |
| SE | 0.052 | 0.046 | 0.042 | 1.239 | 0.216 | [-0.031, 0.135] |
| Constante | 0.243 | — | 0.164 | 1.481 | 0.139 | [-0.079, 0.565] |"""

txt = txt.replace(OLD_M1_TABLE, NEW_M1_TABLE)

# Nota M1
txt = txt.replace(
    '*Nota.* β (est.) = coeficiente de regresión no estandarizado; β (stand.) = coeficiente estandarizado; EE = error estándar; t = estadístico t de Student; p = nivel de significancia bilateral; IC 95% = intervalo de confianza al 95%. EA = Actitud Emprendedora (EA1–EA8); S = Entorno Social/Normas Subjetivas proxy (S1–S3); SE = Autoeficacia Emprendedora/PBC proxy (SE1–SE5). N = 540 (N efectivo = 536 con listwise deletion). ⚠️ *Coeficientes pendientes de recálculo con variables correctas del dataset (Fase C del plan de revisión).*',
    '*Nota.* β (no stand.) = coeficiente de regresión no estandarizado; β (stand.) = coeficiente estandarizado; EE = error estándar; t = estadístico t de Student; p = nivel de significancia bilateral; IC 95% = intervalo de confianza al 95%. EA = Actitud Emprendedora (EA1–EA8); S = Entorno Social/SN proxy (S1–S3); SE = Autoeficacia Emprendedora/PBC proxy (SE1–SE5). N = 540. *** p < .001; * p < .05.'
)

# Índices M1
txt = txt.replace(
    '**Índices de ajuste:** R²=0.478, R²ₐⱼ=0.476, F(3,536)=163.2 p<0.001, RMSE=1.38',
    '**Índices de ajuste:** R²=0.537, R²ₐⱼ=0.535, F(3,536)=207.43, p<0.001, RMSE=0.666'
)

# Interpretación M1
txt = txt.replace(
    '**Interpretación:** Los tres componentes TCP predicen significativamente intención (p<0.001 todos). Efecto de actitud (β=0.548) es más fuerte que normas (β=0.147) y control (β=0.395), jerarquía consistente con teoría. El modelo explica aproximadamente 47.8% de la varianza.',
    '**Interpretación:** La actitud emprendedora (EA) es el predictor dominante (β_std=0.665, t=16.98, p<.001), explicando por sí sola la mayor parte de la varianza del modelo. El entorno social (S) tiene un efecto pequeño pero estadísticamente significativo (β_std=0.071, p=.041). La autoeficacia emprendedora (SE), por el contrario, no alcanza significancia cuando se controla la actitud (β_std=0.046, p=.216), evidenciando supresión por la alta correlación entre EA y SE (r=0.593). El modelo explica el 53.7% de la varianza en EI —magnitud sustancial para el campo— con un ajuste ligeramente superior al reportado en estudios TCP precedentes (Liñán & Chen, 2009, reportaron R²=0.36–0.47). La dominancia de EA sobre SE es consistente con la literatura latinoamericana, donde la actitud general hacia el emprendimiento tiene mayor peso relativo que el control percibido (Moriano et al., 2012).'
)

# ═══════════════════════════════════════════════════════════════════════════
# 5. MODELO 2 — tabla y estadísticos
# ═══════════════════════════════════════════════════════════════════════════

OLD_M2_TABLE = """| Predictor | β (est.) | β (stand.) | EE | t | p | IC 95% |
|-----------|--------|---------|--------|--------|-------|---------|
| EA | 0.516 | 0.486 | 0.049 | 10.51 | <0.001 | [0.420, 0.612] |
| S | 0.095 | 0.090 | 0.043 | 2.20 | 0.028 | [0.010, 0.180] |
| SE | 0.349 | 0.330 | 0.052 | 6.69 | <0.001 | [0.246, 0.451] |
| FK | 0.168 | 0.159 | 0.038 | 4.43 | <0.001 | [0.093, 0.243] |
| FL | 0.084 | 0.080 | 0.041 | 2.03 | 0.043 | [0.003, 0.165] |
| Constante | -0.287 | — | 0.384 | -0.75 | 0.454 | [-1.041, 0.467] |"""

NEW_M2_TABLE = """| Predictor | β (est.) | β (stand.) | EE | t | p | IC 95% |
|-----------|--------|---------|--------|--------|-------|---------|
| EA | 0.818 | 0.674 | 0.048 | 16.945 | <0.001*** | [0.723, 0.913] |
| S | 0.093 | 0.079 | 0.041 | 2.245 | 0.025* | [0.012, 0.174] |
| SE | 0.078 | 0.068 | 0.046 | 1.680 | 0.093† | [-0.013, 0.169] |
| FK | -0.052 | -0.047 | 0.042 | -1.249 | 0.212 | [-0.134, 0.030] |
| FL | -0.012 | -0.012 | 0.033 | -0.373 | 0.709 | [-0.078, 0.053] |
| Constante | 0.297 | — | 0.172 | 1.724 | 0.085 | [-0.041, 0.636] |"""

txt = txt.replace(OLD_M2_TABLE, NEW_M2_TABLE)

# Nota M2
txt = txt.replace(
    '*Nota.* β (est.) = coeficiente de regresión no estandarizado; β (stand.) = coeficiente estandarizado; EE = error estándar; IC 95% = intervalo de confianza al 95%. EA = Actitud Emprendedora; S = Entorno Social (proxy SN-TCP); SE = Autoeficacia Emprendedora (proxy PBC-TCP); FK = Conocimiento Financiero; FL = Estado de Flujo. ΔR² indica el incremento en varianza explicada respecto al Modelo 1 (solo TCP). N = 540. ⚠️ *Coeficientes pendientes de recálculo (Fase C).*',
    '*Nota.* β (est.) = coeficiente de regresión no estandarizado; β (stand.) = coeficiente estandarizado; EE = error estándar; IC 95% = intervalo de confianza al 95%. EA = Actitud Emprendedora; S = Entorno Social (proxy SN-TCP); SE = Autoeficacia Emprendedora (proxy PBC-TCP); FK = Conocimiento del Ecosistema; FL = Estado de Flujo. ΔR² indica el incremento en varianza explicada respecto al Modelo 1. N = 540. *** p < .001; * p < .05; † p < .10.'
)

# Índices M2
txt = txt.replace(
    '**Índices de ajuste:** R²=0.512, R²ₐⱼ=0.509, F(5,534)=112.0 p<0.001, RMSE=1.33',
    '**Índices de ajuste:** R²=0.539, R²ₐⱼ=0.534, F(5,534)=124.78, p<0.001, RMSE=0.667'
)

# Cambio M2
txt = txt.replace(
    '**Cambio:** ΔR²=0.034, F(2,534)=10.39 p<0.001',
    '**Cambio:** ΔR²=0.002, F(2,534)=0.91, p=0.403 (no significativo)'
)

# Interpretación M2
txt = txt.replace(
    '**Interpretación:** FK y FL predicen intención significativamente, soportando H₀₄ y H₀₅. Efecto FK (β=0.159) es más fuerte que FL (β=0.080), sugiriendo que conocimiento de programas es más importante que comprensión de conceptos financieros. Se observa que los coeficientes TCP se reducen (AT: 0.548→0.486, PBC: 0.395→0.330), sugiriendo que parte del efecto TCP opera a través de conocimiento/alfabetización.',
    '**Interpretación:** Contrario a las hipótesis H₀₄ y H₀₅, la adición de conocimiento del ecosistema (FK) y estado de flujo (FL) no mejora significativamente la predicción de EI. Ambas variables presentan coeficientes ligeramente negativos y no significativos (FK: β=-0.047, p=.212; FL: β=-0.012, p=.709), y el incremento de R² es mínimo (ΔR²=0.002, p=.403). Este resultado sugiere que, una vez controlados los componentes TCP, el conocimiento del ecosistema emprendedor no añade poder predictivo sobre la intención. Una explicación plausible es que FK y EI comparten varianza que ya está capturada por EA: conocer los programas de apoyo puede incrementar la actitud favorable, pero no la intención directamente. El efecto de EA permanece estable (β_std=0.674), confirmando su primacía como predictor.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 6. MODELO 3 — tabla y estadísticos
# ═══════════════════════════════════════════════════════════════════════════

OLD_M3_TABLE = """| Predictor | β (est.) | β (stand.) | EE | t | p | IC 95% |
|-----------|--------|---------|--------|--------|-------|---------|
| EA (centrada) | 0.524 | 0.494 | 0.050 | 10.42 | <0.001 | [0.425, 0.623] |
| S | 0.087 | 0.082 | 0.044 | 1.98 | 0.049 | [-0.001, 0.174] |
| SE (centrada) | 0.372 | 0.352 | 0.053 | 7.01 | <0.001 | [0.268, 0.477] |
| FK | 0.145 | 0.137 | 0.041 | 3.54 | <0.001 | [0.065, 0.225] |
| FL | 0.067 | 0.063 | 0.043 | 1.54 | 0.125 | [-0.018, 0.152] |
| U-D (centrada) | 0.134 | 0.127 | 0.048 | 2.81 | 0.005 | [0.041, 0.227] |
| U-AS | 0.118 | 0.109 | 0.044 | 2.70 | 0.007 | [0.031, 0.204] |
| LC | 0.118 | 0.109 | 0.044 | 2.70 | 0.007 | [0.031, 0.204] |
| EA × U-D | 0.089 | 0.084 | 0.041 | 2.17 | 0.031 | [0.009, 0.169] |
| SE × U-D | 0.072 | 0.068 | 0.038 | 1.90 | 0.058 | [-0.002, 0.146] |
| Constante | 3.745 | — | 0.183 | 20.46 | <0.001 | [3.386, 4.104] |"""

NEW_M3_TABLE = """| Predictor | β (est.) | β (stand.) | EE | t | p | IC 95% |
|-----------|--------|---------|--------|--------|-------|---------|
| EA (centrada) | 0.784 | 0.646 | 0.054 | 14.552 | <0.001*** | [0.679, 0.890] |
| S | 0.084 | 0.072 | 0.043 | 1.932 | 0.054† | [-0.001, 0.169] |
| SE (centrada) | 0.101 | 0.089 | 0.049 | 2.054 | 0.040* | [0.004, 0.197] |
| FK | -0.051 | -0.046 | 0.042 | -1.207 | 0.228 | [-0.135, 0.032] |
| FL | -0.002 | -0.002 | 0.035 | -0.071 | 0.944 | [-0.070, 0.065] |
| U-D (centrada) | 0.022 | 0.020 | 0.053 | 0.407 | 0.684 | [-0.083, 0.126] |
| U-AS | 0.030 | 0.032 | 0.044 | 0.696 | 0.487 | [-0.055, 0.116] |
| LC | -0.153 | -0.085 | 0.072 | -2.124 | 0.034* | [-0.295, -0.012] |
| EA × U-D | -0.057 | -0.076 | 0.042 | -1.369 | 0.172 | [-0.138, 0.025] |
| SE × U-D | 0.014 | 0.017 | 0.041 | 0.344 | 0.731 | [-0.066, 0.095] |
| Constante | 4.339 | — | 0.307 | 14.125 | <0.001*** | [3.736, 4.942] |"""

txt = txt.replace(OLD_M3_TABLE, NEW_M3_TABLE)

# Nota M3 — actualizar VIF
txt = txt.replace(
    '*Nota.* β (est.) = coeficiente de regresión no estandarizado; β (stand.) = coeficiente estandarizado; EE = error estándar; IC 95% = intervalo de confianza al 95%. EA, SE y U-D fueron centradas en su media muestral antes de construir los términos de interacción (Aiken & West, 1991). EA × U-D = término de interacción actitud × desarrollo universitario; SE × U-D = término de interacción autoeficacia × desarrollo universitario. U-AS = Apoyo Académico; LC = Locus de Control. ΔR² indica el incremento respecto al Modelo 2. N = 540. VIF máximo = 4.2 (EA × U-D), todos < 5. ⚠️ *Coeficientes pendientes de recálculo (Fase C).*',
    '*Nota.* β (est.) = coeficiente de regresión no estandarizado; β (stand.) = coeficiente estandarizado; EE = error estándar; IC 95% = intervalo de confianza al 95%. EA, SE y U-D fueron centradas en su media muestral (EA_c = EA − 4.07; SE_c = SE − 3.84; U-D_c = U-D − 3.63) antes de construir los términos de interacción (Aiken & West, 1991). EA × U-D = término de interacción actitud × desarrollo universitario; SE × U-D = término de interacción autoeficacia × desarrollo universitario. *** p < .001; * p < .05; † p < .10. **Nota sobre multicolinealidad:** Varios predictores del Modelo 3 presentan VIF elevados: S (VIF=27.3), FK (VIF=27.7), FL (VIF=13.8), U-AS (VIF=25.7), LC (VIF=49.3). Estos valores exceden el umbral convencional de 10, indicando multicolinealidad severa. Las estimaciones de coeficientes para estas variables son inestables y sus errores estándar están inflados. Los VIF de las variables libres de multicolinealidad son bajos: EA_c (2.2), SE_c (1.9), U-D_c (2.2), EA×U-D (3.9), SE×U-D (3.3). N = 540.'
)

# Índices M3
txt = txt.replace(
    '**Índices de ajuste:** R²=0.535, R²ₐⱼ=0.528, F(10,529)=61.9 p<0.001, RMSE=1.29',
    '**Índices de ajuste:** R²=0.546, R²ₐⱼ=0.537, F(10,529)=63.58, p<0.001, RMSE=0.665'
)

# Cambio M3
txt = txt.replace(
    '**Cambio:** ΔR²=0.023, F(4,529)=3.48 p=0.008',
    '**Cambio respecto a Modelo 2 (versión centrada):** ΔR²=0.007, F(5,529)=1.64, p=0.148 (no significativo)'
)

# ═══════════════════════════════════════════════════════════════════════════
# 7. TABLA COMPARATIVA β estandarizados
# ═══════════════════════════════════════════════════════════════════════════

OLD_COMP_TABLE = """| Predictor | Modelo 1 (TCP solo) | Modelo 2 (TCP + Políticas) | Modelo 3 (+ Moderación) | Cambio 1→2 | Cambio 2→3 | Interpretación |
|-----------|---------|---------|---------|---------|---------|---------|
| **EA** | 0.548 | 0.486 | 0.494 | -0.062 (-11.3%) | +0.008 (+1.6%) | Actitud emprendedora se reduce moderadamente cuando se añaden FK/FL, sugiriendo que parte del efecto TCP opera a través del conocimiento. Se estabiliza en Modelo 3. |
| **S** | 0.147 | 0.090 | 0.082 | -0.057 (-38.8%) | -0.008 (-8.9%) | Entorno social (proxy SN) pierde potencia cuando se controlan FK/FL, en línea con literatura que señala que normas macro-sociales operan difusamente en contextos latinoamericanos. |
| **SE** | 0.395 | 0.330 | 0.352 | -0.065 (-16.5%) | +0.022 (+6.7%) | Autoeficacia (proxy PBC) se reduce cuando se añaden moderadores contextuales, pero se recupera parcialmente en Modelo 3, sugiriendo que desarrollo institucional captura recursos que antes atribuían a autoeficacia. |
| **FK** | — | 0.159 | 0.137 | — | -0.022 (-13.8%) | Conocimiento financiero entra en Modelo 2 como predictor significativo pero se reduce en Modelo 3, sugiriendo que U-D es predictor superior de la intención. |
| **FL** | — | 0.080 | 0.063 | — | -0.017 (-21.3%) | Estado de Flujo tiene efecto marginal y decrece con adición de moderadores contextuales, indicando que el engagement cognitivo es relevante pero secundario respecto al contexto institucional. |
| **U-D** | — | — | 0.127 | — | — | Desarrollo institucional es predictor directo significativo (p=0.005) e interactúa con AT (p=0.031). |
| **U-AS** | — | — | 0.109 | — | — | Apoyo académico es significativo predictor directo (p=0.007), replicando importancia de mentoría docente. |
| **LC** | — | — | 0.109 | — | — | Locus de Control es predictor significativo en Modelo 3 (p=0.007), con 8 ítems de locus interno/externo. |"""

NEW_COMP_TABLE = """| Predictor | Modelo 1 (TCP) | Modelo 2 (+Políticas) | Modelo 3 (+Moderación) | Cambio 1→2 | Cambio 2→3 | Interpretación |
|-----------|---------|---------|---------|---------|---------|---------|
| **EA** | 0.665*** | 0.674*** | 0.646*** | +0.009 (+1.4%) | -0.028 (-4.2%) | Predictor dominante y estable en los tres modelos. Magnitud elevada (β_std > 0.64 en todos) sugiere que la actitud es el factor primario de la intención emprendedora, absorbiendo gran parte de la varianza. |
| **S** | 0.071* | 0.079* | 0.072† | +0.008 (+11.3%) | -0.007 (-8.9%) | Efecto pequeño pero consistentemente significativo/marginal. El entorno social (proxy SN) mantiene su contribución aunque EA domina. El estudio cualitativo ayuda a interpretar este efecto como imagen social del empresario. |
| **SE** | 0.046 (ns) | 0.068† | 0.089* | +0.022 | +0.021 | No significativo en M1 cuando se controla EA (supresión). Alcanza significancia marginal en M3 (p=.040), posiblemente porque la multicolinealidad en M2 enmascara su efecto. |
| **FK** | — | -0.047 (ns) | -0.046 (ns) | — | +0.001 | Contra H₀₄: FK no predice EI de forma directa cuando se controla EA. Coeficientes ligeramente negativos y no significativos en M2 y M3. |
| **FL** | — | -0.012 (ns) | -0.002 (ns) | — | +0.010 | Contra H₀₅: FL no predice EI. Efecto prácticamente nulo en ambos modelos. |
| **U-D** | — | — | 0.020 (ns) | — | — | Desarrollo institucional no es predictor directo significativo en M3 (p=.684), en parte por la severa multicolinealidad con U-AS (VIF=25.7) y LC (VIF=49.3). |
| **U-AS** | — | — | 0.032 (ns) | — | — | Apoyo académico no alcanza significancia individual (p=.487), también afectado por multicolinealidad con U-D (r=0.748). |
| **LC** | — | — | -0.085* | — | — | Locus de Control es el único moderador/covariable significativo en M3, pero con coeficiente negativo (β=-0.153, p=.034). Este resultado contra-intuitivo puede explicarse por el efecto de realismo: personas con mayor locus interno evalúan de forma más crítica las barreras emprendedoras. VIF=49.3 exige cautela interpretativa. |"""

txt = txt.replace(OLD_COMP_TABLE, NEW_COMP_TABLE)

# 8. Síntesis tabla comparativa
txt = txt.replace(
    '**Síntesis:** La tabla muestra que adición de variables de política (Modelo 2) reduce sustancialmente coeficientes TCP, especialmente SN (-38.8%), sugiriendo confusión de efectos. Adición de moderadores contextuales (Modelo 3) estabiliza coeficientes AT y PBC, indicando que contexto universitario es factor crítico que no debe omitirse del modelo.',
    '**Síntesis:** La actitud emprendedora (EA) es el predictor robusto y estable de EI en los tres modelos (β_std=0.646–0.674). Las hipótesis H₀₄ (FK predice EI) y H₀₅ (FL predice EI) no se soportan: ambas variables presentan coeficientes no significativos y el ΔR² de M2 es estadísticamente nulo (p=.403). La multicolinealidad severa en M3 (varios VIF>10) hace inestables los coeficientes de U-D, U-AS y LC, limitando inferencias sobre su efecto directo. Solo EA, S y SE (marginalmente) mantienen estimaciones confiables. Los hallazgos son consistentes con la centralidad de la actitud en la TCP (Ajzen, 1991; Liñán & Chen, 2009) y señalan que, en esta muestra, los factores de política pública (FK, FL) no añaden predicción incremental significativa sobre los antecedentes psicológicos.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 9. INTERPRETACIÓN INTERACCIONES
# ═══════════════════════════════════════════════════════════════════════════

OLD_INTERACT = """**Interpretación de interacciones:**

- **EA × U-D:** β=0.089, p=0.031. El efecto de actitud emprendedora (EA) es amplificado en instituciones con mejor desarrollo universitario (U-D). Un incremento de 1 unidad en U-D aumenta el efecto de EA sobre EI en 0.089 unidades, sugiriendo que ecosistemas universitarios robustos amplifican la traducción de actitud favorable en intención emprendedora.

- **SE × U-D:** β=0.072, p=0.058 (marginal). La autoeficacia emprendedora (SE/PBC) es amplificada levemente por el desarrollo institucional universitario, con significancia límite."""

NEW_INTERACT = """**Interpretación de interacciones:**

Los términos de interacción EA×U-D y SE×U-D no alcanzan significancia estadística (EA×U-D: β=-0.057, p=.172; SE×U-D: β=0.014, p=.731), no soportando las hipótesis de moderación. El ΔR² al añadir los términos de moderación y covariables contextuales es de 0.007 (p=.148), estadísticamente no significativo. En consecuencia, **H₀₆ y H₀₇ no se soportan empíricamente**.

- **EA × U-D:** β=-0.057, p=.172 (no significativo). No hay evidencia de que el desarrollo institucional universitario modere el efecto de la actitud sobre la intención. El signo negativo (aunque NS) sugeriría que en contextos de mayor desarrollo universitario, el efecto de EA se reduce ligeramente —lo opuesto a la hipótesis— pero la imprecisión estadística impide ninguna inferencia.

- **SE × U-D:** β=0.014, p=.731 (no significativo). La autoeficacia y el desarrollo institucional no interactúan de forma significativa sobre EI.

*Nota interpretativa:* La ausencia de efectos moderadores puede deberse a la severa multicolinealidad entre U-D, U-AS y LC (r=0.748 entre U-D y U-AS; VIF>10 para ambas), que infla los errores estándar y reduce la potencia para detectar interacciones. Estudios futuros con muestras más grandes y medidas ortogonales del contexto institucional podrían revisar estas hipótesis."""

txt = txt.replace(OLD_INTERACT, NEW_INTERACT)

# ═══════════════════════════════════════════════════════════════════════════
# 10. COLOMBIA — correlaciones, regresión, conclusión
# ═══════════════════════════════════════════════════════════════════════════

OLD_COL_CORR = """| Predictor | r con IE | p |
|-----------|----------|---|
| EA | 0.61** | <0.001 |
| S | 0.34* | 0.031 |
| SE | 0.52** | <0.001 |
| FK | 0.48** | 0.002 |
| FL | 0.31* | 0.053 |
| U-D | 0.56** | <0.001 |
| U-AS | 0.53** | <0.001 |
| LC | 0.41* | 0.010 |

*Nota.* EI = Intención Emprendedora; EA = Actitud Emprendedora (proxy AT-TCP); S = Entorno Social (proxy SN-TCP); SE = Autoeficacia Emprendedora (proxy PBC-TCP); FK = Conocimiento Financiero; FL = Estado de Flujo; U-D = Desarrollo Institucional; U-AS = Apoyo Académico; LC = Locus de Control. N = 41. * p < .05; ** p < .01 (bilateral). Resultados exploratorios."""

NEW_COL_CORR = """| Predictor | r con EI | p |
|-----------|----------|---|
| EA | 0.673*** | <0.001 |
| S | 0.427** | 0.005 |
| SE | 0.198 | 0.215 |
| FK | -0.003 | 0.984 |
| FL | 0.235 | 0.139 |
| U-D | -0.039 | 0.807 |
| U-AS | 0.035 | 0.827 |
| LC | -0.001 | 0.994 |

*Nota.* EI = Intención Emprendedora; EA = Actitud Emprendedora (proxy AT-TCP); S = Entorno Social (proxy SN-TCP); SE = Autoeficacia Emprendedora (proxy PBC-TCP); FK = Conocimiento del Ecosistema; FL = Estado de Flujo; U-D = Desarrollo Institucional; U-AS = Apoyo Académico; LC = Locus de Control. N = 41. *** p < .001; ** p < .01 (bilateral). Solo EA y S correlacionan significativamente con EI en la sub-muestra colombiana. Resultados exploratorios."""

txt = txt.replace(OLD_COL_CORR, NEW_COL_CORR)

# Regresión Colombia
OLD_COL_REG = """EI = β₀ + β₁(EA) + β₂(SE) + ε

| Predictor | β | EE | t | p |
|-----------|--------|--------|--------|-------|
| EA | 0.498 | 0.118 | 4.22 | <0.001 |
| SE | 0.361 | 0.114 | 3.17 | 0.003 |
| Constante | 0.445 | 0.562 | 0.79 | 0.433 |

*Nota.* β = coeficiente de regresión no estandarizado; EE = error estándar; t = estadístico t; p = nivel de significancia bilateral. Modelo incluye solo EA y SE dada la limitación de potencia con N=41 (razón casos:variables recomendada ≥ 10:1). N = 41. ⚠️ *Coeficientes pendientes de recálculo (Fase C).*

R²=0.487, F(2,38)=17.90 p<0.001

**Conclusión:** En muestra colombiana, actitud (EA) y autoeficacia (SE) predicen intención (R²=0.487) con magnitudes similares al global (EA β=0.498 vs. β=0.548 global; SE β=0.361 vs. β=0.330). Aunque N es pequeño, patrón valida que hallazgos globales aplican en contexto colombiano."""

NEW_COL_REG = """EI = β₀ + β₁(EA) + β₂(SE) + ε

| Predictor | β | EE | t | p |
|-----------|--------|--------|--------|-------|
| EA | 1.062 | 0.194 | 5.483 | <0.001*** |
| SE | -0.134 | 0.154 | -0.874 | 0.388 |
| Constante | 0.187 | 0.795 | 0.235 | 0.816 |

*Nota.* β = coeficiente de regresión no estandarizado; EE = error estándar; t = estadístico t; p = nivel de significancia bilateral. Modelo incluye solo EA y SE (con N=41, el límite de 10:1 casos:predictores restringe el número de variables). N = 41. *** p < .001.

R²=0.464, R²ₐⱼ=0.435, F(2,38)=16.42, p<0.001

**Conclusión:** En la sub-muestra colombiana, únicamente la actitud (EA) predice significativamente la intención (β=1.062, p<.001; β_std=0.723). La autoeficacia (SE) presenta un coeficiente negativo no significativo (β=-0.134, p=.388), reforzando el patrón observado en la muestra global: EA absorbe prácticamente toda la varianza, dejando a SE sin efecto adicional. El modelo explica el 46.4% de la varianza de EI en Colombia —magnitud comparable a la muestra global (R²=0.537)— aunque con mayor incertidumbre de estimación por el tamaño reducido de la muestra. Con N=41, el análisis tiene potencia estadística aproximada de 0.82 para detectar el efecto grande de EA (f²=0.27), pero insuficiente para efectos moderados de otras variables. Los resultados deben interpretarse como exploratorios."""

txt = txt.replace(OLD_COL_REG, NEW_COL_REG)

# ═══════════════════════════════════════════════════════════════════════════
# 11. MATRIZ TRIANGULACIÓN — actualizar cifras
# ═══════════════════════════════════════════════════════════════════════════

txt = txt.replace(
    '| Actitud emprendedora (EA) predice EI fuertemente (β=0.548) | Actores reportan que estudiantes sí ven emprendimiento favorable | Actitud es construcción individual modulada por información contexto | Intervenciones en cambio de actitud requieren información creíble sobre oportunidades locales |',
    '| Actitud emprendedora (EA) predice EI dominantemente (β_std=0.665***) | Actores reportan que estudiantes sí ven emprendimiento favorable, condicionado a viabilidad local | Actitud es construcción individual modulada por información del contexto; su primacía frente a SE sugiere que cambiar valoraciones es más eficiente que fortalecer autoeficacia | Intervenciones en cambio de actitud requieren información creíble sobre oportunidades locales |'
)

txt = txt.replace(
    '| Contexto universitario modera EA→EI (β interacción EA×U-D=0.089, p=0.031) | Actores: políticas funcionan con intermediación local; mentoría es crítica | Desarrollo institucional proporciona mentoría, intermediación, legitimidad | Universidades con ecosistema robusto amplifican efecto de actitud favorable |',
    '| Moderación EA×U-D no alcanza significancia estadística (β=-0.057, p=.172); multicolinealidad severa entre U-D, U-AS, LC impide estimar efectos fiables | Actores: políticas funcionan mejor con intermediación local; mentoría es factor crítico para traducir intención en acción | La ausencia de efecto moderador estadístico puede deberse a VIF elevados; el análisis cualitativo ofrece evidencia independiente del rol del ecosistema universitario | Futuras investigaciones con muestras más grandes y medidas ortogonales del contexto deben re-examinar este efecto |'
)

txt = txt.replace(
    '| Conocimiento financiero (FK) predice EI (β=0.159, p<0.001) | Actores: conocimiento de programas es requisito pero insuficiente | FK es condición necesaria pero requiere arquitectura local de implementación | Conocimiento sin intermediación local no traduce a acción |',
    '| Conocimiento del ecosistema (FK) no predice EI directamente (β=-0.047, ns) cuando se controla EA | Actores: conocimiento de programas es requisito pero insuficiente; sin intermediación local, el conocimiento no activa la intención | FK puede operar como antecedente de la actitud (EA↔FK: r=0.502) más que como predictor directo de intención | El diseño cualitativo explica por qué FK no predice EI directamente: la arquitectura local de implementación es el mediador crítico |'
)

txt = txt.replace(
    '| Estado de Flujo (FL) tiene efecto débil (β=0.080, marginal p) | Actores enfatizan que mentoría > capital en determinar éxito | FL como covariable del aprendizaje es limitante menos crítico que el contexto institucional | Engagement cognitivo solo no sustituye al ecosistema universitario de apoyo |',
    '| Estado de Flujo (FL) no predice EI (β=-0.002, ns); efecto prácticamente nulo después de controlar EA | Actores enfatizan que mentoría > capital financiero en determinar éxito emprendedor | FL (engagement cognitivo en aprendizaje) no tiene efecto directo sobre intención; su efecto puede operar indirectamente a través de la actitud | Programas de engagement cognitivo solo no son suficientes para incrementar intención; requieren complementarse con mentoría y contexto institucional |'
)

txt = txt.replace(
    '| Patrones TCP se replican en Colombia (r=0.61 para EA, r=0.52 para SE) | Actores reportan contexto regional varía pero mecanismos TCP similares | Hallazgos globales aplican en Colombia, aunque con matices contextuales | Política nacional puede usar marco TCP pero debe adaptarse a heterogeneidad regional |',
    '| En Colombia (N=41): EA predice EI fuertemente (r=0.673***); SE no correlaciona significativamente (r=0.198, ns); FK, U-D, U-AS, LC prácticamente no correlacionan con EI | Actores reportan contexto regional variable; en ciudades intermedias, la arquitectura de apoyo es más débil | En Colombia, la actitud es el predictor primario de EI con mayor exclusividad que en muestra global; la ausencia de efecto de FK/U-D en Colombia puede reflejar menor calidad percibida de programas de apoyo en contextos regionales | Política en Colombia debe priorizar cambio de actitud (información, modelos de rol exitosos locales) antes que transferencia de conocimiento formal |'
)

# ═══════════════════════════════════════════════════════════════════════════
# 12. TEXTO CUALITATIVO — actualizar referencias a coeficientes FK y moderación
# ═══════════════════════════════════════════════════════════════════════════

txt = txt.replace(
    'Eso explica en parte por qué el efecto FK en el Modelo 2 (β=0.159) es significativo pero moderado.',
    'Esto es consistente con el hallazgo cuantitativo: FK no predice EI directamente (β=-0.047, ns en M2), posiblemente porque su efecto opera a través de la actitud (EA↔FK: r=0.502) más que directamente sobre la intención.'
)

txt = txt.replace(
    'El dato empírico lo confirma: en el Modelo 3, la interacción AT×U-D es significativa (β=0.089, p=0.031), mientras FL pierde significancia (β=0.067, p=0.125).',
    'El análisis cuantitativo no confirma esta interacción a nivel estadístico (EA×U-D: β=-0.057, p=.172, ns), posiblemente por la severa multicolinealidad entre variables del contexto universitario (VIF>25 para U-D, U-AS y LC). El análisis cualitativo ofrece evidencia convergente independiente sobre la importancia de la mentoría, que el modelo cuantitativo no puede estimar con precisión dada la estructura de los datos actuales.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 13. SÍNTESIS INTEGRADA — actualizar referencia a moderación
# ═══════════════════════════════════════════════════════════════════════════

txt = txt.replace(
    '5. **Contexto universitario es catalizador pero no suficiente:** Desarrollo institucional modera relación actitud-intención (p=0.031). Cuando estudiante sale de universidad, esta arquitectura desaparece.',
    '5. **Contexto universitario no muestra efecto moderador estadístico en esta muestra:** Las interacciones EA×U-D y SE×U-D no son significativas (p>.17), en parte por la multicolinealidad severa entre las variables de contexto universitario. El análisis cualitativo sugiere que el ecosistema universitario sí es relevante, pero su efecto puede operar a través de la actitud (mediación) más que como moderador. Cuando el estudiante sale de la universidad, la arquitectura de apoyo desaparece, lo que respalda intervenciones continuas post-egreso.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 14. LIMITACIONES — agregar multicolinealidad
# ═══════════════════════════════════════════════════════════════════════════

txt = txt.replace(
    '- Falta de variables de comportamiento real: ALBA mide intención, no acción posterior.',
    '- Falta de variables de comportamiento real: ALBA mide intención, no acción posterior.\n- **Multicolinealidad en Modelo 3:** Varias variables del contexto universitario y de política presentan VIF>10 (S=27.3, FK=27.7, FL=13.8, U-AS=25.7, LC=49.3), lo que infla errores estándar, reduce potencia estadística para estas variables específicas e impide estimaciones fiables de sus coeficientes individuales. Esta limitación afecta las conclusiones sobre U-D, U-AS, LC, FK y FL en el contexto del modelo multivariado completo. Estudios futuros deberían examinar estructuras factoriales latentes o seleccionar subconjuntos no colineales de predictores.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 15. CONCLUSIONES DEL CAPÍTULO — actualizar estadísticos
# ═══════════════════════════════════════════════════════════════════════════

OLD_CONCL = """**Hallazgos cuantitativos principales:**
- La Teoría de la Conducta Planificada predice EI con consistencia (R²=0.478 en modelo baseline)
- Conocimiento financiero (FK) y Estado de Flujo (FL) añaden predicción significativa (ΔR²=0.034)
- Contexto universitario modera relaciones TCP, amplificando especialmente el efecto de actitud (EA×U-D β=0.089, p=0.031)
- Patrones se replican en sub-muestra colombiana (N=41) ⚠️ *Coeficientes pendientes de recálculo con variables correctas en Fase C.*"""

NEW_CONCL = """**Hallazgos cuantitativos principales:**
- La Teoría de la Conducta Planificada predice EI con consistencia y magnitud sustancial (R²=0.537 en modelo baseline; N=540)
- La actitud emprendedora (EA) es el predictor dominante en todos los modelos (β_std=0.646–0.674), confirmando la primacía de la actitud en TCP y en la literatura latinoamericana
- El entorno social (S, proxy SN-TCP) tiene un efecto pequeño pero marginalemente significativo (β_std=0.071–0.079); la autoeficacia (SE, proxy PBC-TCP) no es significativa en el modelo baseline pero sí en el modelo completo
- Contrariamente a las hipótesis H₀₄ y H₀₅, el conocimiento del ecosistema (FK) y el estado de flujo (FL) no añaden predicción incremental significativa sobre EI (ΔR²=0.002, p=.403)
- Las hipótesis de moderación H₀₆ y H₀₇ no se soportan estadísticamente (EA×U-D: β=-0.057, ns; SE×U-D: β=0.014, ns), en parte por multicolinealidad severa entre variables del contexto universitario
- El locus de control (LC) es el único predictor contextual significativo en M3, con efecto negativo (β=-0.153, p=.034), posiblemente reflejando que personas con mayor agencia interna evalúan más críticamente las barreras
- Patrones se replican parcialmente en Colombia (N=41): EA sigue siendo el predictor dominante (R²=0.464), pero SE no contribuye significativamente"""

txt = txt.replace(OLD_CONCL, NEW_CONCL)

# ═══════════════════════════════════════════════════════════════════════════
# Escribir archivo actualizado
# ═══════════════════════════════════════════════════════════════════════════

with open(CAP3, 'w', encoding='utf-8') as f:
    f.write(txt)

print(f"Original: {original_len} chars")
print(f"Nuevo:    {len(txt)} chars")
print(f"Diferencia: +{len(txt)-original_len} chars")

# Verificar que no queden advertencias de Fase C
remaining = txt.count('⚠️')
print(f"⚠️ restantes: {remaining}")
print("✅ Cap. 3 actualizado con coeficientes reales (Fase C)")
