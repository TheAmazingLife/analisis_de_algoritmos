import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Usar las rutas relativas correctas proporcionadas
try:
    bf_original = pd.read_csv('Tarea 1/testing/brute_force_vs.csv')
    bf_mejorado = pd.read_csv('Tarea 1/testing/brute_force_mejorado_vs.csv')
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
plt.loglog(bf_original['n'], bf_original['t_mean'] / 1e6, 'o-', 
           label='Fuerza Bruta Original', linewidth=2)
plt.loglog(bf_mejorado['n'], bf_mejorado['t_mean'] / 1e6, 's-', 
           label='Fuerza Bruta Mejorado', linewidth=2)
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo promedio (ms)')
plt.title('Comparación de implementaciones - Escala log-log')
plt.legend()
plt.grid(True, which="both", ls="-")
plt.tight_layout()
plt.savefig('vs_log_log_comparison.pdf')
plt.savefig('vs_log_log_comparison.png', dpi=300)
plt.show()

# 2. Gráfico de barras de error
plt.figure(figsize=(12, 6))
x = np.arange(len(bf_original['n']))
width = 0.35

plt.errorbar(x - width/2, bf_original['t_mean'] / 1e6, 
             yerr=bf_original['t_stdev'] / 1e6, fmt='o-', 
             label='Fuerza Bruta Original', capsize=5)
plt.errorbar(x + width/2, bf_mejorado['t_mean'] / 1e6, 
             yerr=bf_mejorado['t_stdev'] / 1e6, fmt='s-', 
             label='Fuerza Bruta Mejorado', capsize=5)

plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo promedio ± desv. est. (ms)')
plt.title('Comparación con barras de error')
plt.xticks(x, bf_original['n'])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('vs_error_bars.pdf')
plt.savefig('vs_error_bars.png', dpi=300)
plt.show()

# 3. Gráfico de mejora (speedup)
speedup = bf_original['t_mean'] / bf_mejorado['t_mean']

plt.figure(figsize=(10, 6))
plt.plot(bf_original['n'], speedup, 'o-', linewidth=2, color='green')
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Factor de mejora (Original/Mejorado)')
plt.title('Factor de mejora vs Tamaño del problema')
plt.grid(True)
plt.tight_layout()
plt.savefig('vs_speedup.pdf')
plt.savefig('vs_speedup.png', dpi=300)
plt.show()

# 4. Boxplot comparativo
plt.figure(figsize=(15, 6))
data_original = [
    [bf_original['t_Q0'][i], bf_original['t_Q1'][i],
     bf_original['t_Q2'][i], bf_original['t_Q3'][i],
     bf_original['t_Q4'][i]] for i in range(len(bf_original))]
data_mejorado = [
    [bf_mejorado['t_Q0'][i], bf_mejorado['t_Q1'][i],
     bf_mejorado['t_Q2'][i], bf_mejorado['t_Q3'][i],
     bf_mejorado['t_Q4'][i]] for i in range(len(bf_mejorado))]

positions = np.arange(len(bf_original['n'])) * 3
plt.boxplot(data_original, positions=positions-0.5, labels=bf_original['n'])
plt.boxplot(data_mejorado, positions=positions+0.5, labels=bf_mejorado['n'])

plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo (ns)')
plt.title('Distribución de tiempos de ejecución')
plt.legend(['Original', 'Mejorado'], loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('vs_boxplot.pdf')
plt.savefig('vs_boxplot.png', dpi=300)
plt.show()