import sqlite3

# 1. Conectar a la base de datos (si no existe, se crea el archivo ventas.db)
conn = sqlite3.connect("ventas.db")

# Creamos un "cursor", que es el objeto que nos permite ejecutar comandos SQL
cursor = conn.cursor()


# 2. Eliminar la tabla si ya existe (para evitar duplicados al ejecutar varias veces)
cursor.execute("DROP TABLE IF EXISTS ventas")


# 3. Crear la tabla "ventas" con sus columnas
cursor.execute("""
CREATE TABLE ventas (
    producto TEXT,      -- nombre del producto
    categoria TEXT,     -- categoría (Tech, Hogar, etc.)
    precio INTEGER,     -- precio por unidad
    cantidad INTEGER    -- cantidad vendida
)
""")


# 4. Insertar datos en la tabla
cursor.execute("""
INSERT INTO ventas VALUES
('Laptop','Tech',1000,2),
('Mouse','Tech',20,10),
('Teclado','Tech',50,5),
('Silla','Hogar',150,3),
('Escritorio','Hogar',300,1)
""")


# 5. Guardar los cambios en la base de datos
# (IMPORTANTE: sin esto, los datos no se guardan realmente)
conn.commit()


# 6. Consultar todos los datos de la tabla
cursor.execute("SELECT * FROM ventas")

# fetchall() trae todos los resultados de la consulta
filas = cursor.fetchall()


# 7. Mostrar los datos fila por fila
print("TODOS LOS DATOS:")
for fila in filas:
    print(fila)


# IMPORTANTE:
# 1-SELECT → Qué quiero ver
# 2-FROM → De dónde saco los datos
# 3-ORDER BY → Cómo organizo esos datos
# 4-LIMIT 1 → Cuántos resultados quiero
# 5-GROUP BY → Agrupar datos por algo
# 6- SUM(precio*cantidad) AS ingresos → “Calculá esto… y llamalo ingresos”


cursor.execute("""
SELECT 
        categoria, 
        SUM(precio*cantidad) * 100.0 / 
        (SELECT SUM(precio*cantidad) FROM ventas) AS porcentaje
FROM ventas
GROUP BY categoria
""")

resultado = cursor.fetchall()


# 9. Mostrar el resultado del análisis
print("\nEl porcentaje es: ")
for fila in resultado:
    print(fila)


# 10. Cerrar la conexión a la base de datos
conn.close()

import matplotlib.pyplot as plt

# separar datos
categorias = []
porcentajes = []

for fila in resultado:
    categorias.append(fila[0])
    porcentajes.append(round(fila[1], 2)) #o porcentajes.append(fila[1]) para barras sin redondear

# crear gráfico

# 1- % 👉 Indica que empieza un formato
# 2- 1.1 👉 primer 1: ancho mínimo, segundo 1: cantidad de decimales; es decir, mostrar 1 decimal
# 3- f 👉 float (número decimal)
# 4- %% 👉 imprime un % real.

explode = [0.1 if p == max(porcentajes) else 0 for p in porcentajes]

# colores (podés cambiarlos)
colores = ['#4CAF50', '#2196F3']

plt.figure(figsize=(6,6))

plt.pie(
    porcentajes,
    labels=categorias,
    autopct='%1.1f%%',
    explode=explode,
    colors=colores
)

plt.title("Distribución de ingresos por categoría")

plt.show()