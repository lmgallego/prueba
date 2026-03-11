import pandas as pd

def compute_descriptives(df):
    # RF6: Análisis individual
    stats = {}
    
    if 'time' in df.columns:
        stats['duration (s)'] = df['time'].max() - df['time'].min()
    
    # Recolectar métricas comunes si existen
    for col in ['power', 'heart_rate', 'cadence', 'speed', 'temp', 'dfa_alpha_1', 'respiration', 'torque', 'artifacts']:
        if col in df.columns:
            stats[f'{col} (mean)'] = round(df[col].mean(), 2) if pd.notna(df[col].mean()) else None
            stats[f'{col} (max)'] = round(df[col].max(), 2) if pd.notna(df[col].max()) else None
            
    if 'distance' in df.columns:
        stats['distance (total)'] = round(df['distance'].max() - df['distance'].min(), 2)
        
    return stats

def compare_activities(stats1, stats2):
    # RF7: Comparación de actividades
    comparison = []
    
    all_keys = set(stats1.keys()).union(set(stats2.keys()))
    
    for k in sorted(all_keys):
        v1 = stats1.get(k, None)
        v2 = stats2.get(k, None)
        
        diff_abs = None
        diff_pct = None
        
        if pd.notna(v1) and pd.notna(v2):
            diff_abs = round(v2 - v1, 2)
            if v1 != 0:
                diff_pct = round((diff_abs / v1) * 100, 2)
                
        comparison.append({
            'Métrica': k,
            'Actividad 1': v1,
            'Actividad 2': v2,
            'Dif. Absoluta (A2 - A1)': diff_abs,
            'Dif. Relativa (%)': f"{diff_pct}%" if diff_pct is not None else None
        })
        
    return pd.DataFrame(comparison)
