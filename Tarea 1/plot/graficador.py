import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Usar las rutas relativas correctas proporcionadas
try:
    bf_data = pd.read_csv('Tarea 1/testing/brute_force.csv')
    dc_data = pd.read_csv('Tarea 1/testing/divide_and_conquer.csv')
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
plt.loglog(bf_data['n'], bf_data['t_mean'] / 1e6, 'o-', label='Fuerza Bruta', linewidth=2)
plt.loglog(dc_data['n'], dc_data['t_mean'] / 1e6, 's-', label='Divide y Vencerás', linewidth=2)
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo promedio (ms)')
plt.title('Comparación de algoritmos - Escala log-log')
plt.legend()
plt.grid(True, which="both", ls="-")
plt.tight_layout()
plt.savefig('log_log_comparison.pdf')
plt.savefig('log_log_comparison.jpg', dpi=300)
plt.show()

# 2. Gráfico normal
plt.figure(figsize=(10, 6))
plt.plot(bf_data['n'], bf_data['t_mean'] / 1e6, 'o-', label='Fuerza Bruta', linewidth=2)
plt.plot(dc_data['n'], dc_data['t_mean'] / 1e6, 's-', label='Divide y Vencerás', linewidth=2)
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo promedio (ms)')
plt.title('Comparación de tiempos de ejecución')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('normal_comparison.pdf')
plt.savefig('normal_comparison.jpg', dpi=300)
plt.show()

# 3. Gráfico semi-log (eje-y logarítmico)
plt.figure(figsize=(10, 6))
plt.semilogy(bf_data['n'], bf_data['t_mean'] / 1e6, 'o-', label='Fuerza Bruta', linewidth=2)
plt.semilogy(dc_data['n'], dc_data['t_mean'] / 1e6, 's-', label='Divide y Vencerás', linewidth=2)
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo promedio (ms) - escala log')
plt.title('Comparación de algoritmos - Escala semi-log')
plt.legend()
plt.grid(True, which="both", ls="-")
plt.tight_layout()
plt.savefig('semi_log_comparison.pdf')
plt.savefig('semi_log_comparison.jpg', dpi=300)
plt.show()

# 4. Gráfico de barras para comparar la desviación estándar
plt.figure(figsize=(12, 6))
x = np.arange(len(bf_data['n']))
width = 0.35

plt.bar(x - width/2, bf_data['t_stdev'] / 1e6, width, label='Fuerza Bruta')
plt.bar(x + width/2, dc_data['t_stdev'] / 1e6, width, label='Divide y Vencerás')

plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Desviación estándar (ms)')
plt.title('Comparación de la variabilidad')
plt.xticks(x, bf_data['n'])
plt.legend()
plt.grid(True, axis='y')
plt.tight_layout()
plt.savefig('stdev_comparison.pdf')
plt.savefig('stdev_comparison.jpg', dpi=300)
plt.show()

# 5. Cálculo de la eficiencia: ratio de tiempos
speedup = bf_data['t_mean'] / dc_data['t_mean']

plt.figure(figsize=(10, 6))
plt.plot(bf_data['n'], speedup, 'o-', linewidth=2, color='green')
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Aceleración (Brute Force / Divide & Conquer)')
plt.title('Speedup de Divide y Vencerás vs Fuerza Bruta')
plt.grid(True)
plt.tight_layout()
plt.savefig('speedup.pdf')
plt.savefig('speedup.jpg', dpi=300)
plt.show()

# 6. Boxplot comparativo
plt.figure(figsize=(15, 6))
data_original = [
    [bf_data['t_Q0'][i], bf_data['t_Q1'][i],
     bf_data['t_Q2'][i], bf_data['t_Q3'][i],
     bf_data['t_Q4'][i]] for i in range(len(bf_data))]
data_mejorado = [
    [dc_data['t_Q0'][i], dc_data['t_Q1'][i],
     dc_data['t_Q2'][i], dc_data['t_Q3'][i],
     dc_data['t_Q4'][i]] for i in range(len(dc_data))]

positions = np.arange(len(bf_data['n'])) * 3
plt.boxplot(data_original, positions=positions-0.5, labels=bf_data['n'], patch_artist=True,
           boxprops=dict(facecolor='C0', color='C0'))  # C0 es el primer color del ciclo de matplotlib
plt.boxplot(data_mejorado, positions=positions+0.5, labels=dc_data['n'], patch_artist=True,
           boxprops=dict(facecolor='C1', color='C1'))  # C1 es el segundo color del ciclo

plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Tiempo (ns)')
plt.title('Distribución de tiempos de ejecución')
plt.legend(['Fuerza Bruta', 'Divide y Vencerás'], loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('vs_boxplot.pdf')
plt.savefig('vs_boxplot.png', dpi=300)
plt.show()