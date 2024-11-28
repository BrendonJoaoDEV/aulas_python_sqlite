# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Sebastião Marcos.
# Data: 27/11/2024.
# Importar a biblioteca do sqlite3 e criar a variável de conexão.

import sqlite3

# Conn: é a variável para conexão com o banco de dados.
conn = sqlite3.connect("bancos_dados/meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()

# Criando uma tabela:
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
""")