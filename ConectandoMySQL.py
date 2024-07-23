# CRUD
import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= 'root',
    database= 'aulaPython',
)

# Para executar essa conexão precisa de um cursor
cursor = conexao.cursor()
# Cursor é o cara que vai executar os comandos da conexão
#CREATE
nmProduto = "Melancia"
preco = 10.0
comando = f'INSERT INTO vendas(nmProduto, preco) VALUES ("{nmProduto}", "{preco}")'
cursor.execute(comando)
conexao.commit() # Edita o banco de dados -> INSERT

#READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # Ler o banco de dados
print(resultado)

#UPDATE 
preco = 11.0
comando = f'UPDATE vendas SET preco = "{preco}"'
cursor.execute(comando)
conexao.commit() # Edita o banco de dados -> UPDATE

#DELETE
nmProduto = "Melancia"
comando = f'DELETE FROM vendas WHERE nmProduto = "{nmProduto}"'
cursor.execute(comando)
conexao.commit() # Edita o banco de dados -> DELETE


cursor.close()
conexao.close()