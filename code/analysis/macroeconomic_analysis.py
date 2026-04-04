#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis Macroeconómico para Tesis Doctoral DBA

Este script realiza análisis estadísticos y visualizaciones
de datos macroeconómicos para la investigación doctoral.

Autor: DBA Student
Fecha: 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualización
plt.style.use('default')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

class AnalisisMacroeconomico:
    """
    Clase para realizar análisis macroeconómicos comprehensivos
    """
    
    def __init__(self, archivo_datos=None):
        """
        Inicializa la clase con datos macroeconómicos
        
        Parámetros:
        archivo_datos (str): Ruta al archivo de datos CSV
        """
        self.datos = None
        if archivo_datos:
            self.cargar_datos(archivo_datos)
    
    def cargar_datos(self, archivo):
        """
        Carga datos desde un archivo CSV
        
        Parámetros:
        archivo (str): Ruta al archivo CSV
        """
        try:
            self.datos = pd.read_csv(archivo)
            print(f"Datos cargados exitosamente: {self.datos.shape[0]} filas, {self.datos.shape[1]} columnas")
            return True
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return False
    
    def resumen_estadistico(self):
        """
        Genera un resumen estadístico de los datos
        """
        if self.datos is None:
            print("No hay datos cargados")
            return None
        
        print("=== RESUMEN ESTADÍSTICO ===")
        print("\nInformación básica:")
        print(self.datos.info())
        
        print("\nEstadísticas descriptivas:")
        return self.datos.describe()
    
    def analisis_correlacion(self):
        """
        Realiza análisis de correlación entre variables
        """
        if self.datos is None:
            print("No hay datos cargados")
            return None
        
        # Seleccionar solo columnas numéricas
        datos_numericos = self.datos.select_dtypes(include=[np.number])
        
        if datos_numericos.empty:
            print("No hay variables numéricas para analizar")
            return None
        
        # Calcular matriz de correlación
        correlacion = datos_numericos.corr()
        
        # Crear heatmap
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlacion, annot=True, cmap='coolwarm', center=0,
                    square=True, fmt='.2f')
        plt.title('Matriz de Correlación - Variables Macroeconómicas')
        plt.tight_layout()
        plt.show()
        
        return correlacion
    
    def analisis_tendencias(self, columna_tiempo='fecha', variables=None):
        """
        Analiza tendencias temporales de las variables
        
        Parámetros:
        columna_tiempo (str): Nombre de la columna de tiempo
        variables (list): Lista de variables a analizar
        """
        if self.datos is None:
            print("No hay datos cargados")
            return None
        
        # Convertir columna de tiempo
        try:
            self.datos[columna_tiempo] = pd.to_datetime(self.datos[columna_tiempo])
        except:
            print(f"No se pudo convertir la columna {columna_tiempo} a fecha")
            return None
        
        # Seleccionar variables
        if variables is None:
            variables = self.datos.select_dtypes(include=[np.number]).columns.tolist()
        
        # Crear gráficos de tendencias
        n_vars = len(variables)
        fig, axes = plt.subplots(n_vars, 1, figsize=(15, 5*n_vars))
        
        if n_vars == 1:
            axes = [axes]
        
        for i, var in enumerate(variables):
            if var in self.datos.columns:
                axes[i].plot(self.datos[columna_tiempo], self.datos[var], 
                           linewidth=2, marker='o', markersize=4)
                axes[i].set_title(f'Tendencia Temporal - {var}')
                axes[i].set_xlabel('Tiempo')
                axes[i].set_ylabel(var)
                axes[i].grid(True, alpha=0.3)
                axes[i].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.show()
    
    def test_estacionariedad(self, variable):
        """
        Realiza test de estacionariedad (Augmented Dickey-Fuller)
        
        Parámetros:
        variable (str): Nombre de la variable a testear
        """
        if self.datos is None or variable not in self.datos.columns:
            print("Variable no encontrada en los datos")
            return None
        
        serie = self.datos[variable].dropna()
        
        # Test ADF
        resultado = stats.adfuller(serie)
        
        print(f"\n=== TEST DE ESTACIONARIEDAD - {variable} ===")
        print(f"Estadístico ADF: {resultado[0]:.4f}")
        print(f"p-value: {resultado[1]:.4f}")
        print(f"Valores críticos:")
        for key, value in resultado[4].items():
            print(f"\t{key}: {value:.3f}")
        
        if resultado[1] <= 0.05:
            print("La serie ES estacionaria (se rechaza H0)")
        else:
            print("La serie NO es estacionaria (no se rechaza H0)")
        
        return resultado
    
    def generar_reporte(self, archivo_salida='reporte_macroeconomico.html'):
        """
        Genera un reporte completo en HTML
        
        Parámetros:
        archivo_salida (str): Nombre del archivo de salida
        """
        if self.datos is None:
            print("No hay datos cargados")
            return None
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Reporte de Análisis Macroeconómico</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                h1, h2 {{ color: #2c3e50; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Reporte de Análisis Macroeconómico</h1>
            <h2>Resumen de Datos</h2>
            <p>Número de observaciones: {self.datos.shape[0]}</p>
            <p>Número de variables: {self.datos.shape[1]}</p>
            
            <h2>Estadísticas Descriptivas</h2>
            {self.datos.describe().to_html()}
            
            <h2>Primeras 10 observaciones</h2>
            {self.datos.head(10).to_html()}
        </body>
        </html>
        """
        
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Reporte generado: {archivo_salida}")
        return archivo_salida


def main():
    """
    Función principal para demostrar el uso de la clase
    """
    print("=== ANÁLISIS MACROECONÓMICO - TESIS DOCTORAL ===")
    print("Iniciando análisis...")
    
    # Crear instancia del analizador
    analizador = AnalisisMacroeconomico()
    
    # Ejemplo de uso con datos sintéticos
    print("\nCreando datos de ejemplo...")
    
    # Generar datos sintéticos
    fechas = pd.date_range('2020-01-01', periods=100, freq='M')
    np.random.seed(42)
    
    datos_ejemplo = pd.DataFrame({
        'fecha': fechas,
        'pib': np.random.normal(100, 10, 100).cumsum(),
        'inflacion': np.random.normal(2, 1, 100),
        'desempleo': np.random.normal(5, 2, 100),
        'tipo_cambio': np.random.normal(20, 3, 100)
    })
    
    analizador.datos = datos_ejemplo
    
    # Realizar análisis
    print("\n1. Resumen estadístico:")
    resumen = analizador.resumen_estadistico()
    
    print("\n2. Análisis de correlación:")
    correlaciones = analizador.analisis_correlacion()
    
    print("\n3. Análisis de tendencias:")
    analizador.analisis_tendencias(variables=['pib', 'inflacion'])
    
    print("\n4. Test de estacionariedad:")
    analizador.test_estacionariedad('pib')
    
    print("\n5. Generando reporte:")
    analizador.generar_reporte()
    
    print("\nAnálisis completado exitosamente!")


if __name__ == "__main__":
    main()
