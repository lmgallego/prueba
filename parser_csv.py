import pandas as pd

COLUMN_MAPPING = {
    'heartrate': 'heart_rate',
    'watts': 'power',
    'velocity_smooth': 'speed',
    'dfa_a1': 'dfa_alpha_1',
    'percentageinz2': 'PercentageinZ2',
    'rra1': 'RRa1',
    'respirationratealphahrv': 'RespirationRateAlphaHRV',
    'stamina': 'Stamina'
}

def normalize_columns(df):
    # RF3: Normalización (minúsculas y eliminación de espacios)
    df.columns = df.columns.astype(str).str.strip().str.lower()
    df.rename(columns=COLUMN_MAPPING, inplace=True)
    return df

def read_csv_robust(file, sep=','):
    # RF2 y RNF2: Lectura robusta con soporte utf-8-sig
    try:
        df = pd.read_csv(file, sep=sep, encoding='utf-8-sig', low_memory=False)
        df = normalize_columns(df)
        
        # Intentar forzar a numérico las columnas que no sean tiempo si este no es convertible
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
                
        return df, None
    except Exception as e:
        return None, str(e)
