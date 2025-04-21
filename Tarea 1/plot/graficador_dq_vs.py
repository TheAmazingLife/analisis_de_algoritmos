import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Usar las rutas relativas correctas proporcionadas
try:
    dq_original = pd.read_csv('Tarea 1/testing/divide_and_conquer_vs.csv')
    dq_mejorado = pd.read_csv('Tarea 1/testing/divide_and_conquer_mejorado_vs.csv')
    print("Archivos cargados correctamente")
except FileNotFoundError as e:
    print(f"Error al cargar los archivos: {e}")
    print("Asegúrate de que las rutas sean correctas")
    exit(1)

# Configurar el estilo general de los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({'font.size': 12})

# 1. Gráfico log-log para comparar los tiempos de ejecución
plt.figure(figsize=(10, 6))
plt.loglog(dq_original['n'], dq_original['t_mean'] / 1e6, 'o-', 
           label='Divide & Conquer Original', linewidth=2)
plt.loglog(dq_mejorado['n'], dq_mejorado['t_mean'] / 1e6, 's-', 
           label='Divide & Conquer Mejorado', linewidth=2)
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo promedio (ms)')
plt.title('Comparación de implementaciones D&C - Escala log-log')
plt.legend()
plt.grid(True, which="both", ls="-")
plt.tight_layout()
plt.savefig('dc_log_log_comparison.pdf')
plt.savefig('dc_log_log_comparison.png', dpi=300)
plt.show()

# 2. Gráfico de barras de error
plt.figure(figsize=(12, 6))
x = np.arange(len(dq_original['n']))
width = 0.35

plt.errorbar(x - width/2, dq_original['t_mean'] / 1e6, 
             yerr=dq_original['t_stdev'] / 1e6, fmt='o-', 
             label='Divide & Conquer Original', capsize=5)
plt.errorbar(x + width/2, dq_mejorado['t_mean'] / 1e6, 
             yerr=dq_mejorado['t_stdev'] / 1e6, fmt='s-', 
             label='Divide & Conquer Mejorado', capsize=5)

plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo promedio ± desv. est. (ms)')
plt.title('Comparación D&C con barras de error')
plt.xticks(x, dq_original['n'])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('dc_error_bars.pdf')
plt.savefig('dc_error_bars.png', dpi=300)
plt.show()

# 3. Gráfico de mejora (speedup)
speedup = dq_original['t_mean'] / dq_mejorado['t_mean']

plt.figure(figsize=(10, 6))
plt.plot(dq_original['n'], speedup, 'o-', linewidth=2, color='green')
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Factor de mejora (Original/Mejorado)')
plt.title('Factor de mejora vs Tamaño del problema (D&C)')
plt.grid(True)
plt.tight_layout()
plt.savefig('dc_speedup.pdf')
plt.savefig('dc_speedup.png', dpi=300)
plt.show()

# 4. Boxplot comparativo
plt.figure(figsize=(15, 6))
data_original = [
    [dq_original['t_Q0'][i], dq_original['t_Q1'][i],
     dq_original['t_Q2'][i], dq_original['t_Q3'][i],
     dq_original['t_Q4'][i]] for i in range(len(dq_original))]
data_mejorado = [
    [dq_mejorado['t_Q0'][i], dq_mejorado['t_Q1'][i],
     dq_mejorado['t_Q2'][i], dq_mejorado['t_Q3'][i],
     dq_mejorado['t_Q4'][i]] for i in range(len(dq_mejorado))]

positions = np.arange(len(dq_original['n'])) * 3
plt.boxplot(data_original, positions=positions-0.5, labels=dq_original['n'])
plt.boxplot(data_mejorado, positions=positions+0.5, labels=dq_mejorado['n'])

plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo (ns)')
plt.title('Distribución de tiempos de ejecución (D&C)')
plt.legend(['Original', 'Mejorado'], loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('dc_boxplot.pdf')
plt.savefig('dc_boxplot.png', dpi=300)
plt.show()