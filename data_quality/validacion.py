import pandas as pd
import re

def ejecutar_validaciones(almacen_datos):
    print("Validacion de registros de sobrevivientes")
    df = almacen_datos['Titanic'].copy()
    sobrevivientes=(df["2urvived"]==1) & (df["Pclass"].notna())
    df_sobrevivientes=df[sobrevivientes].copy()

    almacen_datos['registro sobrevivientes']=df_sobrevivientes
    print("Validacion exitosa de sobrevivientes")

    return(almacen_datos)