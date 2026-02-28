import numpy as np
import plotly.graph_objects as go
from google.colab import files # Importiamo subito la funzione di download

# 1. Dati per la Sfera (Il piano proiettivo topologico)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sphere = np.outer(np.cos(u), np.sin(v))
y_sphere = np.outer(np.sin(u), np.sin(v))
z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))

# 2. Dati della Lemniscata di Bernoulli (a = 1) - PARAMETRIZZAZIONE CONTINUA
t = np.linspace(0, 2 * np.pi, 2000)
x_affine = (np.sqrt(2) * np.cos(t)) / (np.sin(t)**2 + 1)
y_affine = (np.sqrt(2) * np.cos(t) * np.sin(t)) / (np.sin(t)**2 + 1)

# 3. Proiezione sulla sfera (Coordinate Omogenee X1, X2, X0)
den = np.sqrt(x_affine**2 + y_affine**2 + 1)
X1_proj = x_affine / den
X2_proj = y_affine / den
X0_proj = 1 / den  # L'origine affine è al "Polo Nord"

# 4. Equatore (Retta all'infinito X0 = 0)
eq_t = np.linspace(0, 2*np.pi, 100)
x_eq = np.cos(eq_t)
y_eq = np.sin(eq_t)
z_eq = np.zeros_like(eq_t)

# 5. Costruzione del grafico interattivo
fig = go.Figure()

fig.add_trace(go.Surface(
    x=x_sphere, y=y_sphere, z=z_sphere,
    colorscale='Greys', opacity=0.15, showscale=False,
    name='Sfera Proiettiva', hoverinfo='skip'
))

fig.add_trace(go.Scatter3d(
    x=X1_proj, y=X2_proj, z=X0_proj, mode='lines',
    line=dict(color='darkblue', width=8), name='Lemniscata (Principale)'
))

fig.add_trace(go.Scatter3d(
    x=-X1_proj, y=-X2_proj, z=-X0_proj, mode='lines',
    line=dict(color='deepskyblue', width=8), name='Lemniscata (Antipodale)'
))

fig.add_trace(go.Scatter3d(
    x=x_eq, y=y_eq, z=z_eq, mode='lines',
    line=dict(color='green', width=4), name='Retta all\'infinito (X0=0)'
))

# 6. Estetica e layout
fig.update_layout(
    title=dict(text="Modello 3D Interattivo: Lemniscata nel Piano Proiettivo", x=0.5, font=dict(size=18)),
    scene=dict(
        xaxis=dict(showbackground=False, showticklabels=False, title='X1'),
        yaxis=dict(showbackground=False, showticklabels=False, title='X2'),
        zaxis=dict(showbackground=False, showticklabels=False, title='X0'),
        aspectmode='data' 
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    legend=dict(x=0.8, y=0.9)
)

# Mostra il grafico giù nella cella
fig.show()

# --- FASE DI SALVATAGGIO E DOWNLOAD ---
# Diciamo a Colab esattamente dove salvare il file
percorso_file = "/content/Modello_Lemniscata_3D.html"

# Crea fisicamente il file HTML
fig.write_html(percorso_file)

# Forza il download sul tuo computer
files.download(percorso_file)
