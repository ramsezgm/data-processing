import pymysql
import pandas as pd

def process_and_insert_data(csv_file):
    try:
        # Conexión a la base de datos
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Ramses27311914',
            database='sales',
            port=3306
        )

        cursor = connection.cursor()

        # Leer el archivo CSV
        data = pd.read_csv(csv_file)

        # Eliminar espacios en los nombres de las columnas
        data.columns = data.columns.str.strip()
        print(data.columns)

        # Generar IDs únicos para las tablas relacionadas
        genders = data['Gender'].drop_duplicates().reset_index(drop=True)
        genders = {gender: idx + 1 for idx, gender in enumerate(genders)}

        items = data['Item Purchased'].drop_duplicates().reset_index(drop=True)
        items = {item: idx + 1 for idx, item in enumerate(items)}

        locations = data['Location'].drop_duplicates().reset_index(drop=True)
        locations = {location: idx + 1 for idx, location in enumerate(locations)}

        colors = data['Color'].drop_duplicates().reset_index(drop=True)
        colors = {color: idx + 1 for idx, color in enumerate(colors)}

        payment_methods = data['Payment Method'].drop_duplicates().reset_index(drop=True)
        payment_methods = {method: idx + 1 for idx, method in enumerate(payment_methods)}

        # Insertar datos en las tablas relacionadas
        for gender, gender_id in genders.items():
            cursor.execute("""
                INSERT IGNORE INTO gender (gender_id, gender)
                VALUES (%s, %s)
            """, (gender_id, gender))

        for item, item_id in items.items():
            cursor.execute("""
                INSERT IGNORE INTO item (item_id, item)
                VALUES (%s, %s)
            """, (item_id, item))

        for location, location_id in locations.items():
            cursor.execute("""
                INSERT IGNORE INTO location (location_id, location)
                VALUES (%s, %s)
            """, (location_id, location))

        for color, color_id in colors.items():
            cursor.execute("""
                INSERT IGNORE INTO color (color_id, color)
                VALUES (%s, %s)
            """, (color_id, color))

        for method, method_id in payment_methods.items():
            cursor.execute("""
                INSERT IGNORE INTO payment_method (payment_method_id, payment_method)
                VALUES (%s, %s)
            """, (method_id, method))

        # Insertar datos en la tabla `customer` y `purchase`
        for _, row in data.iterrows():
            # Insertar en la tabla `customer`
            cursor.execute("""
                INSERT IGNORE INTO customer (customer_id, age, frequency_of_purchases, promo_code_used, subscription_status, gender_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['Customer ID'],
                row['Age'],
                row['Frequency of Purchases'],
                row['Promo Code Used'],
                row['Subscription Status'],
                genders[row['Gender']]
            ))

            # Insertar en la tabla `purchase`
            cursor.execute("""
                INSERT INTO purchase (item_id, location_id, color_id, payment_method_id, customer_id, purchase_amount)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                items[row['Item Purchased']],
                locations[row['Location']],
                colors[row['Color']],
                payment_methods[row['Payment Method']],
                row['Customer ID'],
                row['Purchase Amount (USD)']  # Asegúrate de que esta columna exista en el CSV
            ))

        # Confirmar los cambios
        connection.commit()
        print("Datos insertados exitosamente.")

    except pymysql.Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

# Ejecutar el script
if __name__ == "__main__":
    # Reemplaza './data/sales.csv' con la ruta de tu archivo CSV
    process_and_insert_data('./data/sales.csv')
