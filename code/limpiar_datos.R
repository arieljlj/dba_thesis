# limpiar_datos.R
# Script para limpiar y preparar datos para la tesis doctoral DBA
# Autor: DBA Student
# Fecha: 2025

suppressPackageStartupMessages({
  library(dplyr)
  library(readr)
  library(stringr)
  library(lubridate)
})

# Función principal de limpieza
depurar_datos <- function(ruta_entrada = "data/datos_brutos.csv",
                          ruta_salida = "data/datos_limpios.csv") {
  message("Iniciando limpieza de datos...")
  
  # 1. Cargar datos
  df <- read_csv(ruta_entrada, show_col_types = FALSE, progress = FALSE)
  message(sprintf("Datos cargados: %s filas, %s columnas", nrow(df), ncol(df)))
  
  # 2. Estandarizar nombres de columnas
  nombres <- names(df) %>%
    str_trim() %>%
    str_to_lower() %>%
    str_replace_all("[\n\r]+", " ") %>%
    str_replace_all("[\t]+", " ") %>%
    str_replace_all("[áÁ]", "a") %>%
    str_replace_all("[éÉ]", "e") %>%
    str_replace_all("[íÍ]", "i") %>%
    str_replace_all("[óÓ]", "o") %>%
    str_replace_all("[úÚ]", "u") %>%
    str_replace_all("ñ", "n") %>%
    str_replace_all("[^a-z0-9]+", "_") %>%
    str_replace_all("_+", "_") %>%
    str_replace("^_", "") %>%
    str_replace("_$", "")
  names(df) <- nombres
  
  # 3. Quitar duplicados exactos
  filas_antes <- nrow(df)
  df <- distinct(df)
  message(sprintf("Duplicados eliminados: %s", filas_antes - nrow(df)))
  
  # 4. Manejar valores perdidos
  # - Quitar columnas completamente vacías
  vacias <- sapply(df, function(x) all(is.na(x)))
  if (any(vacias)) {
    df <- df[, !vacias, drop = FALSE]
    message(sprintf("Columnas vacías eliminadas: %s", sum(vacias)))
  }
  
  # - Relleno simple para columnas numéricas con mediana
  numericas <- sapply(df, is.numeric)
  df[numericas] <- lapply(df[numericas], function(x) {
    ifelse(is.na(x), median(x, na.rm = TRUE), x)
  })
  
  # - Recorte y normalización básica de texto en columnas de caracteres
  de_texto <- sapply(df, is.character)
  df[de_texto] <- lapply(df[de_texto], function(x) {
    x <- str_squish(x)
    x <- na_if(x, "")
    x
  })
  
  # 5. Detección básica de outliers (IQR) en variables numéricas
  tratar_outliers <- function(x) {
    if (!is.numeric(x)) return(x)
    q1 <- quantile(x, 0.25, na.rm = TRUE)
    q3 <- quantile(x, 0.75, na.rm = TRUE)
    iqr <- q3 - q1
    lim_inf <- q1 - 1.5 * iqr
    lim_sup <- q3 + 1.5 * iqr
    x[x < lim_inf] <- lim_inf
    x[x > lim_sup] <- lim_sup
    x
  }
  df[numericas] <- lapply(df[numericas], tratar_outliers)
  
  # 6. Estandarizar fechas si existe alguna columna con nombre similar a 'fecha'
  posibles_fechas <- names(df)[str_detect(names(df), "fecha|date|periodo|period", negate = FALSE)]
  for (col in posibles_fechas) {
    df[[col]] <- suppressWarnings(parse_date_time(df[[col]], orders = c("Ymd", "dmY", "mdY", "Y-m-d", "d/m/Y", "m/d/Y")))
  }
  
  # 7. Guardar datos limpios
  dir.create("data", showWarnings = FALSE)
  write_csv(df, ruta_salida)
  message(sprintf("Datos limpios guardados en: %s", ruta_salida))
  
  invisible(df)
}

# Ejecutar si se llama directamente desde Rscript
if (sys.nframe() == 0) {
  tryCatch({
    depurar_datos()
  }, error = function(e) {
    message(sprintf("Error durante la limpieza: %s", e$message))
    quit(status = 1)
  })
}
