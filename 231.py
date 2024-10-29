from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
import random
from datetime import datetime, timedelta

# Создание SparkSession
spark = SparkSession.builder \
    .appName("Synthetic Purchase Data Generation") \
    .getOrCreate()

# Параметры генерации данных
num_rows = 1000  # Минимальное количество строк
products = ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet"]
min_quantity = 1
max_quantity = 10
min_price = 50.0
max_price = 1000.0

# Генерация данных
data = []
start_date = datetime.now() - timedelta(days=365)

for _ in range(num_rows):
    order_date = start_date + timedelta(days=random.randint(0, 364))  # Случайная дата в пределах последнего года
    user_id = random.randint(1, 1000)  # Случайный UserID
    product = random.choice(products)  # Случайный продукт
    quantity = random.randint(min_quantity, max_quantity)  # Случайное количество
    price = round(random.uniform(min_price, max_price), 2)  # Случайная цена с округлением до 2 знаков после запятой

    data.append((order_date.strftime("%Y-%m-%d"), user_id, product, quantity, price))

# Создание DataFrame
columns = ["Date", "User ID", "Product", "Quantity", "Price"]
df = spark.createDataFrame(data, columns)

# Сохранение DataFrame в формате CSV
output_path = ""
df.write.csv(output_path, header=True, mode="overwrite")

# Завершение работы SparkSession
spark.stop()
