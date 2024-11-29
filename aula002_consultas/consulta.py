# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Sebastião Marcos.
# Data: 28/11/2024.
# Executando uma consulta simples.

import os
import sqlite3

conn = sqlite3.connect("bancos_dados/meu_banco_de_dados.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system("cls")
for row in resultados:
    print(row)
conn.close()