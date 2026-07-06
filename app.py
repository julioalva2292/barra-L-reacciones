import streamlit as st
import math
from dibujo import dibujar_barra

# -------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -------------------------------------------------
st.set_page_config(page_title="Cálculo de Reacciones", page_icon="", layout="wide")

# -------------------------------------------------
# ESTILOS PERSONALIZADOS (TODOS LOS BOTONES ROJOS)
# -------------------------------------------------
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #dc3545 !important; /* rojo */
        color: white !important;
        border-radius: 10px;
        font-size: 16px;
        padding: 12px 20px;
        font-weight: bold;
        border: none;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #c82333 !important;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# INICIALIZAR VALORES
# -------------------------------------------------
defaults = {"fuerza": 300.0, "distancia": 180.0, "altura": 240.0}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -------------------------------------------------
# TÍTULO
# -------------------------------------------------
st.markdown("<h1 style='color:#2E86C1;'>Software para el cálculo de reacciones en una barra en L (ejercicio 4.61)</h1>", unsafe_allow_html=True)
st.markdown("Este software permite calcular las reacciones de una barra en **L** sometida a una fuerza horizontal.")

st.divider()

# -------------------------------------------------
# DATOS DE ENTRADA
# -------------------------------------------------
st.markdown("<h2 style='color:#117A65;'> Datos de entrada</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    fuerza = st.number_input("Fuerza aplicada (N)", min_value=0.0, step=10.0, key="fuerza")
with col2:
    distancia = st.number_input("Distancia a (mm)", min_value=0.0, step=10.0, key="distancia")
with col3:
    altura = st.number_input("Altura BC (mm)", min_value=0.0, step=10.0, key="altura")

st.divider()

# -------------------------------------------------
# GRÁFICO
# -------------------------------------------------
st.markdown("<h2 style='color:#D35400;'> Representación gráfica</h2>", unsafe_allow_html=True)
fig = dibujar_barra(st.session_state.fuerza, st.session_state.distancia, st.session_state.altura)
st.pyplot(fig, use_container_width=False)

st.divider()

# -------------------------------------------------
# FUNCIONES DE CÁLCULO
# -------------------------------------------------
def calcular_resultados(fuerza, distancia, altura):
    if distancia <= 0 or altura <= 0 or fuerza <= 0:
        return None
    diagonal = math.sqrt(distancia**2 + altura**2)
    reaccion_A = fuerza * altura / distancia
    reaccion_B = fuerza * diagonal / distancia
    beta = math.degrees(math.asin(reaccion_A / reaccion_B))
    return diagonal, reaccion_A, reaccion_B, beta

# -------------------------------------------------
# FUNCIONES DE BOTONES
# -------------------------------------------------
def cargar_libro():
    st.session_state["fuerza"] = 300.0
    st.session_state["distancia"] = 180.0
    st.session_state["altura"] = 240.0
    st.success(" Valores del libro cargados correctamente")

def borrar_todo():
    st.session_state["fuerza"] = 0.0
    st.session_state["distancia"] = 0.0
    st.session_state["altura"] = 0.0
    st.info(" Valores borrados")

# -------------------------------------------------
# BOTONES DEBAJO DEL GRÁFICO
# -------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
calcular = col1.button("Calcular", key="btn_calcular")
ejercicio = col2.button("Ejercicio del libro", key="btn_libro", on_click=cargar_libro)
procedimiento = col3.button("Ver procedimiento", key="btn_proc")
borrar = col4.button("Borrar todo", key="btn_borrar", on_click=borrar_todo)

# -------------------------------------------------
# RESULTADOS
# -------------------------------------------------
if calcular or procedimiento or ejercicio:
    resultados = calcular_resultados(st.session_state.fuerza, st.session_state.distancia, st.session_state.altura)
    if resultados:
        diagonal, reaccion_A, reaccion_B, beta = resultados
        if calcular or ejercicio:
            st.markdown("<h2 style='color:#8E44AD;'> Resultados</h2>", unsafe_allow_html=True)
            st.write(f"Diagonal = {diagonal:.2f} mm")
            st.write(f"Reacción A = {reaccion_A:.2f} N")
            st.write(f"Reacción B = {reaccion_B:.2f} N")
            st.write(f"Ángulo β = {beta:.2f}°")
        if procedimiento:
            with st.expander(" Procedimiento paso a paso", expanded=True):
                st.markdown(f"""
                **Paso 1**  
                Diagonal = √(a² + h²) = √({st.session_state.distancia}² + {st.session_state.altura}²) = {diagonal:.2f} mm  

                **Paso 2**  
                A = Fuerza × h / a = {st.session_state.fuerza} × {st.session_state.altura} / {st.session_state.distancia} = {reaccion_A:.2f} N  

                **Paso 3**  
                B = Fuerza × Diagonal / a = {st.session_state.fuerza} × {diagonal:.2f} / {st.session_state.distancia} = {reaccion_B:.2f} N  

                **Paso 4**  
                β = asin(A / B) = asin({reaccion_A:.2f}/{reaccion_B:.2f}) = {beta:.2f}°
                """)
    else:
        st.error(" Los valores deben ser mayores que cero.")
