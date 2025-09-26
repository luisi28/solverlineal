# archivo: app.py
import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de primer grado", page_icon="🧮")

st.title("🧮 Resolver ecuaciones de primer grado")
st.write("Intenta resolver la ecuación y verifica tu respuesta.")

# Generamos una ecuación aleatoria de la forma ax + b = c
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.c = random.randint(-10, 20)

a = st.session_state.a
b = st.session_state.b
c = st.session_state.c

# Ecuación
st.latex(f"{a}x + {b} = {c}")

# Solución correcta
correct_x = (c - b) / a

# Entrada del usuario
user_answer = st.number_input("Ingresa el valor de x (entero):", step=1, format="%d")

if st.button("Verificar"):
    if user_answer == correct_x and correct_x.is_integer():
        st.success("✅ ¡Correcto! Bien hecho 🎉")
        st.balloons()
        # Nueva ecuación después de resolver
        st.session_state.a = random.randint(1, 10)
        st.session_state.b = random.randint(-10, 10)
        st.session_state.c = random.randint(-10, 20)
    else:
        st.error("❌ Respuesta incorrecta. Intenta de nuevo.")
