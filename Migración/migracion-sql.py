import pandas as pd
from mysql.connector import connect, Error

# Conexión al servidor MySQL
conexion = connect(host="localhost", port="3306", user="root", password="12345678")

cursor = conexion.cursor()

# Crear la base de datos si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS bilboard")
cursor.execute("USE bilboard;")  # Seleccionar la base de datos

# Crear las tablas artists y songs
cursor.execute("""
CREATE TABLE IF NOT EXISTS artists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    song_name VARCHAR(255) NOT NULL,
    artist_id INT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(id)
)
""")

# Lista de datasets
datasets = ["datasets/bilboard200.csv", "datasets/global200.csv", "datasets/hot100.csv", "datasets/tiktok50.csv"]

# Procesar los datasets
for dataset in datasets:
    # Cargar el dataset
    df = pd.read_csv(dataset)

    # Obtener el nombre de la tabla basado en el nombre del archivo
    table_name = dataset.split("/")[-1].replace(".csv", "")

    # Reemplazar valores NaN con un texto predeterminado
    df.fillna({"Artist": "Desconocido", "SongName": "Sin título"}, inplace=True)

    # Crear las columnas para la tabla basadas en el DataFrame
    columns = []
    for column in df.columns:
        # Determinar tipo de dato básico para cada columna
        if df[column].dtype == 'int64':
            columns.append(f"`{column}` INT")
        elif df[column].dtype == 'float64':
            columns.append(f"`{column}` FLOAT")
        else:
            columns.append(f"`{column}` VARCHAR(255)")

    # Crear la definición de la tabla
    columns_def = ", ".join(columns)
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS `{table_name}` (
        id INT AUTO_INCREMENT PRIMARY KEY,
        {columns_def}
    )
    """
    cursor.execute(create_table_query)