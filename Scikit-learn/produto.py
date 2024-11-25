import pandas as pd

# Carregar os dados do CSV (substitua 'produtos.csv' pelo nome do seu arquivo)
df = pd.read_csv('produtos.csv', names=['codigo', 'marca', 'tipo', 'categoria', 'preco_unitario', 'custo', 'obs'])

##print(df)

# Criando uma coluna 'quantidade_vendida' aleatória para demonstração
import random
df['quantidade_vendida'] = [random.randint(10, 100) for _ in range(len(df))]

# Agrupando os dados por produto e somando a quantidade vendida
produtos_mais_vendidos = df.groupby('marca')['quantidade_vendida'].sum().reset_index()

# Ordenando os produtos pela quantidade vendida em ordem decrescente
produtos_mais_vendidos = produtos_mais_vendidos.sort_values('quantidade_vendida', ascending=False)

print(produtos_mais_vendidos)

import matplotlib.pyplot as plt

# Plotando um gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(produtos_mais_vendidos['marca'], produtos_mais_vendidos['quantidade_vendida'])
plt.xlabel('marca')
plt.ylabel('Quantidade Vendida')
plt.title('Produtos Mais Vendidos')
plt.xticks(rotation=45)
plt.show()