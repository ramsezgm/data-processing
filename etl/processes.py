import pandas as pd

# 1. Lectura del archivo
df = pd.read_csv('./data/shopping_trends.csv')

# 2. Transformación de los datos

# Convertir columnas a tipo 'category' para variables categóricas
categorical_columns = ['Gender', 'Item Purchased', 'Category', 'Location', 'Size', 'Color', 
                       'Season', 'Payment Method', 'Shipping Type', 'Preferred Payment Method']

for col in categorical_columns:
    df[col] = df[col].astype('category')


# Convertir 'Subscription Status', 'Discount Applied', 'Promo Code Used' de 'Yes'/'No' a 1/0
df['Subscription Status'] = df['Subscription Status'].map({'Yes': 1, 'No': 0})
df['Discount Applied'] = df['Discount Applied'].map({'Yes': 1, 'No': 0})
df['Promo Code Used'] = df['Promo Code Used'].map({'Yes': 1, 'No': 0})

# Convertir 'Frequency of Purchases' a números (días)
frequency_map = {
    'Fortnightly': 15, 'Weekly': 7, 'Annually': 365, 'Monthly': 30, 'Quarterly': 91,
    'Bi-Weekly': 14, 'Every 3 Months': 90
}
df['Frequency of Purchases'] = df['Frequency of Purchases'].map(frequency_map)

# 3. Guardar el archivo procesado
df.to_csv('./data/sales.csv', index=False)
