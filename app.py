import streamlit as st
import pandas as pd
from parser_csv import read_csv_robust
from validators import validate_structure, quality_report
from analysis import compute_descriptives, compare_activities
from charts import plot_time_series
from utils import export_csv

st.set_page_config(page_title="Comparador de Actividades", layout="wide")

st.title("🚴‍♂️ Comparador de Actividades de Ciclismo")
st.markdown("Carga dos archivos CSV de tus actividades para comparar métricas clave.")

# Contenedores para la carga de datos (RF1)
col1, col2 = st.columns(2)
with col1:
    st.subheader("📥 Actividad 1")
    file1 = st.file_uploader("Sube el primer CSV", type=['csv'], key='f1')
    sep1 = st.selectbox("Separador A1", [',', ';', '\t'], key='s1')

with col2:
    st.subheader("📥 Actividad 2")
    file2 = st.file_uploader("Sube el segundo CSV", type=['csv'], key='f2')
    sep2 = st.selectbox("Separador A2", [',', ';', '\t'], key='s2')

def process_file(file, sep, name_label):
    df, err = read_csv_robust(file, sep=sep)
    if err:
        st.error(f"Error al leer {name_label} ({file.name}): {err}")
        return None, None
        
    val = validate_structure(df)
    qual = quality_report(df, val)
    
    if not val['is_valid']:
        st.error(f"❌ Faltan columnas obligatorias en {file.name}: {val['missing_mandatory']}")
    else:
        st.success(f"✅ Archivo cargado correctamente: {file.name}")
    
    with st.expander(f"🔍 Previsualización e Info - {name_label} ({file.name})"):
        st.write(df.head())
        st.caption(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Columnas Opcionales Detectadas:**")
            st.write(val['detected_optional'] if val['detected_optional'] else "Ninguna")
        with c2:
            st.markdown("**Reporte de Calidad:**")
            st.write(f"- Saltos de tiempo: {qual.get('time_jumps', 0)}")
            st.write(f"- Tiempos duplicados: {qual.get('time_dupes', 0)}")
            if qual.get('empty_columns'):
                st.write(f"- Columnas vacías: {qual['empty_columns']}")
            if val['unknown']:
                st.write(f"- Columnas desconocidas: {val['unknown']}")
                
    return df, val

if file1 and file2:
    st.divider()
    df1, val1 = process_file(file1, sep1, "Actividad 1")
    df2, val2 = process_file(file2, sep2, "Actividad 2")
    
    if df1 is not None and df2 is not None and val1['is_valid'] and val2['is_valid']:
        st.header("📊 Análisis Comparativo")
        
        # RF6 y RF7: Análisis descriptivo y comparación
        stats1 = compute_descriptives(df1)
        stats2 = compute_descriptives(df2)
        comp_df = compare_activities(stats1, stats2)
        
        st.dataframe(comp_df, use_container_width=True)
        
        c1, c2 = st.columns([1, 4])
        with c1:
            st.download_button(
                label="⬇️ Descargar Resumen CSV",
                data=export_csv(comp_df),
                file_name="comparativa_resumen.csv",
                mime="text/csv"
            )
        
        st.header("📈 Gráficos de Evolución")
        
        # RF8 y RF9: Visualización dinámica
        # Unir métricas disponibles en ambos df
        all_metrics = set(val1['all_detected']).union(set(val2['all_detected']))
        plotable_metrics = [m for m in all_metrics if m != 'time' and m in 
                            ['power', 'heart_rate', 'cadence', 'speed', 'distance', 'temp', 
                             'dfa_alpha_1', 'respiration', 'torque', 'stamina', 'artifacts']]
        
        if plotable_metrics:
            selected_metrics = st.multiselect("Selecciona métrica(s) a visualizar vs Tiempo", plotable_metrics, default=[plotable_metrics[0]])
            
            overlay = st.radio("Modo de visualización", ["Superpuesto (Solo para 1 métrica)", "Separado"])
            
            for m in selected_metrics:
                st.subheader(f"Evolución: {m}")
                fig = plot_time_series(df1, df2, m, [file1.name, file2.name], overlay == "Superpuesto (Solo para 1 métrica)")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No hay columnas graficables comunes detectadas.")
