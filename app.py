#LIBRERIAS
import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.image("menu.png") 
st.title("Proyecto Aplicado en Streamlit")
menu = st.sidebar.selectbox(
    "Menú de navegación",
    ["Home","Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

#MENU(home)
def home():
    st.write("Laura Fabiana Coronel Velásquez")
    st.write("Módulo 1 - Python Fundamentals")
    st.write("2026")
    st.write("Objetivo del trabajo: Construir una aplicación interactiva en Streamlit que integre variables, estructuras de datos, control de flujo, funciones, programación funcional y POO, mediante ejercicios prácticos de gestión financiera")
    st.write("Librerias utilizadas:")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Numpy")

#EJERCICIO 1: Variables y Condicionales
def ejercicio1():
    st.subheader("Variables y Condicionales")
    Presupuesto = st.number_input("Ingrese el presupuesto:",min_value=0.0)
    Gasto = st.number_input("Ingrese el gasto:",min_value=0.0)
    if st.button("Evaluar"):
        if Gasto <= Presupuesto:
            st.success("El gasto está dentro del presupuesto")
        else:
            st.error("El presupuesto fue excedido")
        diferencia = Presupuesto - Gasto
        st.write(f"La diferencia entre presupuesto y gasto es: {diferencia}")

#EJERCICIO 2: Listas y Diccionarios
def ejercicio2():
    if "actividades" not in st.session_state:
        st.session_state.actividades = []
    st.subheader("Listas y Diccionarios")
    nombre = st.text_input("Nombre de la actividad:")
    tipo = st.selectbox("Tipo de actividad:", ["Ingreso", "Gasto", "Ahorro", "Otro"])
    presupuesto = st.number_input("Presupuesto:", min_value=0.0)
    gasto_real = st.number_input("Gasto real:", min_value=0.0)

    if st.button("Agregar actividad"):
        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }
        st.session_state.actividades.append(actividad)
        st.success(f"Actividad '{nombre}' registrada correctamente.")

    if st.session_state.actividades:
        df = pd.DataFrame(st.session_state.actividades)
        st.subheader("Actividades registradas")
        st.dataframe(df)
        st.subheader("Estado de cada actividad")
        for act in st.session_state.actividades:
            if act["gasto_real"] <= act["presupuesto"]:
                st.write(f"Dentro del presupuesto")
            else:
                st.write(f"Presupuesto excedido")

#EJERCICIO 3: Funciones y Programación Funcional            
def ejercicio3():
    if "actividades" not in st.session_state:
        st.session_state.actividades = []
    st.subheader("Funciones y Programación Funcional")
    def calcular_retorno(actividad, tasa, meses):
        return actividad["presupuesto"] * tasa * meses
    tasa = st.slider("Selecciona la tasa:", min_value=0.0, max_value=1.0, step=0.01)
    meses = st.number_input("Número de meses:", min_value=1, value=1)
    if st.button("Calcular retorno esperado"):
        if st.session_state.actividades:
            retornos = list(map(lambda act: calcular_retorno(act, tasa, meses), st.session_state.actividades))
            st.subheader("Retorno esperado por actividad")
            for act, ret in zip(st.session_state.actividades, retornos):
                st.write(f"Retorno esperado = {ret:.2f}")
        else:
            st.warning("No hay actividades registradas aún.")

#EJERCICIO 4: Programación Orientada a Objetos (POO)       
def ejercicio4():
    st.subheader("Programación Orientada a Objetos (POO)")
    if "actividades_objetos" not in st.session_state:
        st.session_state.actividades_objetos = []
    
    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real
        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto
        def mostrar_info(self):
            return f"{self.nombre} ({self.tipo}) - Presupuesto: {self.presupuesto}, Gasto real: {self.gasto_real}"
   
    nombre = st.text_input("Nombre de la actividad:")
    tipo = st.selectbox("Tipo de actividad:", ["Ingreso", "Gasto", "Ahorro", "Otro"])
    presupuesto = st.number_input("Presupuesto:", min_value=0.0)
    gasto_real = st.number_input("Gasto real:", min_value=0.0)

    if st.button("Agregar actividad (POO)"):
        nueva_actividad = Actividad(nombre, tipo, presupuesto, gasto_real)
        st.session_state.actividades_objetos.append(nueva_actividad)
        st.success(f"Actividad '{nombre}' creada como objeto correctamente.")

    if st.session_state.actividades_objetos:
        st.subheader("Actividades registradas (Objetos)")
        for act in st.session_state.actividades_objetos:
            st.write(act.mostrar_info())
            if act.esta_en_presupuesto():
                st.success("Está dentro del presupuesto.")
            else:
                st.warning("Presupuesto excedido.")

#PARA QUE SE EJECUTE CADA SECCION 
if menu == "Home":
    home()
elif menu == "Ejercicio 1":
    ejercicio1()
elif menu == "Ejercicio 2":
    ejercicio2()
elif menu == "Ejercicio 3":
    ejercicio3()
elif menu == "Ejercicio 4":
    ejercicio4()