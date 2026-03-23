codigo <- c(
  "library(semPlot)",
  "library(semTools)",
  "library(seminr)",
  "library(sem)"
)

if (!requireNamespace("seminr", quietly = TRUE)) install.packages("seminr")
library(seminr)

modelo_medicion <- constructs(
  composite("RE", c("e1", "e2", "e3", "e4", "e5")),
  composite("MO", c("m1", "m2", "m3", "m4")),
  composite("HS", c("ss1", "ss2", "ss3", "ss4", "ss5")),
  composite("AR", c("sr1", "sr2", "sr3")),
  composite("AC", c("sa1", "sa2", "sa3")),
  higher_composite("EC", c("RE", "MO", "HS", "AR", "AC"), weights = mode_B),
  composite("EA", c("var24","var25","var26","var27","var28","var29","var30","var31")),
  composite("ES", c("es1","es2","es3","es4","es5")),
  composite("EI", c("ei1","ei2","ei3","ei4","ei5")),
  composite("FL", c("fl1","fl2","fl3","fl4","fl5","fl6","fl7")),
  composite("ECA", c("ea1","ea2","ea3","ea4","ea5","ea6","ea7","ea8"))
)

modelo_estructura <- relationships(
  paths(from = "EC", to = c("ES", "EA", "ECA")),
  paths(from = c("ES", "EA"), to = "EI"),
  paths(from = "EI", to = "ECA"),
  paths(from = "FL", to = c("ES", "EA", "ECA"))
)

modelo_pls <- estimate_pls(
  data = emprendodres_final,
  measurement_model = modelo_medicion,
  structural_model = modelo_estructura,
  inner_weights = path_weighting,
  missing = mean_replacement,
  missing_value = "-99"
)

set.seed(123)
boot_model <- bootstrap_model(modelo_pls, nboot = 50)

summary_results <- summary(boot_model)

cat("\n=== SIGNIFICANCIA DE COEFICIENTES ESTRUCTURALES ===\n")
print(summary_results$bootstrapped_paths)

cat("\n=== SIGNIFICANCIA DE EFECTOS INDIRECTOS ===\n")
print(summary_results$indirect_effects)

plot(modelo_pls, title = "Modelo PLS-SEM Corregido con Abreviaciones")

constructos <- boot_model$constructs
cat("Constructos en el modelo:", paste(constructos, collapse = ", "), "\n")

paths_boot <- boot_model$boot_paths
dimnames_paths <- dimnames(paths_boot)
cat("\nDimensiones de paths bootstrap:", dim(paths_boot), "\n")
cat("Nombres de filas (from):", dimnames_paths[[1]], "\n")
cat("Nombres de columnas (to):", dimnames_paths[[2]], "\n")

calc_mediacion <- function(from, through, to, boot_model) {
  from_idx <- which(dimnames_paths[[1]] == from)
  through_idx <- sapply(through, function(x) which(dimnames_paths[[1]] == x))
  to_idx <- which(dimnames_paths[[2]] == to)
  
  if (length(from_idx) == 0 || any(sapply(through_idx, length) == 0) || length(to_idx) == 0) {
    stop("Alguno de los constructos no existe en el modelo")
  }
  
  indirect_effects <- sapply(1:boot_model$boots, function(i) {
    path1 <- paths_boot[from_idx, through_idx[1], i]
    path2 <- paths_boot[through_idx[1], through_idx[2], i]
    path3 <- paths_boot[through_idx[2], to_idx, i]
    path1 * path2 * path3
  })
  
  original <- mean(indirect_effects)
  se <- sd(indirect_effects)
  ci <- quantile(indirect_effects, c(0.025, 0.975))
  
  data.frame(
    Relationship = paste(from, "->", paste(through, collapse = "->"), "->", to),
    Original = original,
    Mean.Boot = mean(indirect_effects),
    Std.Error = se,
    CI.Lower = ci[1],
    CI.Upper = ci[2],
    p.value = 2 * pnorm(-abs(original / se))
  )
}

tryCatch({
  mediacion1 <- calc_mediacion("EC", c("ES", "EI"), "ECA", boot_model)
  mediacion2 <- calc_mediacion("EC", c("EA", "EI"), "ECA", boot_model)
  mediacion3 <- calc_mediacion("FL", c("ES", "EI"), "ECA", boot_model)
  mediacion4 <- calc_mediacion("FL", c("EA", "EI"), "ECA", boot_model)
  
  cat("\n=== RESULTADOS DE MEDIACIÓN ===\n")
  print(mediacion1)
  print(mediacion2)
  print(mediacion3)
  print(mediacion4)
}, error = function(e) {
  cat("\nERROR:", e$message, "\n")
  cat("Los constructos disponibles son:", paste(constructos, collapse = ", "), "\n")
  cat("Las relaciones deben usar exactamente estos nombres.\n")
})

calculate_vif <- function(pls_model) {
  path_matrix <- pls_model$path_coef
  endogenous <- which(apply(path_matrix, 2, function(x) any(x != 0)))
  
  vif_results <- sapply(names(endogenous), function(construct) {
    predictors <- which(path_matrix[, construct] != 0)
    
    if (length(predictors) < 2) return(NA)
    
    X <- pls_model$construct_scores[, predictors, drop = FALSE]
    
    r_squared <- sapply(1:length(predictors), function(i) {
      summary(lm(X[, i] ~ X[, -i]))$r.squared
    })
    
    vif <- 1 / (1 - r_squared)
    names(vif) <- colnames(X)
    vif
  })
  
  vif_df <- data.frame(
    Construct = rep(names(endogenous), sapply(vif_results, length)),
    Predictor = unlist(lapply(vif_results, names)),
    VIF = unlist(vif_results)
  )
  
  rownames(vif_df) <- NULL
  vif_df[complete.cases(vif_df), ]
}

cat("\n=== FACTORES DE INFLACIÓN DE VARIANZA (VIF) ===\n")
vif_results <- calculate_vif(modelo_pls)

if (nrow(vif_results) > 0) {
  print(vif_results)
  
  cat("\nINTERPRETACIÓN VIF:
- VIF < 3: No hay problemas de multicolinealidad
- 3 ≤ VIF < 5: Multicolinealidad moderada (revisar)
- VIF ≥ 5: Multicolinealidad alta (problema serio)\n")
  
  problems <- vif_results[vif_results$VIF >= 3, ]
  if (nrow(problems) > 0) {
    cat("\n¡ADVERTENCIA! Multicolinealidad detectada en:\n")
    print(problems)
  } else {
    cat("\nNo se detectaron problemas serios de multicolinealidad.\n")
  }
} else {
  cat("No hay constructos endógenos con suficientes predictores para calcular VIF.\n")
}

cat("\n=== MATRIZ DE CORRELACIONES ENTRE CONSTRUCTOS ===\n")
construct_cor <- cor(modelo_pls$construct_scores)
print(construct_cor)

high_cor <- which(abs(construct_cor) > 0.7 & upper.tri(construct_cor), arr.ind = TRUE)
if (length(high_cor) > 0) {
  cat("\n¡ADVERTENCIA! Correlaciones altas (> 0.7) entre:\n")
  for (i in 1:nrow(high_cor)) {
    cat(rownames(construct_cor)[high_cor[i, 1]], "y",
        colnames(construct_cor)[high_cor[i, 2]],
        ":", round(construct_cor[high_cor[i, 1], high_cor[i, 2]], 3), "\n")
  }
} else {
  cat("\nNo se detectaron correlaciones altas entre constructos.\n")
}