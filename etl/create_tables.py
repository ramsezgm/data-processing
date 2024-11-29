import pymysql
from pymysql.err import Error

def create_database_and_tables():
    connection = None
    try:
        # Conexión a MySQL
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Ramses27311914', 
            port=3306
        )

        # Verificar conexión
        if connection:
            print("Conexión establecida con MySQL.")

        cursor = connection.cursor()

        # Crear la base de datos
        cursor.execute("CREATE DATABASE IF NOT EXISTS sales;")
        cursor.execute("USE sales;")

        # Crear tablas
        queries = [
            """
            CREATE TABLE IF NOT EXISTS gender (
                gender_id INT AUTO_INCREMENT PRIMARY KEY,
                gender VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS customer (
                customer_id INT PRIMARY KEY,
                age INT NOT NULL,
                frequency_of_purchases INT NOT NULL,
                promo_code_used BOOLEAN NOT NULL,
                subscription_status BOOLEAN NOT NULL,
                gender_id INT NOT NULL,
                FOREIGN KEY (gender_id) REFERENCES gender(gender_id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS location (
                location_id INT AUTO_INCREMENT PRIMARY KEY,
                location VARCHAR(100) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS item (
                item_id INT AUTO_INCREMENT PRIMARY KEY,
                item VARCHAR(100) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS color (
                color_id INT AUTO_INCREMENT PRIMARY KEY,
                color VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS payment_method (
                payment_method_id INT AUTO_INCREMENT PRIMARY KEY,
                payment_method VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS purchase (
                purchase_id INT AUTO_INCREMENT PRIMARY KEY,
                item_id INT NOT NULL,
                location_id INT NOT NULL,
                color_id INT NOT NULL,
                payment_method_id INT NOT NULL,
                customer_id INT NOT NULL,
                purchase_amount DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (item_id) REFERENCES item(item_id),
                FOREIGN KEY (location_id) REFERENCES location(location_id),
                FOREIGN KEY (color_id) REFERENCES color(color_id),
                FOREIGN KEY (payment_method_id) REFERENCES payment_method(payment_method_id),
                FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
            );
            """
        ]

        for query in queries:
            cursor.execute(query)

        print("Base de datos y tablas creadas exitosamente.")

    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

# Ejecutar el script
if __name__ == "__main__":
    create_database_and_tables()
