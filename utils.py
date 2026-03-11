import pandas as pd
import io

def export_csv(df):
    # RNF11: Exportación en formato CSV
    buf = io.BytesIO()
    df.to_csv(buf, index=False, encoding='utf-8')
    buf.seek(0)
    return buf.getvalue()
