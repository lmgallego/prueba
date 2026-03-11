import pandas as pd

# RF4: Validación
MANDATORY_COLS = ['time', 'power', 'heart_rate']
OPTIONAL_COLS = [
    'cadence', 'distance', 'speed', 'temp', 'torque', 'dfa_alpha_1',
    'respiration', 'artifacts', 'PercentageinZ2', 'RRa1',
    'RespirationRateAlphaHRV', 'Stamina'
]

def validate_structure(df):
    cols = list(df.columns)
    missing_mandatory = [c for c in MANDATORY_COLS if c not in cols]
    detected_optional = [c for c in OPTIONAL_COLS if c in cols]
    unknown = [c for c in cols if c not in MANDATORY_COLS and c not in OPTIONAL_COLS]
    
    is_valid = len(missing_mandatory) == 0
    return {
        'is_valid': is_valid,
        'missing_mandatory': missing_mandatory,
        'detected_optional': detected_optional,
        'unknown': unknown,
        'all_detected': cols
    }

def quality_report(df, validation_info):
    # RF10: Diagnóstico de calidad
    report = {}
    report['empty_columns'] = df.columns[df.isnull().all()].tolist()
    
    if 'time' in df.columns and pd.api.types.is_numeric_dtype(df['time']):
        diffs = df['time'].diff()
        report['time_jumps'] = int((diffs > 2.0).sum()) # Salto temporal mayor a 2s
        report['time_dupes'] = int((diffs == 0.0).sum()) # Tiempos duplicados
    else:
        report['time_jumps'] = 0
        report['time_dupes'] = 0
        
    return report
