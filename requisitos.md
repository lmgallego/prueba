Requisitos funcionales
RF1. Carga de dos archivos CSV

La aplicación deberá permitir al usuario subir dos archivos CSV correspondientes a dos actividades de ciclismo distintas.

Debe incluir:

Dos widgets de carga independientes.

Validación de que ambos archivos han sido cargados.

Visualización del nombre de cada archivo.

Opción para reemplazar cualquiera de los dos archivos sin reiniciar la app.

RF2. Lectura robusta del CSV

La aplicación deberá leer ambos CSV de forma robusta para minimizar fallos de parseo.

Debe incluir:

Lectura con soporte para BOM (utf-8-sig).

Detección o configuración de separador.

Conversión segura de columnas numéricas.

Gestión de valores nulos, vacíos o corruptos.

Mensajes claros si el archivo no puede parsearse.

RF3. Normalización de encabezados

La aplicación deberá normalizar los nombres de columnas para trabajar internamente con un esquema estándar.

Debe incluir:

Conversión automática de encabezados a minúsculas.

Eliminación de espacios extra.

Mapeo de nombres equivalentes.

Ejemplo de normalización interna:

heartrate → heart_rate

watts → power

velocity_smooth → speed

dfa_a1 → dfa_alpha_1

RF4. Validación estructural del archivo

La aplicación deberá comprobar si cada CSV contiene los campos mínimos necesarios para el análisis.

Campos mínimos recomendados:

time

watts

heartrate

Campos opcionales:

cadence

distance

velocity_smooth

temp

torque

dfa_a1

respiration

artifacts

PercentageinZ2

RRa1

RespirationRateAlphaHRV

Stamina

Debe incluir:

Informe de columnas detectadas.

Aviso de columnas obligatorias ausentes.

Distinción entre columnas obligatorias y opcionales.

RF5. Previsualización de datos

La aplicación deberá mostrar una vista previa de los datos cargados.

Debe incluir:

Primeras filas de cada CSV.

Número de filas y columnas.

Tipo de dato inferido por columna.

Resumen de nulos por columna.

RF6. Análisis descriptivo básico por actividad

La aplicación deberá generar un análisis individual de cada actividad.

Debe incluir como mínimo:

Duración total

Potencia media

Potencia máxima

Frecuencia cardíaca media

Frecuencia cardíaca máxima

Cadencia media y máxima, si existe

Velocidad media, si existe

Distancia total, si existe

Temperatura media, si existe

RF7. Comparación entre las dos actividades

La aplicación deberá comparar ambas actividades.

Debe incluir:

Comparativa de duración

Comparativa de potencia media y máxima

Comparativa de frecuencia cardíaca media y máxima

Comparativa de cadencia, velocidad y distancia si existen

Diferencia absoluta y porcentual entre métricas

RF8. Visualización gráfica

La aplicación deberá mostrar gráficos temporales de las métricas disponibles.

Debe incluir:

Potencia vs tiempo

Frecuencia cardíaca vs tiempo

Cadencia vs tiempo, si existe

DFA alpha 1 vs tiempo, si existe

Respiración vs tiempo, si existe

Velocidad vs tiempo, si existe

Recomendación funcional:

Posibilidad de activar/desactivar series.

Superposición de ambas actividades o visualización separada.

RF9. Detección dinámica de métricas opcionales

La aplicación deberá adaptar el análisis a las columnas presentes en cada CSV.

Debe incluir:

Si existe dfa_a1, mostrar análisis de DFA alpha 1.

Si existe respiration o RespirationRateAlphaHRV, mostrar análisis respiratorio.

Si existe torque, mostrar análisis de torque.

Si existe Stamina, mostrar evolución de stamina.

Si existe artifacts, mostrar porcentaje o magnitud de artefactos.

RF10. Informe de calidad del archivo

La aplicación deberá generar un diagnóstico técnico del CSV cargado.

Debe incluir:

Columnas válidas

Columnas desconocidas

Columnas vacías

Valores no numéricos en columnas esperadas como numéricas

Tramos temporales inconsistentes

Saltos o duplicados en time, si aparecen

RF11. Exportación de resultados

La aplicación deberá permitir exportar los resultados del análisis.

Debe incluir:

Exportación de resumen en CSV o Excel

Exportación opcional a PDF o Markdown

Descarga de métricas comparativas

RF12. Interfaz clara orientada a usuario no técnico

La aplicación deberá presentar los resultados de forma comprensible.

Debe incluir:

Títulos claros

Mensajes de error entendibles

Resumen ejecutivo por actividad

Indicadores visuales de qué datos están disponibles y cuáles no

Requisitos no funcionales
RNF1. Tecnología base

La aplicación deberá estar desarrollada con:

Frontend y lógica de interfaz: Streamlit

Procesamiento de datos: Pandas

Gráficos: Plotly o Altair

Validación y utilidades: Python

RNF2. Robustez de lectura

La aplicación deberá tolerar pequeñas variaciones en los archivos de entrada.

Debe soportar:

Archivos con BOM

Columnas en distinto orden

Mayúsculas/minúsculas distintas

Presencia o ausencia de columnas opcionales

Valores nulos parciales

RNF3. Rendimiento

La aplicación deberá cargar y analizar archivos de tamaño medio de forma fluida.

Objetivo recomendado:

Carga y análisis inicial en pocos segundos para archivos de varias miles de filas.

Interacción fluida con gráficos y tablas.

RNF4. Escalabilidad lógica

Aunque inicialmente se cargarán dos CSV, la arquitectura deberá facilitar ampliación futura.

Debe permitir evolucionar a:

Comparación de más de dos actividades

Análisis por bloques o laps

Carga masiva de actividades

Integración con otros formatos como FIT o CSV exportados desde otras plataformas

RNF5. Mantenibilidad

El código deberá estar organizado en módulos claros.

Recomendación de estructura:

app.py

parser.py

validators.py

analysis.py

charts.py

utils.py

RNF6. Tolerancia a errores

La aplicación no deberá romperse ante archivos mal formados.

Debe incluir:

try/except en lectura

validación previa antes del análisis

mensajes de error específicos

fallback cuando falten columnas opcionales

RNF7. Usabilidad

La aplicación deberá ser fácil de usar sin conocimientos técnicos avanzados.

Debe incluir:

flujo lineal de uso

feedback inmediato

tablas legibles

gráficos claros

botones de descarga visibles

RNF8. Compatibilidad

La aplicación deberá funcionar en entorno local y en despliegue web.

Entornos recomendados:

Local con streamlit run app.py

Streamlit Community Cloud

VPS con Docker

Servidor propio

RNF9. Reproducibilidad

El análisis deberá devolver siempre el mismo resultado para el mismo archivo de entrada.

Debe incluir:

reglas de parseo definidas

conversiones de tipos consistentes

normalización estandarizada de columnas

RNF10. Seguridad básica

Si la app se usa solo en local, la seguridad puede ser mínima.
Si se despliega online, deberá contemplar:

control de acceso

limitación de tamaño de archivos

validación de entradas

no ejecución de contenido arbitrario

aislamiento de sesiones de usuario
