"""
Fase C — Re-análisis de Regresión Jerárquica
Tesis DBA: Intención Emprendedora (EI) — Jorge Ariel Loaiza Loaiza
Dataset: datos_encuesta_2025.csv (N=540, ALBA 2025)
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
warnings.filterwarnings('ignore')

CSV = '/sessions/beautiful-dreamy-knuth/mnt/dba_thesis/data/processed/datos_encuesta_2025.csv'
df_raw = pd.read_csv(CSV)
print(f"Dataset: {df_raw.shape[0]} filas x {df_raw.shape[1]} columnas")
print(f"Códigos de país: {df_raw['Country'].value_counts().to_dict()}")

# ── Compuestos ────────────────────────────────────────────────────────────

def comp(cols):
    return df_raw[cols].apply(pd.to_numeric, errors='coerce').mean(axis=1)

EI  = comp(['EI1','EI2','EI3','EI4','EI5'])
EA  = comp(['EA1','EA2','EA3','EA4','EA5','EA6','EA7','EA8'])
S   = comp(['S1','S2','S3'])
SE  = comp(['SE1','SE2','SE3','SE4','SE5'])
FK  = comp(['FK1','FK2','FK3','FK4','FK5','FK6','FK7','FK8'])
FL  = comp(['FL1','FL2','FL3','FL4','FL5','FL6'])
UD  = comp(['U-D1','U-D2','U-D3','U-D4','U-D5'])
UAS = comp(['U-AS1','U-AS2','U-AS3'])
LC  = comp(['LC1','LC2','LC3','LC4','LC5','LC6','LC7','LC8'])

data = pd.DataFrame({
    'EI':EI,'EA':EA,'S':S,'SE':SE,
    'FK':FK,'FL':FL,'UD':UD,'UAS':UAS,'LC':LC,
    'Country': df_raw['Country']
}).dropna(subset=['EI','EA','S','SE','FK','FL','UD','UAS','LC'])

N_total = len(data)
print(f"\nN efectivo (listwise completo): {N_total}")

# Medias globales
M = {v: data[v].mean() for v in ['EI','EA','S','SE','FK','FL','UD','UAS','LC']}
SD = {v: data[v].std() for v in ['EI','EA','S','SE','FK','FL','UD','UAS','LC']}

print("\n── Medias y DE (global) ──")
labels_long = {'EI':'EI (Intención)','EA':'EA (Actitud)','S':'S  (Entorno Social)',
               'SE':'SE (Autoeficacia)','FK':'FK (Conocimiento)','FL':'FL (Estado de Flujo)',
               'UD':'U-D (Desarrollo Inst.)','UAS':'U-AS (Apoyo Acad.)','LC':'LC (Locus Control)'}
for k,v in M.items():
    print(f"  {labels_long[k]:<30}: M={v:.3f}  DE={SD[k]:.3f}")

# Variables centradas
data = data.copy()
data['EA_c'] = data['EA'] - M['EA']
data['SE_c'] = data['SE'] - M['SE']
data['UD_c'] = data['UD'] - M['UD']
data['EA_x_UD'] = data['EA_c'] * data['UD_c']
data['SE_x_UD'] = data['SE_c'] * data['UD_c']

# ── Helper: regresión OLS con β estandarizados ───────────────────────────

def stars(p):
    if p < .001: return '***'
    if p < .01:  return '**'
    if p < .05:  return '*'
    if p < .10:  return '†'
    return ''

def run_ols(y_col, x_cols, df, predictor_labels=None):
    """Corre OLS, devuelve (result, coef_df)."""
    y = df[y_col].values.astype(float)
    X_raw = df[x_cols].values.astype(float)
    X = np.column_stack([np.ones(len(y)), X_raw])

    res = sm.OLS(y, X).fit()
    params = res.params
    bse    = res.bse
    tvals  = res.tvalues
    pvals  = res.pvalues
    ci     = res.conf_int()

    # β estandarizados
    std_y  = np.std(y, ddof=1)
    std_xs = np.std(X_raw, axis=0, ddof=1)
    beta_std = [np.nan] + list(params[1:] * std_xs / std_y)

    rows = []
    names = ['Constante'] + (predictor_labels or x_cols)
    for i in range(len(params)):
        rows.append({
            'Predictor': names[i],
            'β':        round(params[i], 3),
            'β_std':    round(beta_std[i], 3) if not np.isnan(beta_std[i]) else None,
            'EE':       round(bse[i], 3),
            't':        round(tvals[i], 3),
            'p':        round(pvals[i], 4),
            'IC_lo':    round(ci[i,0], 3),
            'IC_hi':    round(ci[i,1], 3),
        })
    return res, pd.DataFrame(rows)

def print_model(title, coef_df, res, delta_r2=None, delta_f=None, delta_p=None):
    rmse = np.sqrt(res.mse_resid)
    n, k = res.nobs, res.df_model
    print(f"\n{'='*78}")
    print(f"  {title}")
    print(f"{'='*78}")
    print(f"  {'Predictor':<32} {'β':>7} {'β_std':>7} {'EE':>6} {'t':>7} {'p':>8}  IC 95%")
    print(f"  {'-'*74}")
    for _, row in coef_df.iterrows():
        sig = stars(row['p'])
        bs  = f"{row['β_std']:7.3f}" if row['β_std'] is not None else "      —"
        print(f"  {row['Predictor']:<32} {row['β']:7.3f} {bs} {row['EE']:6.3f} {row['t']:7.3f} {row['p']:8.4f}{sig:<4}  [{row['IC_lo']:.3f}, {row['IC_hi']:.3f}]")
    print(f"  {'-'*74}")
    print(f"  R²={res.rsquared:.3f}  R²_adj={res.rsquared_adj:.3f}  F({int(k)},{int(res.df_resid)})={res.fvalue:.2f}  p={res.f_pvalue:.4f}  RMSE={rmse:.3f}")
    if delta_r2 is not None:
        print(f"  ΔR²={delta_r2:.3f}  ΔF={delta_f:.2f}  Δp={delta_p:.4f}")
    print(f"  *** p<.001  ** p<.01  * p<.05  † p<.10")

# ── Modelo 1: TCP baseline ─────────────────────────────────────────────────
m1_res, m1_coef = run_ols('EI', ['EA','S','SE'], data,
    predictor_labels=['EA (Actitud Emprendedora)', 'S (Entorno Social / SN proxy)', 'SE (Autoeficacia / PBC proxy)'])
print_model('MODELO 1 — TCP Baseline  |  EI = β₀ + β₁(EA) + β₂(S) + β₃(SE) + ε', m1_coef, m1_res)

# ── Modelo 2: + Políticas ──────────────────────────────────────────────────
m2_res, m2_coef = run_ols('EI', ['EA','S','SE','FK','FL'], data,
    predictor_labels=['EA (Actitud)','S (Entorno Social)','SE (Autoeficacia)','FK (Conocimiento Ecosistema)','FL (Estado de Flujo)'])

# ΔR² test vs M1
# F = (R²2 - R²1) / q_added / ((1-R²2) / df_resid_m2)
q = 2  # FK, FL
dR2 = m2_res.rsquared - m1_res.rsquared
F_delta = (dR2 / q) / ((1 - m2_res.rsquared) / m2_res.df_resid)
p_delta = 1 - stats.f.cdf(F_delta, q, m2_res.df_resid)
print_model('MODELO 2 — TCP + Políticas  |  EI = β₀ + β₁(EA) + β₂(S) + β₃(SE) + β₄(FK) + β₅(FL) + ε',
            m2_coef, m2_res, delta_r2=dR2, delta_f=F_delta, delta_p=p_delta)

# ── Modelo 3: + Moderación ─────────────────────────────────────────────────
# Usamos versión centrada de M2 como base para ΔR²
m2c_res, _ = run_ols('EI', ['EA_c','S','SE_c','FK','FL'], data)

m3_vars = ['EA_c','S','SE_c','FK','FL','EA_x_UD','SE_x_UD','UD_c','UAS','LC']
m3_labels = ['EA_c (Actitud — centrada)','S (Entorno Social)','SE_c (Autoeficacia — centrada)',
             'FK (Conocimiento)','FL (Estado de Flujo)',
             'EA × U-D (interacción)','SE × U-D (interacción)',
             'U-D_c (Desarrollo Inst. — centrado)','U-AS (Apoyo Académico)','LC (Locus de Control)']
m3_res, m3_coef = run_ols('EI', m3_vars, data, predictor_labels=m3_labels)

q3 = 4  # interacciones + UD + UAS + LC añadidos sobre M2_centrado
dR2_3 = m3_res.rsquared - m2c_res.rsquared
F_delta3 = (dR2_3 / 5) / ((1 - m3_res.rsquared) / m3_res.df_resid)  # 5 vars nuevas vs m2c
p_delta3 = 1 - stats.f.cdf(F_delta3, 5, m3_res.df_resid)
print_model('MODELO 3 — + Moderación  |  EI ~ EA_c + S + SE_c + FK + FL + EA×U-D + SE×U-D + U-D_c + U-AS + LC',
            m3_coef, m3_res, delta_r2=dR2_3, delta_f=F_delta3, delta_p=p_delta3)

# ── VIF Modelo 3 ───────────────────────────────────────────────────────────
print("\n── VIF — Modelo 3 ──")
X3_mat = data[m3_vars].values.astype(float)
vifs = [variance_inflation_factor(X3_mat, i) for i in range(X3_mat.shape[1])]
for var, vif in zip(m3_vars, vifs):
    flag = "  ⚠️  >10" if vif > 10 else ""
    print(f"  {var:<20}: {vif:.2f}{flag}")

# ── Correlaciones ──────────────────────────────────────────────────────────
print("\n── Matriz de Correlaciones Pearson (N={}) ──".format(N_total))
cor_cols = ['EI','EA','S','SE','FK','FL','UD','UAS','LC']
cor_lbls = ['EI','EA','S','SE','FK','FL','U-D','U-AS','LC']
C = data[cor_cols].rename(columns=dict(zip(cor_cols, cor_lbls))).corr()

# Header
print("  " + "".join(f"{l:>7}" for l in cor_lbls))
for r in cor_lbls:
    row_str = f"  {r:<5}"
    for c in cor_lbls:
        v = C.loc[r,c]
        row_str += "      —" if r == c else f"  {v:>5.3f}"
    print(row_str)

print("\n  p-valores (correlaciones con EI):")
for c in cor_lbls[1:]:
    r_, p_ = stats.pearsonr(data['EI'], data[c.replace('-','').replace('AS','AS').replace('U-D','UD').replace('U-AS','UAS').replace('LC','LC').replace('-','')
                                              if c not in ['EI','EA','S','SE','FK','FL'] else c])
    # map label → data column
    col_map = {'U-D':'UD','U-AS':'UAS'}
    dc = col_map.get(c, c)
    r_, p_ = stats.pearsonr(data['EI'], data[dc])
    sig = stars(p_)
    print(f"    EI ↔ {c}: r={r_:.3f}  p={p_:.4f}{sig}")

# ── M y DE por constructo global vs Colombia ──────────────────────────────
col_mask = data['Country'] == 5   # Código 5 = Colombia (41 obs)
df_col = data[col_mask]
print(f"\n── Global vs Colombia (N_col={len(df_col)}) ──")
print(f"  {'Var':<6} {'M_global':>9} {'DE_global':>9} {'M_col':>8} {'DE_col':>8}")
for k, lbl in zip(['EI','EA','S','SE','FK','FL','UD','UAS','LC'],
                   ['EI','EA','S','SE','FK','FL','U-D','U-AS','LC']):
    mg=data[k].mean(); sg=data[k].std()
    mc=df_col[k].mean(); sc=df_col[k].std()
    print(f"  {lbl:<6} {mg:9.3f} {sg:9.3f} {mc:8.3f} {sc:8.3f}")

# ── Regresión Colombia ─────────────────────────────────────────────────────
print("\n── Sub-muestra Colombia (N={}) — EI ~ EA + SE ──".format(len(df_col)))
mc_res, mc_coef = run_ols('EI', ['EA','SE'], df_col,
    predictor_labels=['EA (Actitud)','SE (Autoeficacia)'])
print_model('COLOMBIA — EI = β₀ + β₁(EA) + β₂(SE) + ε  [exploratorio]', mc_coef, mc_res)

# ── Tabla comparativa β estandarizados ────────────────────────────────────
print("\n── Tabla comparativa β estandarizados ──")
print(f"  {'Predictor':<25} {'M1':>7} {'M2':>7} {'M3':>7}")
print("  " + "-"*46)

def β_std(coef_df, pred_contains):
    r = coef_df[coef_df['Predictor'].str.contains(pred_contains, case=False, regex=False)]
    if len(r)==0: return '     —'
    v = r.iloc[0]['β_std']
    return f"  {v:.3f}" if v is not None else '     —'

pairs = [('EA (Actitud)',   'Actitud','Actitud','Actitud'),
         ('S (Entorno)',    'Entorno','Entorno','Entorno'),
         ('SE (Autoeficac','Autoeficacia','Autoeficacia','Autoeficacia'),
         ('FK',             '—','Conocimiento','Conocimiento'),
         ('FL',             '—','Flujo','Flujo'),
         ('EA×U-D',         '—','—','EA × U-D'),
         ('SE×U-D',         '—','—','SE × U-D'),
         ('U-D',            '—','—','Desarrollo'),
         ('U-AS',           '—','—','Apoyo Académico'),
         ('LC',             '—','—','Locus'),
        ]
for row_label, k1, k2, k3 in pairs:
    b1 = β_std(m1_coef, k1) if k1 != '—' else '     —'
    b2 = β_std(m2_coef, k2) if k2 != '—' else '     —'
    b3 = β_std(m3_coef, k3) if k3 != '—' else '     —'
    print(f"  {row_label:<25} {b1} {b2} {b3}")

print("\n✅  Fase C completada.")
                                                                                                                                                                                                                                                                                                                        