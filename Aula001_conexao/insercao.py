# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Sebastião Marcos.
# Data: 27/11/2024.
# Inserindo dados na tabela clientes.

import sqlite3

# Conexão com o banco de dados:
conn = sqlite3.connect("bancos_dados/meu_banco_de_dados")

cursor = conn.cursor()

# Definição de uma tupla com os dados:
dados_cliente = ("joão Silva", 30)

# Placeholders (?, ?): Os pomtos de interrogação são usados como
# "espaços reservados". Eles serão substituídos pelos valores da
# tupla dados_cliente (ou seja, "João Silva" e 30).
# Por quê: Usar placeholders é uma prática recomendada,
# pois previne ataques de injeção de SQL.
cursor.execute("INSERT INTO clientes (nome, idade) VALUES (?, ?)", dados_cliente)

conn.commit() # Salva a transação no banco de dados.
conn.close() # Fecha conexão.