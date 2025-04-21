import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Cargar los datos
try:
    bf_data = pd.read_csv('uhr-main/brute_force.csv')
    dc_data = pd.read_csv('uhr-main/divide_and_conquer.csv')
    print("Archivos cargados correctamente")
except FileNotFoundError as e:
    print(f"Error al cargar los archivos: {e}")
    print("Asegúrate de que las rutas sean correctas")
    exit(1)

# Crear un gráfico con 3 subplots como en el ejemplo
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Subplot 1: Gráfico log-log (comparación de ambos algoritmos)
ax[0].errorbar(
    bf_data["n"],
    bf_data["t_mean"],
    bf_data["t_stdev"],
    linestyle="None",
    marker='.',
    label='Fuerza Bruta',
    ecolor='tab:red'
)

ax[0].errorbar(
    dc_data["n"],
    dc_data["t_mean"],
    dc_data["t_stdev"],
    linestyle="None",
    marker='s',
    label='Divide y Vencerás',
    ecolor='tab:blue'
)

ax[0].set_title("log-log")
ax[0].set_xlabel("Tamaño del problema (n)")
ax[0].set_ylabel("Tiempo (ns)")
ax[0].set_xscale("log", base=2)
ax[0].set_yscale("log", base=10)
ax[0].legend()
ax[0].grid(True, which="both", ls="-", alpha=0.2)

# Subplot 2: Gráfico normal (tiempo vs n)
ax[1].errorbar(
    bf_data["n"][:5],  # Usamos menos puntos para mejor visualización
    bf_data["t_mean"][:5] / 1e6,  # Convertir a ms
    bf_data["t_stdev"][:5] / 1e6,
    linestyle="None",
    marker='.',
    label='Fuerza Bruta',
    ecolor='tab:red'
)

ax[1].errorbar(
    dc_data["n"][:5],
    dc_data["t_mean"][:5] / 1e6,
    dc_data["t_stdev"][:5] / 1e6,
    linestyle="None",
    marker='s',
    label='Divide y Vencerás',
    ecolor='tab:blue'
)

ax[1].set_title("Comparación de tiempos")
ax[1].set_xlabel("Tamaño del problema (n)")
ax[1].set_ylabel("Tiempo (ms)")
ax[1].legend()
ax[1].grid(True, alpha=0.2)

# Subplot 3: Gráfico semi-log (speedup vs n)
speedup = bf_data["t_mean"] / dc_data["t_mean"]
speedup_error = np.sqrt((bf_data["t_stdev"]/bf_data["t_mean"])**2 + 
                        (dc_data["t_stdev"]/dc_data["t_mean"])**2) * speedup

ax[2].errorbar(
    bf_data["n"],
    speedup,
    speedup_error,
    linestyle="None",
    marker='.',
    ecolor='tab:red'
)

ax[2].set_title("semi-log plot")
ax[2].set_xlabel("Tamaño del problema (n)")
ax[2].set_ylabel("Speedup (BF/DC)")
ax[2].set_xscale("log", base=2)
ax[2].grid(True, alpha=0.2)

# Ajustar el layout y guardar
fig.tight_layout()
fig.savefig("comparison_plots.pdf")
fig.savefig("comparison_plots.png", dpi=300)
plt.show()

# Versión alternativa con formato más parecido al ejemplo original
fig2, ax2 = plt.subplots(1, 3, figsize=(15, 5))

# Subplot 1: Gráfico log-log (solo fuerza bruta)
ax2[0].errorbar(
    bf_data["n"],
    bf_data["t_mean"],
    bf_data["t_stdev"],
    linestyle="None",
    marker='.',
    ecolor='tab:red'
)

ax2[0].set_title("log-log")
ax2[0].set_xlabel("x axis label")
ax2[0].set_ylabel("y axis label")
ax2[0].set_xscale("log", base=2)
ax2[0].set_yscale("log", base=10)

# Subplot 2: Gráfico normal (tiempo vs n para fuerza bruta)
ax2[1].errorbar(
    bf_data["n"][:5],  # Usamos menos puntos para mejor visualización
    bf_data["t_mean"][:5] / 1e6,  # Convertir a ms
    bf_data["t_stdev"][:5] / 1e6,
    linestyle="None",
    marker='.',
    ecolor='tab:red'
)

ax2[1].set_title("Super cool and descriptive name")
ax2[1].set_xlabel("Unit length variable")
ax2[1].set_ylabel("Response")

# Subplot 3: Gráfico semi-log (solo para divide y vencerás)
ax2[2].errorbar(
    dc_data["n"],
    dc_data["t_mean"],
    dc_data["t_stdev"],
    linestyle="None",
    marker='.',
    ecolor='tab:red'
)

ax2[2].set_title("semi-log plot")
ax2[2].set_xlabel("Position")
ax2[2].set_ylabel("Average happiness")
ax2[2].set_xscale("log", base=2)

# Ajustar el layout y guardar
fig2.tight_layout()
fig2.savefig("sample_style_plots.pdf")
fig2.savefig("sample_style_plots.png", dpi=300)
plt.show()