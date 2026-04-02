import pandas as pd

datos = [
    ["Laptop","Tech",1000,2],
    ["Mouse","Tech",20,10],
    ["Teclado","Tech",50,5],
    ["Silla","Hogar",150,3],
    ["Escritorio","Hogar",300,1],
]

df = pd.DataFrame(datos,columns=["Producto","Categoria","Precio","Cantidad"])

#¿Cuánto fueron los ingresos?
df["Ingresos"]= df["Precio"] * df["Cantidad"]

total = df["Ingresos"].sum()

#----------------------------------------------------------------------------------------------------------------------

#¿Qué producto generó más ingresos?

#índice del mayor ingreso
idx = df["Ingresos"].idxmax()

#Producto con mayor ingreso
producto_top = df.loc[idx, "Producto"]

#Ingreso máximo
ingreso_top = df.loc[idx, "Ingresos"]

#----------------------------------------------------------------------------------------------------------------------

#¿Qué categoría genera más ingresos?

resultado = df.groupby("Categoria")["Ingresos"].sum()

#----------------------------------------------------------------------------------------------------------------------

#¿Cuál es la mejor categoría?

idx = resultado.idxmax()

better = idx

#----------------------------------------------------------------------------------------------------------------------

#¿Qué porcentaje del total representa cada categoría?

porcentaje = resultado / total * 100

print (porcentaje)
