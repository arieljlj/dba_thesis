# 📚 DBA Thesis - Tesis Doctoral UIIX

> **Repositorio de archivos de tesis doctoral siguiendo la estructura oficial de la Universidad de Investigación e Innovación de México (UIIX)**

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-nd/4.0/)

## 📋 Estructura del Repositorio

### 📁 **docs/** - Documentación de la Tesis
```
docs/
├── estructura_tesis_completa.md     # Estructura completa según UIIX
├── index.html                       # Página web de documentación
├── styles.css                       # Estilos para la documentación web
├── estadodelarte                    # Estado del arte (en desarrollo)
├── capitulos/                       # Capítulos principales
│   ├── cap1_proyeccion_investigacion/
│   ├── cap2_fundamentos_teoricos/
│   ├── cap3_metodologia_resultados/
│   └── cap4_propuesta_transformacion/
└── elementos_finales/               # Introducción, conclusiones, bibliografía
    ├── introduccion.md
    ├── conclusiones.md
    ├── recomendaciones.md
    ├── bibliografia.md
    └── anexos/
```

### 💻 **code/** - Scripts de Análisis
```
code/
├── analisis_macroeconomico.py      # Análisis macroeconómico
└── limpiar_datos.R                  # Limpieza de datos en R
```

### 📊 **data/** - Datos de la Investigación
```
data/
├── datos_brutos.csv                # Datos sin procesar
└── datos_limpios.csv               # Datos procesados
```

## 🎯 Capítulos de la Tesis

### **INTRODUCCIÓN**
Presentación general del trabajo de investigación.

### **Capítulo 1: Proyección de la Investigación**
- 1.1. Línea de investigación UIIX y ámbito de estudio
- 1.2. Planteamiento del problema
- 1.3. Formulación del problema (Pregunta de investigación)
- 1.4. Justificación
- 1.5. Objeto de estudio
- 1.6. Campo de acción
- 1.7. Objetivos (General y específicos)
- 1.8. Hipótesis
- 1.9. Alcance temático
- 1.10. Delimitación espacial y temporal

### **Capítulo 2: Fundamentos Teóricos Referenciales**
- 2.1. Estado del arte (Marco histórico y actual)
- 2.2. Marco teórico
- 2.3. Marco conceptual
- 2.4. Marco contextual
- 2.5. Marco legal y normativo

### **Capítulo 3: Fundamentos Metodológicos y Resultados**
- 3.1. Cuadro de operacionalización de variables
- 3.2. Diseño metodológico
  - 3.2.1. Enfoque, diseño y tipo de investigación
  - 3.2.2. Métodos, técnicas e instrumentos
  - 3.2.3. Desarrollo de instrumentos
  - 3.2.4. Determinación de la muestra
- 3.3. Trabajo de campo
  - 3.3.1. Aplicación de instrumentos
  - 3.3.2. Procesamiento de información
- 3.4. Análisis de resultados
- 3.5. Redacción de resultados y discusión

### **Capítulo 4: Propuesta de Transformación**
- 4.1. Fundamentación de la propuesta
- 4.2. Estructura de la propuesta
- 4.3. Valoración/evaluación/validación

### **Elementos Finales**
- **Conclusiones**
- **Recomendaciones**
- **Bibliografía** (Normas APA 7ª edición)
- **Anexos**

## 🚀 Instrucciones de Uso

### Análisis de Datos
1. **Limpieza de datos:**
   ```bash
   Rscript code/limpiar_datos.R
   ```
   - Input: `data/datos_brutos.csv`
   - Output: `data/datos_limpios.csv`

2. **Análisis macroeconómico:**
   ```bash
   python code/analisis_macroeconomico.py
   ```

### Documentación Web
- Abrir `docs/index.html` en navegador para ver la documentación interactiva
- Revisar `docs/estructura_tesis_completa.md` para la estructura completa

## 📏 Especificaciones Técnicas UIIX

### Formato del Documento
- **Tipo de letra:** Times New Roman 12 pt
- **Justificación:** Izquierda
- **Márgenes:** Izquierdo 4 cm, otros 2.5 cm
- **Interlineado:** 1.5 (citas: simple)
- **Extensión:** 120-200 páginas (introducción a recomendaciones)

### Elementos Requeridos
- ✅ Portada con datos institucionales
- ✅ Licencia Creative Commons BY-NC-ND 4.0
- ✅ Resumen (español) y Abstract (inglés)
- ✅ Índices automáticos actualizables
- ✅ Referencias APA 7ª edición

## 🔄 Estado de Desarrollo

| Sección | Estado | Progreso |
|---------|--------|----------|
| Estructura general | ✅ Completa | 100% |
| Capítulo 1 | 🚧 En desarrollo | 10% |
| Capítulo 2 | 🚧 En desarrollo | 15% |
| Capítulo 3 | 🚧 En desarrollo | 5% |
| Capítulo 4 | ⏳ Pendiente | 0% |
| Elementos finales | ⏳ Pendiente | 0% |

## 📚 Recursos Adicionales

- [Plantilla oficial UIIX](docs/Profesor%20Andres%20Forero%20-%20Artículo.pdf)
- [Matriz de operacionalización](docs/capitulos/cap3_metodologia_resultados/matrices/operacionalizacion_variables.md)
- [Normas APA 7ª edición](https://apastyle.apa.org/)
- [Creative Commons](http://creativecommons.org/licenses/by-nc-nd/4.0/)

## 📞 Información de Contacto

**Universidad:** Universidad de Investigación e Innovación de México (UIIX)

**Programa:** Doctorado en Administración de Empresas (DBA)

**Licencia:** Esta obra está bajo una [Licencia Creative Commons Atribución-NoComercial-SinDerivar 4.0 Internacional](http://creativecommons.org/licenses/by-nc-nd/4.0/)

---

**Última actualización:** Septiembre 2025

**Versión:** 2.0.0 - Estructura completa UIIX