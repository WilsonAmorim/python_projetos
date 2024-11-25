import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
sales_data = pd.read_csv("produtos.csv")

# Análise exploratória
print(sales_data.head())
print(sales_data.describe())

# Visualização
plt.figure(figsize=(10, 6))
plt.bar(sales_data["marca"], sales_data["custo"])
plt.xlabel("marca")
plt.ylabel("custo")
plt.title("Sales by Product")
plt.show()