import plotly.graph_objects as go
import pandas as pd

def plot_time_series(df1, df2, metric_col, names, overlay=False):
    # RF8: Gráficos de evolución
    fig = go.Figure()
    
    # helper para que los colores sean consistentes
    colors = ['#1f77b4', '#ff7f0e']
    
    for idx, (df, name) in enumerate(zip([df1, df2], names)):
        if df is not None and metric_col in df.columns and 'time' in df.columns:
            # Si estan superpuestos mantenemos x='time' normal
            # Pero en actividades de distinto tamaño/tiempo, al superponer 
            # asume que ambas inician en t=0 o mantienen su 'time' tal cual
            fig.add_trace(go.Scatter(
                x=df['time'].copy() if overlay else df['time'], 
                y=df[metric_col], 
                mode='lines', 
                name=f"{name}",
                line=dict(color=colors[idx], width=1.5)
            ))
            
    fig.update_layout(
        title=f'Comparativa de {metric_col}',
        xaxis_title='Tiempo (s)',
        yaxis_title=metric_col,
        hovermode="x unified",
        template="plotly_white",
        legend_title="Actividad"
    )
    
    return fig
