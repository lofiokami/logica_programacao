from  conexao  import  conecta_db
from  menu     import  menu_resumido

def menu_cliente(titulo):
    menu_resumido(titulo)

    while True: 

        opcao   = input ("Escolha uma opção:")
        conexao = conecta_db()

        if opcao == "1":
            listar_clientes(conexao)
            menu_resumido(titulo)

        elif opcao == "2":
            listar_clientes(conexao)
            consultar_cliente_por_id(conexao)
            menu_resumido(titulo)

        elif opcao == "3":
            inserir_cliente(conexao)
            listar_clientes(conexao)
            menu_resumido(titulo)
        elif opcao == "4":
            listar_clientes(conexao)
            atualizar_cliente(conexao)
            listar_clientes(conexao)
            menu_resumido(titulo)

        elif opcao == "5":
            listar_clientes(conexao)
            delete_cliente(conexao)
            listar_clientes(conexao)
            menu_resumido(titulo)

        elif opcao == "6":
            print("Sair")

            break

        else:
            print("Opção invalida, tente novamente")

def listar_clientes(conexao):
    cursor = conexao.cursor()
    # Execução do select no banco de dados
    cursor.execute("select id,nome from cliente order by id asc")
    # recuperar todos registros
    registros = cursor.fetchall()
    print ("|----------------------------------------|")
    for registro in registros:
        print (f"| ID: {registro[0]}  - Nome: {registro[1]} ")
    print ("|----------------------------------------|")

def consultar_cliente_por_id(conexao):

    id      = input ("Digite o ID: ")
    cursor  = conexao.cursor()
    cursor.execute("select id,nome from cliente where id = " + id)
    registro = cursor.fetchone()

    if registro is None:
        print ("Cliente não encontrado:")
    else:
        print (f"| ID ..: {registro[0]} |")
        print (f"| Nome : {registro[1]} |")

def inserir_cliente(conexao):
    print ("Inserindo o Cliente ..: ")

    cursor = conexao.cursor()
    
    nome = input ("Nome :")
    sql_insert = "insert into cliente (nome) values ('" + nome + "')"
    cursor.execute(sql_insert)
    conexao.commit()

def atualizar_cliente(conexao):
    print ("Alterando dados dos clientes")
    cursor = conexao.cursor()

    id = input ("Digite o ID:")
    nome = input ("Nome : ")

    sql_update = "update cliente set nome = '" + nome + "' where id = "+ id 
    cursor.execute(sql_update)
    conexao.commit()

def delete_cliente(conexao):
    print ("Deletar Cliente")
    cursor = conexao.cursor()

    id = input ("Digite o ID:")

    sql_delete = "delete from cliente where id =" + id 
    cursor.execute(sql_delete)
    conexao.commit()