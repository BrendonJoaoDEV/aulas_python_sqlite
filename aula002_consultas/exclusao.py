# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Sebastião Marcos.
# Data: 28/11/2024.
# Excluindo dados.

import os
import sqlite3

conn = sqlite3.connect("bancos_dados/meu_banco_de_dados.db")

cursor = conn.cursor()

os.system('cls')

nome_cliente = input("Digite o nome do cliente para excluir: ")

# Executa a esclusão com base no nome fornecido pelo usuário:
cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome_cliente,))
conn.commit()

print('Cliente deletado com sucesso!')

# Fecha a conexão:
conn.close()